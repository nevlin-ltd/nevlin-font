"""Build the editable UFO sources with Fontmake; no binary font input required."""
from pathlib import Path
import os
import json
import hashlib
import math
from fontmake.font_project import FontProject
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables.ttProgram import Program
from fontTools.ttLib.removeOverlaps import removeOverlaps
from fontTools.ttLib.tables import otTables
from fontTools import subset
import glyphsLib
import ufoLib2
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

ROOT = Path(__file__).resolve().parent
# Fixed reproducible release timestamp, 2026-10-16 00:00 UTC.
os.environ.setdefault('SOURCE_DATE_EPOCH', '1792108800')

def simplify_straight_segments(font):
    """Remove redundant straight-line points within one design unit (1/2048 em).

    Never simplify a curve or a corner; retain almost-collinear points whose
    departure from the chord is greater than one unit.
    """
    from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
    for glyph in font['glyf'].glyphs.values():
        if glyph.numberOfContours <= 0:
            continue
        coords=[];flags=[];ends=[];start=0
        for end in glyph.endPtsOfContours:
            pts=list(zip(glyph.coordinates[start:end+1],glyph.flags[start:end+1]))
            changed=True
            while changed and len(pts)>3:
                changed=False
                for i in range(len(pts)):
                    (a,fa),(b,fb),(c,fc)=pts[i-1],pts[i],pts[(i+1)%len(pts)]
                    if not (fa&1 and fb&1 and fc&1):continue
                    ux,uy=b[0]-a[0],b[1]-a[1]
                    vx,vy=c[0]-b[0],c[1]-b[1]
                    dot=ux*vx+uy*vy
                    if dot<=0:continue
                    cross=ux*vy-uy*vx
                    angle=abs(math.atan2(cross,dot))
                    chord=math.hypot(c[0]-a[0],c[1]-a[1])
                    if angle<0.1 and chord and abs(cross)/chord<=1:
                        del pts[i];changed=True;break
            coords.extend(p for p,_ in pts);flags.extend(f for _,f in pts)
            ends.append(len(coords)-1);start=end+1
        glyph.coordinates=GlyphCoordinates(coords)
        glyph.flags=bytearray(flags)
        glyph.endPtsOfContours=ends
    for name in font.getGlyphOrder():
        g=font['glyf'][name];g.recalcBounds(font['glyf'])
        if hasattr(g,'xMin'):font['hmtx'][name]=(font['hmtx'][name][0],g.xMin)

def main():
    out = ROOT / 'fonts' / 'ttf'
    out.mkdir(parents=True, exist_ok=True)
    web = ROOT / 'fonts' / 'woff2'
    web.mkdir(parents=True, exist_ok=True)
    fonts = []
    source_dir = ROOT / 'sources' if (ROOT / 'sources').exists() else ROOT
    glyphs_sources = sorted(source_dir.glob('*.glyphs'))
    if glyphs_sources:
        generated = ROOT / 'build' / 'ufos'
        generated.mkdir(parents=True,exist_ok=True)
        ufo_sources=[]
        for source in glyphs_sources:
            masters=list(glyphsLib.to_ufos(glyphsLib.load(str(source)),ufo_module=ufoLib2))
            assert len(masters)==1, 'Each static source must contain one master'
            # Drop i/j dots before above accents, ignoring intervening below marks.
            import unicodedata
            ufo=masters[0]
            ogonek=ufo.newGlyph("iogonek.dotless")
            ufo["iogonek"].drawPoints(ogonek.getPointPen())
            ogonek.width=ufo["iogonek"].width
            for component in list(ogonek.components):
                if component.baseGlyph=="uni0307":ogonek.components.remove(component)
            import re
            def extend_mark_bases(match):
                names=match.group(1).split()
                if "iogonek" in names:names.append("iogonek.dotless")
                return "pos base ["+" ".join(names)+"]"
            ufo.features.text=re.sub(r"pos base \[([^\]]*)\]",extend_mark_bases,ufo.features.text)
            above=[g.name for g in ufo if any(unicodedata.combining(chr(c))==230 for c in g.unicodes)]
            ufo.features.text += "\n@NevlinAbove = [" + " ".join(above) + "] ;\nfeature ccmp {\nlookup NevlinSoftDots {\nlookupflag UseMarkFilteringSet @NevlinAbove;\nsub i' @NevlinAbove by dotlessi;\nsub j' @NevlinAbove by uni0237;\nsub iogonek' @NevlinAbove by iogonek.dotless;\n} NevlinSoftDots;\n} ccmp;\n"
            target=generated/(source.stem+'.ufo')
            masters[0].save(str(target),overwrite=True)
            ufo_sources.append(target)
    else:
        ufo_sources=sorted(source_dir.glob('*.ufo'))
    assert len(ufo_sources)==4, 'Expected four editable source weights'
    for source in ufo_sources:
        path = out / (source.stem.replace('Semibold', 'SemiBold') + '.ttf')
        FontProject().run_from_ufos([str(source)], output=['ttf'],
                                   output_path=str(path), use_production_names=False,
                                   remove_overlaps=True, overlaps_backend='pathops')
        f = TTFont(path, recalcTimestamp=False)
        gs=f.getGlyphSet()
        for name in f.getGlyphOrder():
            glyph=f['glyf'][name]
            if glyph.isComposite() and any(f['glyf'][c.glyphName].isComposite() for c in glyph.components):
                recording=DecomposingRecordingPen(gs)
                gs[name].draw(recording)
                pen=TTGlyphPen(None)
                recording.replay(pen)
                f['glyf'][name]=pen.glyph()
        # Remove overlaps after quadratic compilation as well. This handles
        # intersecting components and coincident segments consistently.
        removeOverlaps(f, removeHinting=True)
        simplify_straight_segments(f)
        f['name'].names = [n for n in f['name'].names if n.platformID != 1]
        # Preserve the human-readable labels for inherited ssXX/cvXX features.
        menus = json.loads((source_dir / 'feature-menus.json').read_text())
        for record in f['GSUB'].table.FeatureList.FeatureRecord:
            if record.FeatureTag in menus:
                data = menus[record.FeatureTag]
                params = getattr(otTables, data['type'])()
                params.__dict__.update(data['values'])
                record.Feature.FeatureParams = params
        # Keep all encoded characters and every OpenType feature, but discard
        # unused construction helpers left behind by overlap removal.
        options = subset.Options()
        options.layout_features = ['*']
        options.name_IDs = ['*']
        options.name_legacy = True
        options.name_languages = ['*']
        options.glyph_names = True
        options.notdef_outline = True
        options.recalc_timestamp = False
        sub = subset.Subsetter(options=options)
        sub.populate(unicodes=json.loads((ROOT / 'repertoire.json').read_text()))
        sub.subset(f)
        f['meta'] = newTable('meta')
        f['meta'].data = {'dlng': 'Latn', 'slng': 'Latn'}
        f['prep'] = newTable('prep')
        f['prep'].program = Program()
        f['prep'].program.fromBytecode(b'\xb8\x01\xff\x85\xb0\x04\x8d')
        f['gasp'] = newTable('gasp')
        f['gasp'].gaspRange = {65535: 15}
        fonts.append((path, f))
    # One clipping box for the entire family, large enough for every glyph.
    ymax = max(g.yMax for _, f in fonts for g in f['glyf'].glyphs.values() if hasattr(g, 'yMax'))
    ymin = min(g.yMin for _, f in fonts for g in f['glyf'].glyphs.values() if hasattr(g, 'yMin'))
    manifest = []
    for path, f in fonts:
        f['OS/2'].recalcAvgCharWidth(f)
        f['OS/2'].usWinAscent = ymax
        f['OS/2'].usWinDescent = -ymin
        f.save(path)
        manifest.append({'file': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        f.flavor = 'woff2'
        wpath = web / (path.stem + '.woff2')
        f.save(wpath)
        manifest.append({'file': str(wpath.relative_to(ROOT)), 'sha256': hashlib.sha256(wpath.read_bytes()).hexdigest()})
    (ROOT / 'qa').mkdir(exist_ok=True)
    (ROOT / 'qa' / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

if __name__ == '__main__':
    main()

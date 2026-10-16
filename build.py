"""Nevlin UI Plus: a SIL OFL 1.1 derivative of Inter 4.001.
Redraws eight base characters and figure variants; retains remaining upstream typography/shaping.
Requires fonttools, brotli. Redrawn shapes are in redraw.py. No previous Nevlin font artifacts are changed.
"""
from pathlib import Path
import json, hashlib, html
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib.tables.ttProgram import Program
from redraw import redraw_glyphs
R=Path(__file__).resolve().parent
(R/'source/upstream').mkdir(parents=True,exist_ok=True)
src=R/'InterVariable.ttf'
manifest=[]; reports=[]

def soft_square(g):
    x0,y0,x1,y1=g.xMin,g.yMin,g.xMax,g.yMax
    cx=(x0+x1)/2;cy=(y0+y1)/2;size=min(x1-x0,y1-y0)*.92
    a=cx-size/2;b=cy-size/2;c=cx+size/2;d=cy+size/2;r=size*.40
    p=TTGlyphPen(None)
    p.moveTo((a+r,b));p.lineTo((c-r,b));p.qCurveTo((c,b),(c,b+r));p.lineTo((c,d-r));p.qCurveTo((c,d),(c-r,d));p.lineTo((a+r,d));p.qCurveTo((a,d),(a,d-r));p.lineTo((a,b+r));p.qCurveTo((a,b),(a+r,b));p.closePath()
    return p.glyph()

for style,weight in [('Regular',400),('Medium',500),('Semibold',600),('Bold',700)]:
    f=instantiateVariableFont(TTFont(src),{'wght':weight+35,'opsz':28},inplace=True)
    glyf=f['glyf']; cmap=f.getBestCmap()
    for n in ['period','uni0307']:
        glyf[n]=soft_square(glyf[n]);glyf[n].recalcBounds(glyf)
        w,_=f['hmtx'][n];f['hmtx'][n]=(w,glyf[n].xMin)
    # A subtly longer outward tail, without altering Q's bowl.
    g=glyf['Q']; end=g.endPtsOfContours[0]; top=max(y for x,y in g.coordinates[:end+1]); bot=min(y for x,y in g.coordinates[:end+1])
    for i in range(end+1):
        x,y=g.coordinates[i];t=(top-y)/(top-bot);g.coordinates[i]=(x+60*t,y-12*t)
    g.program=Program();g.recalcBounds(glyf)
    # Slightly wider tenge crossbars, with its stem and vertical metrics retained.
    g=glyf[cmap[ord('₸')]];start=g.endPtsOfContours[0]+1;cx=(g.xMin+g.xMax)/2
    for i in range(start,len(g.coordinates)):
        x,y=g.coordinates[i];g.coordinates[i]=(cx+(x-cx)*1.045,y)
    g.program=Program();g.recalcBounds(glyf)
    n=cmap[ord('₸')];f['hmtx'][n]=(f['hmtx'][n][0],g.xMin)
    changed=redraw_glyphs(f,weight)
    assert glyf['g'].yMin >= f['hhea'].descent
    for n in changed:
        assert glyf[n].numberOfContours > 0
    changed_by_weight = {'weight':weight,'glyphs':changed}
    (R/'source'/f'changed-{weight}.json').write_text(json.dumps(changed_by_weight,indent=2))
    name=f['name']
    family='Nevlin UI Plus';ps='NevlinUIPlus-'+style
    updates={1:family if style=='Regular' else family+' '+style,2:'Regular',3:ps+';0.400',4:family+' '+style,5:'Version 0.400',6:ps,16:family,17:style,18:family+' '+style,25:'NevlinUIPlus',10:'Nevlin UI Plus prototype, derived from Inter 4.001. Independently redrawn a, e, g, r, t, 1, 4 and 7 with propagated figure variants. Slightly increased stroke weight. Retained custom dots, Q tail and tenge bars. Licensed under SIL OFL 1.1.'}
    for nid in updates:name.removeNames(nameID=nid)
    for nid,value in updates.items():
        name.setName(value,nid,3,1,0x409);name.setName(value,nid,1,0,0)
    # Preserve the upstream copyright and license records.
    f['head'].fontRevision=.4;f['OS/2'].usWeightClass=weight
    f['OS/2'].fsSelection=(f['OS/2'].fsSelection & ~(1|32))|64
    f['head'].macStyle=0
    fonts=R/'fonts';fonts.mkdir(exist_ok=True)
    path=fonts/(ps+'.ttf');f.save(path)
    # Export from reloaded, quantized outlines so SVGs match the installable font.
    f=TTFont(path);gs=f.getGlyphSet();cmap=f.getBestCmap();upem=f['head'].unitsPerEm
    out=R/'glyphs'/style;out.mkdir(parents=True,exist_ok=True)
    for cp,n in sorted(cmap.items()):
        p=SVGPathPen(gs);gs[n].draw(p);w=f['hmtx'][n][0]
        bp=BoundsPen(gs);gs[n].draw(bp);bounds=bp.bounds or (0,0,0,0)
        xmin=min(0,bounds[0]); xmax=max(w,1,bounds[2]); top=max(f['hhea'].ascent,bounds[3]); bottom=min(f['hhea'].descent,bounds[1])
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{xmin} {-top} {xmax-xmin} {top-bottom}"><title>Nevlin UI Plus {style} U+{cp:04X}</title><path transform="scale(1,-1)" fill="currentColor" d="{p.getCommands()}"/></svg>'
        fn=f'U+{cp:04X}.svg';(out/fn).write_text(svg)
        if style=='Regular':manifest.append({'character':chr(cp),'codepoint':f'U+{cp:04X}','glyph':n,'advance_width':w,'svg':f'glyphs/Regular/{fn}'})
    f.flavor='woff2';f.save(fonts/(ps+'.woff2'))
    for suffix in ['ttf','woff2']:
        check=TTFont(fonts/(ps+'.'+suffix));cm=check.getBestCmap()
        assert all(ord(c) in cm for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$€£¥₸₽₹₩₿')
        assert check['name'].getDebugName(16)==family
        assert 'GPOS' in check and 'GSUB' in check
        tags={r.FeatureTag for r in check['GSUB'].table.FeatureList.FeatureRecord}
        assert {'tnum','zero'}.issubset(tags)
        reports.append({'file':ps+'.'+suffix,'characters':len(cm),'family':family,'weight':weight,'readable':True,'redrawn_glyphs':changed,'tnum_zero_and_layout_tables':True})
(R/'glyph-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(R/'validation.json').write_text(json.dumps(reports,indent=2))
(R/'source/upstream/provenance.json').write_text(json.dumps({'source':'https://github.com/rsms/inter','font_url':'https://raw.githubusercontent.com/rsms/inter/master/docs/font-files/InterVariable.ttf','version':'4.001;git-9221beed3','sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'license':'SIL Open Font License 1.1','optical_size':28,'upstream_weight_offset':35,'custom_stem_increment':10,'customized_glyphs':['period','uni0307','Q','uni20B8'],'redrawn_base_glyphs':['a','e','g','r','t','one','four','seven'],'derived_glyphs':'Composite glyphs using period and uni0307 inherit the customized dots.'},indent=2))
(R/'nevlin-ui-plus.css').write_text('\n'.join(f'@font-face{{font-family:"Nevlin UI Plus";src:url("fonts/NevlinUIPlus-{s}.woff2") format("woff2");font-weight:{w};font-style:normal;font-display:swap;}}' for s,w in [('Regular',400),('Medium',500),('Semibold',600),('Bold',700)]))
print('Built',len(manifest),'characters,',len(manifest)*4,'SVGs, 8 font files.')

"""Build original Nevlin Sprout drawings into editable UFO, TTF, WOFF2 and SVG.
Run with Python 3.12 and the versions in requirements.txt. No base font is read.
"""
from pathlib import Path
import hashlib, json, unicodedata
from array import array
import pathops
from fontTools.agl import UV2AGL
from fontTools.svgLib.path import parse_path
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont, newTable
from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
from ufoLib2 import Font
from ufoLib2.objects import Component
from fontmake.font_project import FontProject
from sources.design import GLYPHS
from sources.extended import extend

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = [('Regular',400,64),('Medium',500,78),('SemiBold',600,92),('Bold',700,108)]
def name(cp): return UV2AGL.get(cp, f'uni{cp:04X}')
def stroke(paths, thickness):
    result = pathops.Path()
    for d in paths:
        p=pathops.Path(); parse_path(d,p.getPen())
        p.stroke(thickness,pathops.LineCap.BUTT_CAP,pathops.LineJoin.ROUND_JOIN,4)
        p.convertConicsToQuads(0.1)
        result.addPath(p)
    return result
def dot(x,y,size):
    s=size/2; r=size*.23
    d=f'M{x-s+r} {y-s} L{x+s-r} {y-s} Q{x+s} {y-s} {x+s} {y-s+r} L{x+s} {y+s-r} Q{x+s} {y+s} {x+s-r} {y+s} L{x-s+r} {y+s} Q{x-s} {y+s} {x-s} {y+s-r} L{x-s} {y-s+r} Q{x-s} {y-s} {x-s+r} {y-s} Z'
    p=pathops.Path();parse_path(d,p.getPen());return p
def transformed(path, dx=0,dy=0,sx=1,sy=1):
    p=pathops.Path(); path.draw(TransformPen(p.getPen(),(sx,0,0,sy,dx,dy)));return p
def write_glyph(font,n,width,path,cp=None):
    g=font.newGlyph(n);g.width=width
    if cp is not None:g.unicodes=[cp]
    if list(path):pathops.simplify(path,clockwise=False).draw(g.getPen())
    return g

def build(style,weight,t):
    f=Font();i=f.info
    i.familyName='Nevlin Sprout';i.styleName=style;i.unitsPerEm=1000
    i.ascender=1000;i.descender=-300;i.capHeight=700+t/2;i.xHeight=500+t/2
    i.versionMajor=1;i.versionMinor=1
    i.copyright='Copyright 2026 The Nevlin Sprout Project Authors (https://github.com/nevlin-ltd/nevlin-font)'
    i.openTypeNameDesigner='Nevlin Sprout Project Authors'
    i.openTypeNameDescription='Original geometric learning-interface typeface. Unreleased review candidate.'
    i.openTypeNameLicense='Licensed under the SIL Open Font License, Version 1.1.'
    i.openTypeNameLicenseURL='https://openfontlicense.org'
    i.openTypeOS2WeightClass=weight;i.openTypeOS2WidthClass=5
    i.openTypeOS2VendorID='NONE';i.openTypeOS2Type=[]
    i.openTypeOS2TypoAscender=1000;i.openTypeOS2TypoDescender=-300;i.openTypeOS2TypoLineGap=0
    i.openTypeOS2WinAscent=1050;i.openTypeOS2WinDescent=350
    i.openTypeHheaAscender=1000;i.openTypeHheaDescender=-300;i.openTypeHheaLineGap=0
    i.openTypeOS2Selection=[7,8]
    paths={}; widths={}
    for c,(w,ds) in GLYPHS.items():
        p=stroke(ds,t)
        dots={'i':[(115,670)],'j':[(140,670)],'.':[(115,25)],'·':[(115,300)],':':[(115,25),(115,380)],';':[(115,380)],'!':[(115,25)],'?':[(225,25)],'…':[(115,25),(345,25),(575,25)],'•':[(150,300)],'÷':[(285,535),(285,65)]}
        for x,y in dots.get(c,[]):p.addPath(dot(x,y,t*1.35 if c!='•' else t*1.7))
        paths[c]=p;widths[c]=w
    for c in '<>≤≥':
        paths[c]=transformed(paths[c],15);widths[c]=570
    paths['\u00a0']=pathops.Path();widths['\u00a0']=280
    for c,base in [('ı','i'),('ȷ','j')]:paths[c]=stroke(GLYPHS[base][1],t);widths[c]=GLYPHS[base][0]
    # Marks centered on x=0, origin y=0. Composite placement is explicit.
    marks={
      '\u0300':stroke(['M-70 170 L55 65'],t*.85),
      '\u0301':stroke(['M-55 65 L70 170'],t*.85),
      '\u0302':stroke(['M-110 65 L0 170 L110 65'],t*.8),
      '\u0303':stroke(['M-125 95 C-55 205 55 5 125 115'],t*.75),
      '\u0304':stroke(['M-115 105 L115 105'],t*.8),
      '\u0306':stroke(['M-110 170 C-100 40 100 40 110 170'],t*.8),
      '\u0307':dot(0,115,t*1.3),
      '\u0308':pathops.Path(),
      '\u030a':stroke(['M0 55 C-110 55 -110 205 0 205 C110 205 110 55 0 55 Z'],t*.65),
      '\u030b':stroke(['M-120 65 L-20 170','M15 65 L115 170'],t*.7),
      '\u030c':stroke(['M-110 170 L0 65 L110 170'],t*.8),
      '\u0327':stroke(['M10 -40 L-25 -100 C120 -100 100 -240 -35 -200'],t*.7),
      '\u0328':stroke(['M70 -30 C-60 -110 -35 -220 80 -180'],t*.7),
    }
    marks['\u0308'].addPath(dot(-90,115,t*1.1));marks['\u0308'].addPath(dot(90,115,t*1.1))
    for cp in range(0xC0,0x180):
        c=chr(cp);dec=unicodedata.normalize('NFD',c)
        if len(dec)==2 and dec[0] in paths and dec[1] in marks:
            base,mark=dec; source='ı' if base=='i' and mark not in '\u0326\u0327\u0328' else base
            p=pathops.Path();p.addPath(paths[source]); top=0 if mark in '\u0327\u0328' else (760 if base.isupper() or base in 'bdfhklt' else 560)
            if c in 'Ľľďť':
                # Compact side caron: newly drawn tapered shape, not an apostrophe.
                wedge=pathops.Path();parse_path('M0 0 L30 135 L80 135 L40 0 Z',wedge.getPen())
                p.addPath(transformed(wedge,widths[base]+5,580));widths[c]=widths[base]+115
            elif c in 'ĢģĶķĻļŅņŖŗ':
                comma=stroke(['M20 -85 L-15 -185'],t*.7)
                p.addPath(transformed(comma,widths[base]/2,0) if c!='ģ' else transformed(comma,widths[base]/2,760))
                widths[c]=widths[base]
            else:
                p.addPath(transformed(marks[mark],widths[base]/2,top-45 if c=='ţ' else top));widths[c]=widths[base]
            paths[c]=p
    # Distinct forms for common non-decomposing Latin letters.
    for c,base in [('Ø','O'),('ø','o')]:
        p=pathops.Path();p.addPath(paths[base]);p.addPath(stroke([f'M70 -35 L{widths[base]-70} {735 if base.isupper() else 535}'],t*.75));paths[c]=p;widths[c]=widths[base]
    for c,base in [('Ł','L'),('ł','l')]:
        p=pathops.Path();p.addPath(paths[base]);p.addPath(stroke([f'M40 270 L{widths[base]-35} 440'],t*.85));paths[c]=p;widths[c]=widths[base]
    for c,b1,b2,overlap in [('Æ','A','E',155),('æ','a','e',80),('Œ','O','E',125),('œ','o','e',80)]:
        p=pathops.Path();p.addPath(paths[b1]);p.addPath(transformed(paths[b2],widths[b1]-overlap));paths[c]=p;widths[c]=widths[b1]+widths[b2]-overlap
    paths['ß']=stroke(['M85 0 L85 475 C85 640 145 720 275 720 C390 720 435 665 435 575 C435 475 365 420 300 370 C445 335 495 265 495 165 C495 45 425 -10 275 15'],t);widths['ß']=580
    extend(paths,widths,marks,t,stroke,transformed,dot)
    for c,p in paths.items():
        g=write_glyph(f,name(ord(c)),widths[c],p,ord(c))
        if c.isalpha() or c=='◌':
            top=760 if c.isupper() or c in 'bdfhklt' else 560
            g.appendAnchor(dict(name='top',x=widths[c]/2,y=top))
            g.appendAnchor(dict(name='bottom',x=widths[c]/2,y=0))
    for c,p in marks.items():
        g=write_glyph(f,name(ord(c)),0,p,ord(c));g.appendAnchor(dict(name='_bottom' if c in '\u0326\u0327\u0328' else '_top',x=0,y=0))
    # Preserve true base + dedicated side-caron components, not flattened paths.
    wedge=pathops.Path();parse_path('M0 0 L30 135 L80 135 L40 0 Z',wedge.getPen())
    write_glyph(f,'caroncomb.alt',0,wedge)
    for c,base,x,y,advance in [('Ľ','L',170,555,515),('ľ','l',185,555,335),('ď','d',570,555,705),('ť','t',230,555,375)]:
        g=f[name(ord(c))];g.clearContours();g.components=[Component(name(ord(base))),Component('caroncomb.alt',(1,0,0,1,x,y))];g.width=advance
    ogonek=pathops.Path();ogonek.addPath(paths['ı']);ogonek.addPath(transformed(marks['\u0328'],widths['i']/2))
    g=write_glyph(f,'iogonek.dotless',widths['i'],ogonek)
    g.appendAnchor(dict(name='top',x=widths['i']/2,y=560));g.appendAnchor(dict(name='bottom',x=widths['i']/2,y=0))
    # GF Latin Core also requires unencoded localized forms.
    write_glyph(f,'periodcentered.loclCAT',180,dot(90,350,t))
    write_glyph(f,'periodcentered.loclCAT.case',220,dot(110,350,t))
    g=write_glyph(f,'idotaccent',widths['i'],paths['i'])
    g.appendAnchor(dict(name='top',x=widths['i']/2,y=560))
    g.appendAnchor(dict(name='bottom',x=widths['i']/2,y=0))
    write_glyph(f,'.notdef',600,stroke(['M80 0 L80 700 L520 700 L520 0 Z','M80 0 L520 700'],t*.6))
    # A slashed zero is opt-in; tabular figures never change letter spacing.
    p=pathops.Path();p.addPath(paths['0']);p.addPath(stroke(['M175 135 L435 565'],t*.7))
    write_glyph(f,'zero.slash',610,p)
    for c in '0123456789':write_glyph(f,name(ord(c))+'.tab',640,transformed(paths[c],(640-widths[c])/2))
    write_glyph(f,'zero.slash.tab',640,transformed(p,15))
    f.features.text='languagesystem DFLT dflt;\nlanguagesystem latn dflt;\nfeature zero { sub zero by zero.slash; sub zero.tab by zero.slash.tab; } zero;\nfeature tnum {\n'+''.join(f' sub {name(ord(c))} by {name(ord(c))}.tab;\n' for c in '0123456789')+' sub zero.slash by zero.slash.tab;\n} tnum;\n'
    f.features.text += """
feature locl {
 script latn;
 language CAT;
 sub l periodcentered' l by periodcentered.loclCAT;
 sub L periodcentered' L by periodcentered.loclCAT.case;
 language TRK; sub i by idotaccent;
 language AZE; sub i by idotaccent;
 language CRT; sub i by idotaccent;
 language KAZ; sub i by idotaccent;
 language TAT; sub i by idotaccent;
} locl;
"""
    above=[name(ord(c)) for c in marks if c not in '\u0326\u0327\u0328']
    f.features.text+='@SproutAbove = ['+' '.join(above)+'];\nfeature ccmp { lookup SproutSoftDots { lookupflag UseMarkFilteringSet @SproutAbove; sub i\' @SproutAbove by dotlessi; sub j\' @SproutAbove by uni0237; sub iogonek\' @SproutAbove by iogonek.dotless; } SproutSoftDots; } ccmp;\n'
    for a,b,v in [('A','V',-38),('A','W',-25),('A','Y',-38),('T','a',-35),('T','o',-35),('T','e',-35),('V','a',-25),('W','a',-18),('Y','o',-40),('Y','a',-40),('L','T',-25),('L','Y',-25),('F','o',-15),('P','a',-18),('r','.',-20)]:f.kerning[(name(ord(a)),name(ord(b)))]=v
    f.glyphOrder=['.notdef']+sorted(n for n in f.keys() if n!='.notdef')
    # Resolve sub-unit rasterization noise at the intended horizontal alignments.
    for g in f:
        for contour in g:
            # Remove redundant on-curve points on straight segments.
            changed=True
            while changed and len(contour.points)>3:
                changed=False
                for idx,p in enumerate(contour.points):
                    prev=contour.points[idx-1];nxt=contour.points[(idx+1)%len(contour.points)]
                    if p.type=='line' and nxt.type=='line' and prev.type is not None:
                        cross=(p.x-prev.x)*(nxt.y-p.y)-(p.y-prev.y)*(nxt.x-p.x)
                        if abs(cross)<0.01:
                            del contour.points[idx];changed=True;break
            for point in contour:
                if point.type is not None:
                    for y in [0,i.capHeight,i.xHeight]:
                        if abs(point.y-y)<=1:point.y=y
    f.save(ROOT/'sources'/f'NevlinSprout-{style}.ufo',overwrite=True)
    out=ROOT/'fonts'/'ttf';out.mkdir(parents=True,exist_ok=True)
    web=ROOT/'fonts'/'webfonts';web.mkdir(parents=True,exist_ok=True)
    target=out/f'NevlinSprout-{style}.ttf'
    FontProject().run_from_ufos([str(ROOT/'sources'/f'NevlinSprout-{style}.ufo')],output=('ttf',),output_path=str(target),use_production_names=False,remove_overlaps=False)
    font=TTFont(target)
    # Make implied quadratic on-curves explicit, then align only on-curves
    # within 3/1000 em of a declared line. Control handles stay unchanged.
    alignment_log={}
    for glyph_name in font.getGlyphOrder():
        glyph=font['glyf'][glyph_name]
        if glyph.isComposite() or not hasattr(glyph,'coordinates'):continue
        coords=[];flags=[];ends=[];start=0;changes=[]
        for end in glyph.endPtsOfContours:
            for idx in range(start,end+1):
                pt=glyph.coordinates[idx];flag=glyph.flags[idx]
                coords.append(pt);flags.append(flag)
                nxt=start if idx==end else idx+1
                if not flag&1 and not glyph.flags[nxt]&1:
                    other=glyph.coordinates[nxt]
                    coords.append(((pt[0]+other[0])/2,(pt[1]+other[1])/2));flags.append(1)
            ends.append(len(coords)-1);start=end+1
        for idx,(x,y) in enumerate(coords):
            if flags[idx]&1:
                for target_y in (0,i.capHeight,i.xHeight):
                    if 0<abs(y-target_y)<=3:
                        coords[idx]=(x,target_y);changes.append([idx,y,target_y]);break
        glyph.coordinates=GlyphCoordinates(coords);glyph.flags=array('B',flags);glyph.endPtsOfContours=ends
        if changes:alignment_log[glyph_name]=changes
    qa=ROOT/'qa';qa.mkdir(exist_ok=True)
    (qa/f'alignment-{style}.json').write_text(json.dumps(alignment_log,indent=2))
    buildStatTable(font,[dict(tag='wght',name='Weight',values=[dict(value=weight,name=style,flags=2 if weight==400 else 0)]),dict(tag='ital',name='Italic',values=[dict(value=0,name='Roman',linkedValue=1,flags=2)])])
    font['name'].names=[n for n in font['name'].names if n.platformID!=1]
    font['gasp']=newTable('gasp');font['gasp'].gaspRange={65535:15}
    font['meta']=newTable('meta');font['meta'].data={'dlng':'Latn','slng':'Latn'}
    font['head'].created=font['head'].modified=3875040000
    font.recalcTimestamp=False
    font.save(out/f'NevlinSprout-{style}.ttf');font.flavor='woff2';font.save(web/f'NevlinSprout-{style}.woff2')
    gs=font.getGlyphSet()
    svgdir=ROOT/'glyphs'/style;svgdir.mkdir(parents=True,exist_ok=True)
    for c in paths:
        pen=SVGPathPen(gs);gs[name(ord(c))].draw(pen)
        (svgdir/f'U+{ord(c):04X}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {max(f[name(ord(c))].width,350)} 1400"><title>U+{ord(c):04X} {unicodedata.name(c,"SPACE")} — {style}</title><path transform="translate(0 1050) scale(1 -1)" d="{pen.getCommands()}"/></svg>')
    for g in f:
        if g.unicodes and chr(g.unicodes[0]) in paths:continue
        pen=SVGPathPen(gs);gs[g.name].draw(pen);w=max(g.width,350)
        filename=f'U+{g.unicodes[0]:04X}' if g.unicodes else f'glyph-{g.name}'
        (svgdir/f'{filename}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 1400"><title>{g.name} — {style}</title><path transform="translate({175 if g.width==0 else 0} 1050) scale(1 -1)" d="{pen.getCommands()}"/></svg>')
    return dict(style=style,weight=weight,encoded=len(font.getBestCmap()),glyphs=len(f),sha256=hashlib.sha256((out/f'NevlinSprout-{style}.ttf').read_bytes()).hexdigest())

if __name__=='__main__':
    reports=[build(*args) for args in WEIGHTS]
    (ROOT/'build-manifest.json').write_text(json.dumps(reports,indent=2)+'\n')
    print(json.dumps(reports,indent=2))

"""Local design studies, not release fonts. No external font outlines imported.
Unchanged characters originate in the project's earlier Sprout drawings.
Run with ../../nevlin-google-fonts/.venv/bin/python sources/build.py.
"""
from pathlib import Path
import json, math
import pathops
from fontTools.svgLib.path import parse_path
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.fontBuilder import FontBuilder
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from ufoLib2 import Font
from previous_drawings import GLYPHS

ROOT=Path(__file__).resolve().parents[1]
D=dict(GLYPHS)
REDRAWN=set()
def put(c,w,*p):
    D[c]=(w,p);REDRAWN.add(c)
# A shared new skeleton: continuous oval curves, asymmetric shoulders,
# larger apertures and less rigid spacing than the previous rounded boxes.
oval='M282 -8 C158 -8 80 88 80 250 C80 411 158 508 282 508 C409 508 486 411 486 250 C486 88 409 -8 282 -8 Z'
put('o',566,oval)
put('c',515,'M453 422 C414 478 359 508 286 508 C157 508 80 405 80 250 C80 93 157 -8 286 -8 C360 -8 416 23 457 82')
put('e',540,'M82 260 L465 260 C472 409 410 508 282 508 C154 508 80 405 80 250 C80 91 162 -8 295 -8 C366 -8 422 17 466 63')
put('a',543,'M104 425 C146 480 207 508 281 508 C398 508 459 449 459 335 L459 0','M459 280 C389 298 327 302 269 287 C151 262 79 216 79 132 C79 43 143 -8 238 -8 C341 -8 416 48 459 122')
put('n',563,'M84 500 L84 0','M84 360 C130 457 207 508 296 508 C412 508 479 437 479 312 L479 0')
put('h',563,'M84 720 L84 0',D['n'][1][1])
put('m',828,'M84 500 L84 0','M84 360 C123 460 187 508 263 508 C370 508 414 430 414 313 L414 0','M414 355 C456 458 523 508 600 508 C703 508 744 430 744 313 L744 0')
put('u',563,'M84 500 L84 190 C84 60 148 -8 260 -8 C350 -8 429 47 479 141','M479 500 L479 0')
put('b',570,'M84 720 L84 0','M84 374 C132 465 201 508 283 508 C412 508 486 407 486 250 C486 93 412 -8 283 -8 C199 -8 128 36 84 120')
put('p',570,'M84 500 L84 -210',D['b'][1][1])
put('d',570,'M486 720 L486 0','M486 374 C438 465 369 508 287 508 C158 508 84 407 84 250 C84 93 158 -8 287 -8 C371 -8 442 36 486 120')
put('q',570,'M486 500 L486 -210',D['d'][1][1])
put('g',570,'M486 500 L486 -49 C486 -166 417 -218 295 -218 C215 -218 150 -193 104 -154',D['d'][1][1])
put('r',352,'M84 500 L84 0','M84 341 C130 463 202 517 308 489')
put('s',475,'M407 433 C368 482 310 508 240 508 C140 508 78 458 78 383 C78 304 145 277 245 248 C341 219 398 187 398 111 C398 38 334 -8 236 -8 C158 -8 95 23 58 79')
put('t',350,'M142 660 L142 128 C142 29 188 -7 300 25','M43 478 L307 478')
put('f',343,'M139 0 L139 553 C139 677 195 733 311 707','M44 478 L302 478')
put('l',260,'M99 720 L99 108 C99 31 131 0 209 16')
put('v',496,'M62 500 L248 0 L434 500')
put('w',736,'M62 500 L204 0 L368 415 L532 0 L674 500')
put('x',496,'M66 500 L430 0','M430 500 L66 0')
put('y',500,'M62 500 L252 0','M438 500 L235 -60 C194 -170 143 -226 63 -200')
put('z',470,'M64 500 L405 500 L64 0 L405 0')
put('O',666,'M333 -10 C176 -10 84 124 84 350 C84 576 176 710 333 710 C490 710 582 576 582 350 C582 124 490 -10 333 -10 Z')
put('Q',666,*D['O'][1],'M394 130 Q480 34 596 -80')
put('C',631,'M554 609 C506 675 431 710 336 710 C177 710 84 571 84 350 C84 129 177 -10 336 -10 C431 -10 507 25 559 96')
# One connected contour path: the previous C plus two detached bars left
# a notch at the bowl and a stepped external corner at the crossbar.
put('G',672,'M554 609 C506 675 431 710 336 710 C177 710 84 571 84 350 C84 129 177 -10 336 -10 C431 -10 512 28 568 95 L568 330 L374 330')
# Close the outside skeleton instead of ending its bottom bar on a butt-capped
# stem. The old B had the same half-stroke step as G at the lower left.
put('B',620,'M85 0 L85 700 L310 700 C455 700 515 637 515 530 C515 430 458 365 310 365 C468 365 550 303 550 185 C550 65 478 0 310 0 Z','M85 365 L310 365')
put('0',584,'M292 -10 C159 -10 84 120 84 350 C84 580 159 710 292 710 C425 710 500 580 500 350 C500 120 425 -10 292 -10 Z')
put('1',409,'M67 552 L216 700 L216 0','M100 0 L333 0')
put('2',551,'M80 555 C92 657 163 710 280 710 C397 710 467 642 467 540 C467 437 383 354 285 261 L79 61 L79 0 L480 0')
put('4',584,'M375 700 L75 228 L515 228','M417 526 L417 0')
put('7',524,'M64 700 L460 700 L199 0')
put('€',631,*D['C'][1],'M42 419 L411 419','M42 275 L386 275')

def path(ds,t,contrast):
    # Expand in scaled coordinates to make horizontal strokes optically lighter.
    out=pathops.Path()
    for s in ds:
        p=pathops.Path();parse_path(s,TransformPen(p.getPen(),(1,0,0,1/contrast,0,0)))
        p.stroke(t,pathops.LineCap.BUTT_CAP,pathops.LineJoin.ROUND_JOIN,4)
        p.convertConicsToQuads(.15)
        p.draw(TransformPen(out.getPen(),(1,0,0,contrast,0,0)))
    return out
def circle(x,y,r):
    p=pathops.Path(); k=r*.55228475
    parse_path(f'M{x+r} {y} C{x+r} {y+k} {x+k} {y+r} {x} {y+r} C{x-k} {y+r} {x-r} {y+k} {x-r} {y} C{x-r} {y-k} {x-k} {y-r} {x} {y-r} C{x+k} {y-r} {x+r} {y-k} {x+r} {y} Z',p.getPen());return p

def build(label,compact):
    dest=ROOT/label;dest.mkdir(exist_ok=True)
    f=Font();f.info.familyName='Study '+label;f.info.styleName='Regular';f.info.unitsPerEm=1000
    f.info.ascender=820;f.info.descender=-250;f.info.xHeight=530;f.info.capHeight=730
    shapes=dict(D)
    if compact:
        # A separate single-storey a, straighter l, flatter e and tight proportions.
        shapes['a']=(570,('M486 500 L486 0',D['d'][1][1]))
        shapes['l']=(230,('M115 720 L115 0',))
        shapes['t']=(340,('M145 665 L145 120 Q145 0 290 20','M45 475 L300 475'))
    if label=='B2':
        # Revised UI direction; wider counters and differentiated a / l / 1.
        shapes['a']=(560,('M105 421 C145 479 208 508 293 508 C407 508 470 447 470 334 L470 0','M470 272 C417 290 344 297 278 283 C158 263 84 217 84 131 C84 45 145 -8 242 -8 C348 -8 425 45 470 121'))
        shapes['e']=(565,('M84 256 L481 256 C481 414 405 508 287 508 C157 508 80 406 80 250 C80 91 164 -8 302 -8 C376 -8 438 22 481 72',))
        shapes['o']=(590,('M295 -8 C163 -8 80 93 80 250 C80 407 163 508 295 508 C427 508 510 407 510 250 C510 93 427 -8 295 -8 Z',))
        shapes['n']=(580,('M88 500 L88 0','M88 354 C132 455 209 508 304 508 C427 508 492 431 492 306 L492 0'))
        shapes['h']=(580,('M88 720 L88 0',shapes['n'][1][1]))
        shapes['m']=(854,('M88 500 L88 0','M88 354 C128 454 195 508 274 508 C379 508 427 435 427 310 L427 0','M427 354 C467 454 534 508 613 508 C718 508 766 435 766 310 L766 0'))
        shapes['r']=(367,('M88 500 L88 0','M88 343 C132 457 213 517 324 485'))
        shapes['l']=(275,('M108 720 L108 112 C108 36 141 0 224 16',))
        shapes['t']=(362,('M144 650 L144 130 C144 31 190 -5 310 27','M45 475 L315 475'))
        shapes['M']=(760,('M88 0 L88 700 L380 290 L672 700 L672 0',))
        shapes['1']=(410,('M85 548 L240 700 L240 0',))
    dots={'i':[(115,665)],'j':[(140,665)],'.':[(115,10)],':':[(115,10),(115,370)],';':[(115,370)],'!':[(115,10)],'?':[(225,10)]}
    sx=.91 if compact else 1; thickness=78 if compact else 74; contrast=.94 if compact else .83
    if label=='B2':sx=1;thickness=86;contrast=.88
    cmap={}; order=['.notdef']; glyf={}; metrics={}; svgs={}
    glyph=f.newGlyph('.notdef');glyph.width=600
    path(['M80 0 L80 700 L520 700 L520 0 Z'],40,1).draw(glyph.getPen())
    chars=[chr(i) for i in range(32,127)]+list('€£¥₸–—')
    for c in chars:
        w,ds=shapes[c];p=path(ds,thickness,contrast)
        for x,y in dots.get(c,[]):p.addPath(circle(x,y,thickness*.59))
        n=f'uni{ord(c):04X}';order.append(n);cmap[ord(c)]=n
        g=f.newGlyph(n);g.unicodes=[ord(c)];g.width=round(w*sx)
        if list(p):pathops.simplify(p,clockwise=False).draw(TransformPen(g.getPen(),(sx,0,0,1,0,0)))
    # Consistent tabular alternates for financial figures.
    for c in '0123456789':
        base=f[cmap[ord(c)]];g=f.newGlyph(cmap[ord(c)]+'.tab');g.width=round(610*sx)
        base.draw(TransformPen(g.getPen(),(1,0,0,1,(g.width-base.width)/2,0)));order.append(g.name)
    f.features.text='feature tnum {\n'+''.join(f'sub {cmap[ord(c)]} by {cmap[ord(c)]}.tab;\n' for c in '0123456789')+'} tnum;\n'
    pairs=[('A','V',-30),('A','W',-20),('T','o',-28),('T','a',-24),('Y','o',-32),('V','a',-22),('L','T',-24)]
    f.features.text+='feature kern {\n'+''.join(f'pos {cmap[ord(a)]} {cmap[ord(b)]} {v};\n' for a,b,v in pairs)+'} kern;'
    f.glyphOrder=order;f.save(dest/f'{label}.ufo',overwrite=True)
    for n in order:
        g=f[n];pen=TTGlyphPen(None);g.draw(Cu2QuPen(pen,1,reverse_direction=True));glyf[n]=pen.glyph();metrics[n]=(int(g.width),round(g.getBounds(f)[0]) if len(g) else 0)
        sp=SVGPathPen(f);g.draw(sp);svgs[n]=sp.getCommands()
        (dest/'svg').mkdir(exist_ok=True)
        (dest/'svg'/f'{n}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -1000 {g.width or 600} 1300"><g transform="scale(1,-1)"><path d="{sp.getCommands()}"/></g></svg>')
    fb=FontBuilder(1000,isTTF=True);fb.setupGlyphOrder(order);fb.setupCharacterMap(cmap);fb.setupGlyf(glyf);fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=850,descent=-270)
    fb.setupNameTable({'familyName':'Study '+label,'styleName':'Regular','uniqueFontIdentifier':'LocalStudy-'+label+'-0.001','fullName':'Study '+label+' Regular','psName':'Study'+label+'-Regular','version':'Version 0.001'})
    fb.setupOS2(sTypoAscender=850,sTypoDescender=-270,usWinAscent=1000,usWinDescent=300,sxHeight=530,sCapHeight=730);fb.setupPost();addOpenTypeFeaturesFromString(fb.font,f.features.text);fb.save(dest/f'{label}.ttf');fb.font.flavor='woff2';fb.save(dest/f'{label}.woff2')
    return {'label':label,'encoded_characters':len(cmap),'glyphs':len(order),'new_drawings':sorted(REDRAWN)}

if __name__=='__main__':
    print(json.dumps([build('A',False),build('B',True),build('B2',True)]))

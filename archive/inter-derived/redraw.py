"""Independent outline drawings for eight Nevlin characters.

Coordinates below define new silhouettes and counters; they do not manipulate
or trace Inter contour points. Inter metrics provide alignment/spacing only.
Cubic drawings are converted to quadratic TrueType curves to <1 font-unit error.
"""
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path
from fontTools.ttLib.tables.ttProgram import Program


def drawings(weight):
    # Stem increments across regular/medium/semibold; outer skeleton stays fixed.
    t={400:156,500:184,600:214,700:242}[weight]+10
    return {
    # A compact double-storey a with a diagonal top terminal and full lower bowl.
    'a':f'''M 115 805 C 190 970 350 1020 540 1020
        C 805 1020 920 875 920 650 L 920 0 L {920-t} 0 L {920-t} 145
        C 630 20 505 -20 350 -20 C 115 -20 30 125 30 295
        C 30 520 220 595 490 615 L {920-t} 630 L {920-t} 675
        C {920-t} 810 655 {1020-t} 525 {1020-t}
        C 380 {1020-t} 295 800 260 740 Z
        M {920-t} 475 L 505 460 C {30+t} 445 {30+t} 370 {30+t} 295
        C {30+t} 190 285 {t-20} 390 {t-20}
        C 565 {t-20} {920-t} 270 {920-t} 430 Z''',
    # Open e, with a very subtly rising crossbar.
    'e':f'''M 960 495 L {30+t} 485
        C {30+t+10} 260 335 {t-20} 520 {t-20}
        C 655 {t-20} 750 215 805 310 L 960 250
        C 875 65 725 -20 520 -20 C 205 -20 30 180 30 500
        C 30 815 215 1020 515 1020 C 820 1020 960 825 960 550 Z
        M {30+t+10} {485+t-12} L {960-t} {495+t-12}
        C {940-t} 800 665 {1020-t} 515 {1020-t}
        C 355 {1020-t} {30+t+35} 785 {30+t+10} {485+t-12} Z''',
    # Single-storey g with an open, upward-curving descender and a generous bowl.
    'g':f'''M {980-t} 1000 L 980 1000 L 980 -40
        C 980 -310 790 -410 530 -410 C 300 -410 140 -320 85 -175
        L {85+t*.86} {-175+t*.38}
        C 340 {-410+t} 420 {-410+t} 535 {-410+t}
        C 710 {-410+t} {980-t} -150 {980-t} -25 L {980-t} 140
        C 675 25 540 -20 405 -20 C 145 -20 30 190 30 500
        C 30 810 170 1020 435 1020 C 600 1020 720 950 {980-t} 825 Z
        M {980-t} 510 C {980-t} 740 670 {1020-t} 490 {1020-t}
        C 295 {1020-t} {30+t} 710 {30+t} 500
        C {30+t} 285 305 {t-20} 490 {t-20}
        C 680 {t-20} {980-t} 300 {980-t} 510 Z''',
    # r with a fuller curved shoulder, low join, and diagonal shoulder terminal.
    'r':f'''M 65 0 L 65 1000 L {65+t} 1000 L {65+t} 795
        C 310 965 450 1040 650 1005 L 610 {1005-t}
        C 410 920 {65+t} 735 {65+t} 525 L {65+t} 0 Z''',
    # t with an angled top and a more open, rising foot; bar is asymmetrical.
    't':f'''M 210 1000 L 210 1300 L {210+t} 1320 L {210+t} 1000
        L 680 1000 L 680 {1000-t} L {210+t} {1000-t}
        L {210+t} 280 C {210+t} 130 490 120 650 190
        L 700 35 C 440 -100 210 -15 210 270 L 210 {1000-t}
        L 20 {1000-t} L 20 1000 Z''',
    # One keeps its angled flag and gains a short foot for distinction from l.
    'one':f'''M 50 1150 L 395 1450 L {395+t} 1450 L {395+t} {t}
        L {395+t+70} {t*.55} L {395+t+70} 0 L 325 0 L 325 {t*.55} L 395 {t*.55}
        L 395 {1450-t-75} L 165 1020 Z''',
    # Four has a fully open top and a broad, low crossbar.
    'four':f'''M 640 1450 L {640+t*1.15} 1450 L 235 445 L 1120 445
        L 1120 {445-t} L 25 {445-t} L 25 445 Z
        M 790 1040 L {790+t} 1040 L {790+t} 0 L 790 0 Z''',
    # Uncrossed seven with a clean, compact diagonal.
    'seven':f'''M 60 1450 L 1080 1450 L 1080 {1450-t}
        L {245+t*1.15} 0 L 245 0 L {1080-t*1.15} {1450-t} L 60 {1450-t} Z
'''
    }


def redraw_glyphs(font,weight):
    glyf=font['glyf'];source=drawings(weight);changed=[]
    for base,path in source.items():
        bp=BoundsPen(None);parse_path(path,bp);x0,y0,x1,y1=bp.bounds
        # Keep normal OpenType financial and superscript variants visually coherent.
        targets=[base]
        if base in ['one','four','seven']:
            for n in font.getGlyphOrder():
                if n.startswith(base+'.') and not any(k in n for k in ['circled','squared','dotleader']):targets.append(n)
        else:
            targets += [n for n in [base+'.sups',base+'.subs'] if n in glyf]
        for n in targets:
            old=glyf[n];old.recalcBounds(glyf)
            if n==base:
                # Retain original bearings and width; define the new baseline/extents.
                left,right=old.xMin,old.xMax
                if base in ['a','e','r']:sy=font['OS/2'].sxHeight/1000;dy=0
                elif base=='g':sy=font['OS/2'].sxHeight/1020;dy=0
                elif base=='t':sy=old.yMax/1320;dy=0
                else:sy=font['OS/2'].sCapHeight/1450;dy=0
                sx=(right-left)/(x1-x0);dx=left-x0*sx
            else:
                sx=(old.xMax-old.xMin)/(x1-x0);sy=(old.yMax-old.yMin)/(y1-y0)
                dx=old.xMin-x0*sx;dy=old.yMin-y0*sy
            pen=TTGlyphPen(None)
            transformed=TransformPen(Cu2QuPen(pen,max_err=.7,reverse_direction=False),(sx,0,0,sy,dx,dy))
            parse_path(path,transformed)
            glyf[n]=pen.glyph();glyf[n].recalcBounds(glyf)
            # Overlapping bars (4/7) use nonzero filling; flag explicitly for renderers.
            if len(glyf[n].flags):glyf[n].flags[0] |= 0x40
            advance,_=font['hmtx'][n];font['hmtx'][n]=(advance,glyf[n].xMin)
            changed.append(n)
    return changed

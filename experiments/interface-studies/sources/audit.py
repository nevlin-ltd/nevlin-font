"""Structural and visual proofs for the limited local studies, not release QA."""
from pathlib import Path
import json, math
from fontTools.ttLib import TTFont
from fontTools.pens.areaPen import AreaPen
from PIL import Image, ImageDraw, ImageFont
from ufoLib2 import Font

ROOT=Path(__file__).resolve().parents[1]
reports={}
for label in ['A','B','B2']:
    font=TTFont(ROOT/label/f'{label}.ttf')
    web=TTFont(ROOT/label/f'{label}.woff2')
    source=Font.open(ROOT/label/f'{label}.ufo')
    issues=[]
    for name in font.getGlyphOrder():
        g=font['glyf'][name]
        if not g.numberOfContours:continue
        if g.xMin<0 or g.xMax>font['hmtx'][name][0]:issues.append([name,'horizontal overhang'])
        if g.yMin < -300 or g.yMax > 1000:issues.append([name,'export frame overflow'])
        for contour in source[name].contours:
            pen=AreaPen(None);contour.draw(pen)
            if abs(pen.value)<4:issues.append([name,'tiny contour'])
            if contour.points and contour.points[0].type == 'move':issues.append([name,'open contour'])
            assert all(math.isfinite(p.x) and math.isfinite(p.y) for p in contour.points)
    assert font.getBestCmap()==web.getBestCmap()
    assert font['glyf']['uni0047'].numberOfContours==1
    assert font['glyf']['uni0042'].numberOfContours==3
    assert len(set(font['hmtx'][f'uni{ord(c):04X}.tab'][0] for c in '0123456789'))==1
    reports[label]={'glyphs_checked':len(font.getGlyphOrder()),'encoded_characters':len(font.getBestCmap()),'issues':issues,'ttf_woff2_cmap_match':True,'G_continuous':True,'B_outer_and_two_counters':True,'tabular_widths_equal':True}
    assert not issues,issues

font=TTFont(ROOT/'B2/B2.ttf');chars=list(font.getBestCmap())
im=Image.new('RGB',(1600,1760),'white');d=ImageDraw.Draw(im)
face=ImageFont.truetype(str(ROOT/'B2/B2.ttf'),100)
for i,cp in enumerate(chars):
    x=i%10*160;y=i//10*160
    d.text((x+12,y+2),f'U+{cp:04X}',fill='gray')
    d.text((x+16,y+20),chr(cp),font=face,fill='#241744')
im.save(ROOT/'qa/atlas-after.png')
im=Image.new('RGB',(1600,1100),'white');d=ImageDraw.Draw(im)
for x,filename in [(25,ROOT/'qa/B2-before-audit.ttf'),(825,ROOT/'B2/B2.ttf')]:
    d.text((x,12),'BEFORE AUDIT' if x==25 else 'AFTER AUDIT',fill='gray')
    for y,size,text in [(40,250,'BG'),(340,60,'HAMBURGEFONTS'),(440,48,'minimum rhythm  rn m'),(530,40,'Il1 O0  $12,480.50  € £ ¥ ₸'),(630,12,'Build a steady saving habit. Your next goal is closer than you think.'),(690,14,'Build a steady saving habit. Your next goal is closer than you think.'),(750,16,'Build a steady saving habit. Your next goal is closer than you think.'),(820,20,'AVATAR  To  Wa  Yo  Plan today. Grow tomorrow.')]:
        d.text((x,y),text,font=ImageFont.truetype(str(filename),size),fill='#241744')
im.save(ROOT/'qa/audit-proof.png')
reports['scope']='101 encoded characters per study; no complete Latin Core, hinting, language or cross-platform certification. Visual review remains necessary.'
(ROOT/'qa/audit.json').write_text(json.dumps(reports,indent=2))
print(json.dumps(reports))

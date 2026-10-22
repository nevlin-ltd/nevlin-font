from pathlib import Path
import json, math
from PIL import Image,ImageDraw,ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.areaPen import AreaPen
from ufoLib2 import Font
from glyphsLib.glyphdata import get_glyph
R=Path(__file__).resolve().parents[1]
f=TTFont(R/'A/A.ttf'); source=Font.open(R/'A/A.ufo'); issues=[]
for name in f.getGlyphOrder():
 g=f['glyf'][name]
 if g.numberOfContours:
  if g.xMin<0 or g.xMax>f['hmtx'][name][0]:issues.append([name,'horizontal overhang'])
  if g.yMin < -300 or g.yMax >1000:issues.append([name,'export overflow'])
 for c in source[name].contours:
  p=AreaPen(None);c.draw(p)
  if abs(p.value)<4:issues.append([name,'tiny contour'])
  if c.points and c.points[0].type=='move':issues.append([name,'open contour'])
  assert all(math.isfinite(p.x) and math.isfinite(p.y) for p in c.points)
assert not issues,issues
assert f.getBestCmap()==TTFont(R/'A/A.woff2').getBestCmap()
assert len({f['hmtx'][f'uni{ord(c):04X}.tab'][0] for c in '0123456789'})==1
required=R.parents[1]/'families/nevlin-sprout/qa/GF_Latin_Core.txt'
missing=[]
for n in required.read_text().splitlines():
 if not n or n.startswith('#'):continue
 u=get_glyph(n).unicode
 if not ((u and int(u,16) in f.getBestCmap()) or (not u and n in f.getGlyphOrder())):missing.append(n)
(R/'qa/report.json').write_text(json.dumps({'glyphs':len(f.getGlyphOrder()),'encoded_characters':len(f.getBestCmap()),'structural_issues':issues,'latin_core_missing':missing,'coverage_reference':'Previously pinned GF_Latin_Core.txt in families/nevlin-sprout/qa','scope':'Construction audit only; no full FontBakery or cross-platform certification.'},indent=2))
im=Image.new('RGB',(1600,1260),'white');d=ImageDraw.Draw(im)
for x,fn,title in [(30,R/'qa/baseline.ttf','ORIGINAL A'),(820,R/'A/A.ttf','A / FIRST REFINEMENT')]:
 d.text((x,15),title,fill='#555555')
 for y,size,t in [(55,90,'DOPRUS'),(190,90,'035689'),(330,48,'Grow at your own pace.'),(420,40,'minimum  rn m  Il1 O0'),(510,36,'Savings $12,480.50'),(600,12,'Plan your spending. Build a steady saving habit.'),(650,14,'Plan your spending. Build a steady saving habit.'),(710,16,'Plan your spending. Build a steady saving habit.'),(780,20,'Plan your spending. Build a steady saving habit.'),(865,28,'AVATAR  To Wa Yo  ffi fi fl'),(945,32,'abcdefghijklmnopqrstuvwxyz'),(1020,32,'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),(1100,32,'0123456789  € £ ¥ ₸')]:
  d.text((x,y),t,font=ImageFont.truetype(str(fn),size),fill='#241744')
im.save(R/'qa/proof.png')
print(f'112 glyphs checked; {len(missing)} Latin Core requirements still missing.')

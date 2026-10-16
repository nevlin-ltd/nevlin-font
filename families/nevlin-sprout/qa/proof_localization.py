from pathlib import Path
import uharfbuzz as hb
import resvg_py
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
ROOT=Path(__file__).resolve().parents[1]
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1000"><rect width="1400" height="1000" fill="white"/>']
for row,style in enumerate(['Regular','Medium','SemiBold','Bold']):
 file=ROOT/'fonts'/'ttf'/f'NevlinSprout-{style}.ttf';tt=TTFont(file);gs=tt.getGlyphSet();font=hb.Font(hb.Face(file.read_bytes()))
 for line,(text,lang) in enumerate([(style,'en'),('col·legi  paral·lel  L·L  l·l','ca'),('İ i  I ı    Ľ ľ ď ť    café Ångström','tr')]):
  b=hb.Buffer();b.add_str(text);b.guess_segment_properties();b.language=lang;hb.shape(font,b)
  x=40;y=65+row*240+line*65;scale=.046
  for g,p in zip(b.glyph_infos,b.glyph_positions):
   pen=SVGPathPen(gs);gs[tt.getGlyphName(g.codepoint)].draw(pen)
   svg.append(f'<path fill="#20164c" transform="translate({x+p.x_offset*scale} {y-p.y_offset*scale}) scale({scale} {-scale})" d="{pen.getCommands()}"/>');x+=p.x_advance*scale
svg.append('</svg>');out='\n'.join(svg)
(ROOT/'qa/latin-core-localization.svg').write_text(out)
(ROOT/'qa/latin-core-localization.png').write_bytes(resvg_py.svg_to_bytes(svg_string=out))

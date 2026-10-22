"""Exercise cmap, mark attachment, localized forms and figure features."""
from pathlib import Path
import json,unicodedata
import uharfbuzz as hb
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1];reports=[]
for file in sorted((R/'fonts/ttf').glob('*.ttf')):
 t=TTFont(file);f=hb.Font(hb.Face(file.read_bytes()))
 def shape(text,features=None,lang='en'):
  b=hb.Buffer();b.add_str(text);b.guess_segment_properties();b.language=lang;hb.shape(f,b,features or {})
  assert all(g.codepoint for g in b.glyph_infos),(file.name,text,'missing glyph')
  return [(t.getGlyphName(g.codepoint),p.x_advance,p.x_offset,p.y_offset) for g,p in zip(b.glyph_infos,b.glyph_positions)]
 def advance(text,features=None):return sum(g[1] for g in shape(text,features))
 for text in ['Příliš žluťoučký kůň','Zażółć gęślą jaźń','Crème brûlée','Ångström','Straße','İstanbul','Ľ ľ ď ť','Ǥ ǥ Œ œ Æ æ','a\u0301 e\u0308 o\u0302 i\u0301 j\u0302']:
  shape(text)
  assert advance(text)==advance(unicodedata.normalize('NFD',text)),(file.name,text,'canonical advance mismatch')
 assert len({advance(c,{'tnum':True}) for c in '0123456789'})==1
 assert shape('0',{'zero':True})[0][0]=='zero.slash'
 assert shape('0',{'zero':True,'tnum':True})[0][0]=='zero.slash.tab'
 assert any(g[0]=='periodcentered.loclCAT' for g in shape('l·l',lang='ca'))
 assert advance('To')<advance('To',{'kern':False})
 assert advance('Tó')==advance('To'),(file.name,'accent kern mismatch')
 stacked=shape('x\u0301\u0308');assert len(stacked)==3 and stacked[1][3]>0 and stacked[2][3]>stacked[1][3],stacked
 assert t.getBestCmap()==TTFont(R/'fonts/webfonts'/file.with_suffix('.woff2').name).getBestCmap()
 reports.append({'font':file.name,'status':'pass','checks':['no missing sample glyphs','canonical-equivalent advances','equal tabular advances','slashed zero','Catalan locl','accented kerning','stacked mark attachment','TTF/WOFF2 cmap match']})
(R/'qa/shaping.json').write_text(json.dumps(reports,indent=2)+'\n');print('All four weights pass shaping checks.')

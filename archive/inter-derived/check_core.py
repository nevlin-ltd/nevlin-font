"""Check required coverage, numeric alignment and dot-removal behavior."""
from pathlib import Path
import json
import uharfbuzz as hb
from fontTools.ttLib import TTFont
ROOT=Path(__file__).resolve().parent
required=set(json.loads((ROOT/'repertoire.json').read_text()))
results=[]
for path in sorted((ROOT/'fonts/ttf').glob('*.ttf')):
    tt=TTFont(path);font=hb.Font(hb.Face(path.read_bytes()));names=tt.getGlyphOrder()
    assert required <= set(tt.getBestCmap())
    def shape(text,features=None):
        buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(font,buf,features or {})
        return [names[g.codepoint] for g in buf.glyph_infos],[p.x_advance for p in buf.glyph_positions]
    for text in ['i\u030b','j\u030b','i\u0326\u0303','į\u030b']:
        assert shape(text)[0][0] in ('dotlessi','uni0237','iogonek.dotless','itilde'),(path,text,shape(text))
    widths=shape('0123456789',{'tnum':True})[1]
    assert len(set(widths))==1,(path,widths)
    for text in ['Make your money make sense.','$12,480.50 € £ ¥ ₸']:
        assert '.notdef' not in shape(text)[0]
    results.append({'font':path.name,'codepoints':len(tt.getBestCmap()),'coverage':True,'dot_removal':True,'tabular_digits':True})
(ROOT/'qa/core-checks.json').write_text(json.dumps(results,indent=2))
print('All four weights pass coverage, dot-removal, tabular digit and specimen checks.')

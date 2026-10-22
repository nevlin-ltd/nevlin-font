"""Check encoded and unencoded requirements against the pinned official list."""
from pathlib import Path
import json, hashlib
from fontTools.ttLib import TTFont
from glyphsLib.glyphdata import get_glyph
ROOT=Path(__file__).resolve().parent
source=ROOT/'GF_Latin_Core.txt'
names=[n for n in source.read_text().splitlines() if n and not n.startswith('#')]
report={'source':'https://github.com/googlefonts/glyphsets/blob/0ac0e515473e39247683ed473fd74728671e2364/data/results/txt/nice-names/GF_Latin_Core.txt','list_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'required_glyphs':len(names),'fonts':[]}
files=sorted((ROOT/'fonts'/'ttf').glob('*.ttf'))
assert len(files)==4, 'Expected all four TTF weights'
for path in files:
 f=TTFont(path);cm=f.getBestCmap();rows=[]
 for n in names:
  u=get_glyph(n).unicode; actual=cm.get(int(u,16)) if u else n if n in f.getGlyphOrder() else None
  rows.append({'required_name':n,'unicode':u,'actual_glyph':actual,'present':actual is not None})
 missing=[r['required_name'] for r in rows if not r['present']]
 assert not missing,(path,missing)
 report['fonts'].append({'file':path.name,'version':f['head'].fontRevision,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'missing':missing,'requirements':rows})

print(f"All {len(names)} official named requirements covered in four weights.")

# Verify localized substitutions and unaffected default text in every weight.
import uharfbuzz as hb
for path in files:
 f=TTFont(path); names=f.getGlyphOrder(); font=hb.Font(hb.Face(path.read_bytes()))
 def shape(text,lang):
  b=hb.Buffer();b.add_str(text);b.guess_segment_properties();b.language=lang;hb.shape(font,b)
  return [names[g.codepoint] for g in b.glyph_infos]
 assert 'periodcentered.loclCAT' in shape('l·l','ca'), (path,shape('l·l','ca'))
 assert 'periodcentered.loclCAT.case' in shape('L·L','ca')
 assert 'periodcentered.loclCAT' not in shape('l·l','en')
 for lang in ['tr','az']:assert shape('i',lang)==['idotaccent'],(path,lang,shape('i',lang))
 assert shape('i','en')==['i']
report['shaping_checks']='Catalan lower/upper, Turkish/Azeri dotted i, default English negative controls: all four weights pass'
(ROOT/'qa/latin-core-coverage.json').write_text(json.dumps(report,indent=2)+'\n')
print(report['shaping_checks'])

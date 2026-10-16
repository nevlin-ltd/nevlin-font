"""Check encoded and unencoded requirements against the pinned official list."""
from pathlib import Path
import json, hashlib
from fontTools.ttLib import TTFont
from glyphsLib.glyphdata import get_glyph
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'qa/GF_Latin_Core.txt'
names=[n for n in source.read_text().splitlines() if n and not n.startswith('#')]
report={'source':'https://github.com/googlefonts/glyphsets/blob/0ac0e515473e39247683ed473fd74728671e2364/data/results/txt/nice-names/GF_Latin_Core.txt','list_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'required_glyphs':len(names),'fonts':[]}
for path in sorted((ROOT/'fonts').glob('*.ttf')):
 f=TTFont(path);cm=f.getBestCmap();rows=[]
 for n in names:
  u=get_glyph(n).unicode; actual=cm.get(int(u,16)) if u else n if n in f.getGlyphOrder() else None
  rows.append({'required_name':n,'unicode':u,'actual_glyph':actual,'present':actual is not None})
 missing=[r['required_name'] for r in rows if not r['present']]
 assert not missing,(path,missing)
 report['fonts'].append({'file':path.name,'version':f['head'].fontRevision,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'missing':missing,'requirements':rows})
(ROOT/'qa/latin-core-coverage.json').write_text(json.dumps(report,indent=2)+'\n')
print(f"All {len(names)} official named requirements covered in four weights.")

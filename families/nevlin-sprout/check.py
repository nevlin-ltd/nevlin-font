"""Focused structural and shaping checks for the development prototype."""
from pathlib import Path
import json, unicodedata
from fontTools.ttLib import TTFont
import uharfbuzz as hb
ROOT=Path(__file__).parent
results=[]
def shape(data,text,features=None):
    font=hb.Font(hb.Face(data));buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(font,buf,features or {})
    return buf.glyph_infos,buf.glyph_positions
samples=['Small steps. Clearer thinking.','Make sense of your money.', 'Il1 O0 rn m', '$12,480.50 € £ ¥ ₸ ₹ ₽', 'café naïve Ångström', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789']
for file in sorted((ROOT/'fonts').glob('*.ttf')):
    data=file.read_bytes();f=TTFont(file);cmap=f.getBestCmap()
    assert all(cp in cmap for cp in range(32,127)), 'Missing ASCII'
    assert set(json.loads((ROOT/'gf-latin-core.json').read_text())) <= set(cmap), 'Missing GF Latin Core'
    assert all(cp in cmap for cp in [0x20AC,0x20B8,0x20B9,0x20BD])
    for sample in samples:
        assert all(g.codepoint!=0 for g in shape(data,sample)[0]),sample
        assert all(g.codepoint!=0 for g in shape(data,unicodedata.normalize('NFD',sample))[0]),sample
    digits=shape(data,'0123456789',{'tnum':1})[1]
    assert len({p.x_advance for p in digits})==1
    assert shape(data,'0',{'zero':1})[0][0].codepoint!=shape(data,'0')[0][0].codepoint
    assert shape(data,'0',{'zero':1,'tnum':1})[1][0].x_advance==640
    assert 'mark' in [r.FeatureTag for r in f['GPOS'].table.FeatureList.FeatureRecord]
    for cp in [0x13D,0x13E,0x10F,0x165]:
        g=f['glyf'][cmap[cp]]
        assert g.isComposite() and len(g.components)==2
        assert g.components[1].glyphName=='caron.side'
    for text in ['i\u030b','j\u030b','į\u0301','i\u0326\u0303']:
        info,_=shape(data,text);names=[f.getGlyphName(g.codepoint) for g in info]
        assert names[0] in ['dotlessi','uni0237','iogonek.dotless','itilde'],(text,names)
    assert f['glyf']['iogonek'].numberOfContours>f['glyf']['iogonek.dotless'].numberOfContours,'iogonek lost its dot'
    for cp in cmap:
        assert all(g.codepoint!=0 for g in shape(data,unicodedata.normalize('NFD',chr(cp)))[0]),hex(cp)
    woff=TTFont(file.with_suffix('.woff2'));assert woff.getBestCmap()==cmap
    badbounds=[]
    for n in f.getGlyphOrder():
        g=f['glyf'][n]
        if hasattr(g,'yMax') and (g.yMax>1050 or g.yMin < -350): badbounds.append(n)
    assert not badbounds,badbounds
    results.append(dict(font=file.name,encoded=len(cmap),gf_latin_core=True,side_caron_components=True,soft_dot_removal=True,iogonek_dot_preserved=True,ascii=True,sample_shaping=True,nfd_all_encoded_characters=True,tabular_advance=640,slashed_zero=True,mark_feature=True,woff2_cmap_matches=True,vertical_bounds=True))
(ROOT/'structural-checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))

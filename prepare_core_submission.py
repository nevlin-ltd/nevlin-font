"""Prepare a Google Fonts-style review directory, without submitting anything."""
from pathlib import Path
import shutil
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontbakery.fonts_public_pb2 import FamilyProto
from google.protobuf import text_format
import uharfbuzz as hb

ROOT=Path(__file__).resolve().parent
STYLES=[('Regular',400),('Medium',500),('SemiBold',600),('Bold',700)]

def specimen(path, lines=None):
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">',
         '<rect width="1200" height="720" fill="#f8f5ff"/>']
    for i,(style,_) in enumerate(STYLES):
        source=ROOT/'fonts/ttf'/f'NevlinFont-{style}.ttf'
        tt=TTFont(source); font=hb.Font(hb.Face(source.read_bytes()));gs=tt.getGlyphSet()
        svg.append(f'<text x="40" y="{38+i*175}" font-family="sans-serif" font-size="16" fill="#8046cf">{style}</text>')
        for j,text in enumerate(lines or ['Make your money make sense.','$12,480.50  €  £  ¥  ₸   0123456789']):
            buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(font,buf,{'tnum':True})
            x=0;scale=40/tt['head'].unitsPerEm
            for glyph,pos in zip(buf.glyph_infos,buf.glyph_positions):
                pen=SVGPathPen(gs);gs[tt.getGlyphName(glyph.codepoint)].draw(pen)
                svg.append(f'<path fill="#201747" transform="translate({40+(x+pos.x_offset)*scale} {90+i*175+j*55-pos.y_offset*scale}) scale({scale} {-scale})" d="{pen.getCommands()}"/>')
                x+=pos.x_advance
    svg.append('</svg>');path.write_text('\n'.join(svg))

def main():
    out=ROOT/'googlefonts/nevlinfont';out.mkdir(parents=True,exist_ok=True)
    p=FamilyProto();p.name='Nevlin Font';p.designer='Nevlin Font Project Authors, Inter Project Authors'
    p.license='OFL';p.category.append('SANS_SERIF');p.date_added='2026-10-16'
    p.subsets.extend(sorted(['latin','latin-ext','menu']))
    p.source.repository_url='https://github.com/nevlin-ltd/nevlin-font'
    for style,weight in STYLES:
        name=f'NevlinFont-{style}.ttf';source=ROOT/'fonts/ttf'/name;tt=TTFont(source)
        f=p.fonts.add();f.name='Nevlin Font';f.style='normal';f.weight=weight;f.filename=name
        f.post_script_name=tt['name'].getDebugName(6);f.full_name=tt['name'].getDebugName(4)
        f.copyright=tt['name'].getDebugName(0)
        shutil.copy(source,out/name)
    (out/'METADATA.pb').write_text(text_format.MessageToString(p))
    shutil.copy(ROOT/'OFL.txt',out/'OFL.txt')
    (out/'DESCRIPTION.en_us.html').unlink(missing_ok=True)
    article=out/'article';article.mkdir(exist_ok=True)
    specimen(article/'specimen.svg')
    specimen(ROOT/'qa/character-proof.svg', ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz  0123456789'])
    (article/'ARTICLE.en_us.html').write_text('''<h1>Nevlin Font</h1>
<p>Nevlin Font explores a familiar interface voice with distinctive details for
financial text. Four upright weights offer a consistent progression from Regular
to Bold. Tabular figures align amounts in columns, while proportional figures
remain available for ordinary text. The modified lowercase forms include a
single-storey g, a rising e crossbar and a compact t. The figures include an open
4 and a short-footed 1.</p>
<img src="specimen.svg" alt="Four weights of Nevlin Font, showing text, amounts and currency symbols">
<p>The project is derived from Inter 4.001. Most inherited letters, spacing and
OpenType functionality remain attributable to the Inter Project Authors. This
is not an independently designed full family. The editable sources include both
those inherited forms and the Nevlin modifications.</p>
<p>The current version is a development candidate. Automated validation and
reproducible builds support technical review, but they do not establish design
originality or replace native-language and cross-platform rendering reviews.
No Google Fonts acceptance is claimed. Contributions and issue reports are
welcome in the public project repository.</p>\n''')
    print('Prepared',out)

if __name__=='__main__':main()

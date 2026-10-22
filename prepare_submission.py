"""Assemble a local review directory. Does not post or submit anything."""
from pathlib import Path
import shutil
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontbakery.fonts_public_pb2 import FamilyProto
from google.protobuf import text_format
import uharfbuzz as hb

ROOT=Path(__file__).parent
def proof(destination,lines,size=34):
    rows=len(lines)*4; height=rows*75+100
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="{height}" viewBox="0 0 1400 {height}"><rect width="1400" height="{height}" fill="#f7f6fe"/>']
    y=50
    for style in ['Regular','Medium','SemiBold','Bold']:
        file=ROOT/'fonts'/'ttf'/f'StudyA-{style}.ttf';tt=TTFont(file);gs=tt.getGlyphSet();font=hb.Font(hb.Face(file.read_bytes()));scale=size/1000
        for line in lines:
            buf=hb.Buffer();buf.add_str(line);buf.guess_segment_properties();hb.shape(font,buf,{'tnum':1});x=45
            for g,p in zip(buf.glyph_infos,buf.glyph_positions):
                pen=SVGPathPen(gs);gs[tt.getGlyphName(g.codepoint)].draw(pen)
                svg.append(f'<path fill="#1f1350" transform="translate({x+p.x_offset*scale} {y-p.y_offset*scale}) scale({scale} {-scale})" d="{pen.getCommands()}"/>');x+=p.x_advance*scale
            y+=75
    svg.append('</svg>');destination.write_text('\n'.join(svg))

def main():
    out=ROOT/'googlefonts/studya';out.mkdir(parents=True,exist_ok=True)
    p=FamilyProto();p.name='Study A';p.designer='Nevlin';p.license='OFL';p.category.append('SANS_SERIF');p.date_added='2026-10-22'
    p.subsets.extend(['latin','latin-ext','menu'])
    p.source.repository_url='https://github.com/nevlin-ltd/nevlin-font'
    for style,weight in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700)]:
        filename=f'StudyA-{style}.ttf';tt=TTFont(ROOT/'fonts'/'ttf'/filename);f=p.fonts.add()
        f.name=p.name;f.style='normal';f.weight=weight;f.filename=filename;f.post_script_name=tt['name'].getDebugName(6);f.full_name=tt['name'].getDebugName(4);f.copyright=tt['name'].getDebugName(0)
        shutil.copy(ROOT/'fonts'/'ttf'/filename,out/filename)
    (out/'METADATA.pb').write_text(text_format.MessageToString(p));shutil.copy(ROOT/'OFL.txt',out/'OFL.txt')
    article=out/'article';article.mkdir(exist_ok=True)
    proof(article/'specimen.svg',['Small steps. Clearer thinking.','Make sense of your money.','$12,480.50  € £ ¥ ₸ ₹ ₽   0123456789'])
    qa=ROOT/'qa';qa.mkdir(exist_ok=True)
    proof(qa/'accents.svg',['Ľ Ľa ľ ľa ď ďa ť ťa — L l d t','Ģģ Ķķ Ļļ Ņņ Șș Țț  Īī Įį','Ææ Œœ Ðð Þþ Đđ Ħħ ẞß Ŋŋ Ʒʒ','i\u030b j\u030b į\u0301 i\u0326\u0303  Åå  Ǿǿ'],32)
    (article/'ARTICLE.en_us.html').write_text("""<h1>Study A — provisional name</h1>
<p>Study A is an upright humanist sans serif developed for everyday interface text and financial education. It has oval bowls, open apertures, a two-storey a and single-storey g. Four static weights include Regular, Medium, SemiBold and Bold. Tabular figures and a slashed zero are optional.</p>
<img src="specimen.svg" alt="Study A in four weights">
<p>This is a revision of the separately drawn Nevlin Sprout project, following Google Fonts' design-quality rejection. The build uses editable Python drawings and UFO sources with Fontmake. No Inter or SF Pro outlines are build inputs. AI-assisted development is disclosed; automated checks do not establish editorial quality.</p>
<p>The public family name, copyright-owner confirmation, CLA and maintenance commitments are pending. This package is for preliminary design review and is not approved for Google Fonts publication. A version number of 1.000 denotes the candidate binary format, not approval.</p>
<p>Sources: repository root in https://github.com/nevlin-ltd/nevlin-font.</p>""")
    print(out)
if __name__=='__main__':main()

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
        file=ROOT/'fonts'/'ttf'/f'NevlinSprout-{style}.ttf';tt=TTFont(file);gs=tt.getGlyphSet();font=hb.Font(hb.Face(file.read_bytes()));scale=size/1000
        for line in lines:
            buf=hb.Buffer();buf.add_str(line);buf.guess_segment_properties();hb.shape(font,buf,{'tnum':1});x=45
            for g,p in zip(buf.glyph_infos,buf.glyph_positions):
                pen=SVGPathPen(gs);gs[tt.getGlyphName(g.codepoint)].draw(pen)
                svg.append(f'<path fill="#1f1350" transform="translate({x+p.x_offset*scale} {y-p.y_offset*scale}) scale({scale} {-scale})" d="{pen.getCommands()}"/>');x+=p.x_advance*scale
            y+=75
    svg.append('</svg>');destination.write_text('\n'.join(svg))

def main():
    out=ROOT/'googlefonts/nevlinsprout';out.mkdir(parents=True,exist_ok=True)
    p=FamilyProto();p.name='Nevlin Sprout';p.designer='Nevlin';p.license='OFL';p.category.append('SANS_SERIF');p.date_added='2026-10-16'
    p.subsets.extend(['latin','latin-ext','menu'])
    p.source.repository_url='https://github.com/nevlin-ltd/nevlin-font'
    for style,weight in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700)]:
        filename=f'NevlinSprout-{style}.ttf';tt=TTFont(ROOT/'fonts'/'ttf'/filename);f=p.fonts.add()
        f.name=p.name;f.style='normal';f.weight=weight;f.filename=filename;f.post_script_name=tt['name'].getDebugName(6);f.full_name=tt['name'].getDebugName(4);f.copyright=tt['name'].getDebugName(0)
        shutil.copy(ROOT/'fonts'/'ttf'/filename,out/filename)
    (out/'METADATA.pb').write_text(text_format.MessageToString(p));shutil.copy(ROOT/'OFL.txt',out/'OFL.txt')
    article=out/'article';article.mkdir(exist_ok=True)
    proof(article/'specimen.svg',['Small steps. Clearer thinking.','Make sense of your money.','$12,480.50  € £ ¥ ₸ ₹ ₽   0123456789'])
    qa=ROOT/'qa';qa.mkdir(exist_ok=True)
    proof(qa/'accents.svg',['Ľ Ľa ľ ľa ď ďa ť ťa — L l d t','Ģģ Ķķ Ļļ Ņņ Șș Țț  Īī Įį','Ææ Œœ Ðð Þþ Đđ Ħħ ẞß Ŋŋ Ʒʒ','i\u030b j\u030b į\u0301 i\u0326\u0303  Åå  Ǿǿ'],32)
    (article/'ARTICLE.en_us.html').write_text('''<h1>Nevlin Sprout</h1>
<p>Nevlin Sprout is an upright geometric sans serif designed for approachable
financial education. Its gently squared bowls, open forms and distinctive
capital I, lowercase l and figure 1 support clear lesson text and amounts.
The family includes Regular, Medium, SemiBold and Bold. Optional tabular figures
align numerical columns and an optional slashed zero distinguishes zero from O.</p>
<img src="specimen.svg" alt="Four weights of Nevlin Sprout showing text and currency figures">
<p>The outlines originate in newly authored geometric drawing sources. No Inter,
SF Pro or other font binary is used as a build input. Development uses
AI-assisted code, editable UFO sources and Fontmake. This is an unreleased
review candidate; its originality and suitability remain subject to editorial
and independent type-design assessment.</p>
<p>The working family name, designer attribution and publication metadata need
confirmation during onboarding. Sources and candidate binaries are public in the Nevlin font repository,
under families/nevlin-sprout. This review candidate is not yet available
in the Google Fonts catalog.</p>''')
    print(out)
if __name__=='__main__':main()

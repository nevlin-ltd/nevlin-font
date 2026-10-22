from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1]
for style in ['Regular','Medium','SemiBold','Bold']:
 fn=R/'fonts/ttf'/f'StudyA-{style}.ttf';tt=TTFont(fn);cps=[cp for cp in tt.getBestCmap() if cp not in (32,160,8232,8233)]
 im=Image.new('RGB',(1600,((len(cps)+11)//12)*130),'white');d=ImageDraw.Draw(im);f=ImageFont.truetype(str(fn),58)
 for i,cp in enumerate(cps):
  x=(i%12)*133;y=(i//12)*130;d.text((x+5,y+4),f'{cp:04X}',fill='#666666');d.text((x+8,y+20),chr(cp),font=f,fill='#241744')
 im.save(R/'qa'/f'atlas-{style}.png')

"""Render the final binary font's changed characters with Pillow/FreeType."""
from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
ROOT=Path(__file__).parent
im=Image.new('RGB',(1600,1300),'#f7f6fe');d=ImageDraw.Draw(im)
lines=['Ľ Ľa ľ ľa ď ďa ť ťa     L l d t','Ææ Œœ Ðð Þþ Đđ Ħħ ẞß Ŋŋ Ʒʒ','Ģģ Ķķ Ļļ Ņņ Șș Țț Īī Įį  Ǿǿ']
y=30
for style in ['Regular','Medium','SemiBold','Bold']:
    font=ImageFont.truetype(str(ROOT/'fonts'/'ttf'/f'NevlinSprout-{style}.ttf'),52)
    d.text((45,y),style,font=font,fill='#8749d0');y+=60
    for line in lines:d.text((45,y),line,font=font,fill='#1f1350');y+=70
    y+=30
im.save(ROOT/'qa/accents.png')

"""New Latin drawings and constructions for the Sprout submission candidate."""
import math, unicodedata
import pathops

def extend(paths, widths, marks, t, stroke, transform, dot):
    def add(c,w,*ds):paths[c]=stroke(ds,t);widths[c]=w
    def combine(c,w,*pieces):
        p=pathops.Path()
        for piece in pieces:p.addPath(piece)
        paths[c]=p;widths[c]=w
    # Shared stems avoid the acute cusps created by overlapping whole letters.
    add('Æ',890,'M65 0 L340 700 L465 700 L465 0','M160 235 L465 235','M465 700 L820 700','M465 365 L770 365','M465 0 L820 0')
    add('Œ',940,'M470 700 L300 700 C140 700 85 615 85 450 L85 250 C85 85 140 0 300 0 L470 0 Z','M470 700 L865 700','M470 365 L810 365','M470 0 L865 0')
    left='M400 500 L270 500 C130 500 85 425 85 250 C85 75 130 0 270 0 L400 0 Z'
    right='M400 245 L790 245 L790 290 C790 435 740 500 595 500 C450 500 400 425 400 250 C400 75 455 0 605 0 C690 0 745 25 785 75'
    add('œ',875,left,right)
    add('æ',875,'M95 425 C135 480 195 500 270 500 C360 500 400 445 400 340 L400 0','M400 280 L240 280 C130 280 85 230 85 140 C85 45 140 0 230 0 C310 0 365 45 400 110',right)
    add('Þ',605,'M85 700 L85 0','M85 560 L315 560 C470 560 530 490 530 360 C530 230 470 160 315 160 L85 160')
    add('þ',580,'M85 720 L85 -220','M85 390 C135 475 205 500 290 500 C445 500 495 425 495 250 C495 75 445 0 290 0 C205 0 135 25 85 110')
    add('ð',580,'M130 720 C330 710 495 545 495 250 C495 75 440 0 290 0 C140 0 85 75 85 235 C85 390 140 460 285 460 C385 460 455 400 490 325','M120 545 L385 730')
    for c,base,bar in [('Ð','D','M35 350 L300 350'),('Đ','D','M35 350 L300 350'),('đ','d','M315 610 L565 610'),('Ħ','H','M35 540 L615 540'),('ħ','h','M25 610 L310 610'),('Ŧ','T','M130 365 L440 365'),('ŧ','t','M45 285 L310 285'),('Ǥ','G','M440 200 L635 200'),('ǥ','g','M375 -65 L565 -65')]:
        combine(c,widths[base],paths[base],stroke([bar],t*.8))
    add('Ŋ',650,'M85 0 L85 700 L565 0','M565 700 L565 -55 C565 -180 510 -230 375 -205')
    add('ŋ',570,'M85 500 L85 0','M85 355 C135 455 210 500 305 500 C435 500 485 435 485 305 L485 -75 C485 -185 440 -225 335 -205')
    add('ſ',285,'M105 0 L105 550 C105 685 155 730 270 700')
    add('ẞ',690,'M85 0 L85 515 C85 650 155 700 315 700 L500 700 L355 390 C530 355 605 295 605 175 C605 55 520 0 390 0 L285 0')
    add('Ʒ',570,'M75 700 L490 700 L265 385 C405 385 490 300 490 175 C490 50 410 0 280 0 C180 0 105 30 65 90')
    add('ʒ',500,'M65 500 L425 500 L235 260 C350 260 425 185 425 65 C425 -55 355 -140 230 -140 C155 -140 95 -115 65 -75')
    for c,b1,b2 in [('Ĳ','I','J'),('ĳ','i','j')]:combine(c,widths[b1]+widths[b2],paths[b1],transform(paths[b2],widths[b1]))
    for c,base in [('Ŀ','L'),('ŀ','l')]:combine(c,widths[base]+80,paths[base],dot(widths[base]+15,330,t*1.2))
    marks['\u0326']=stroke(['M20 -85 L-15 -185'],t*.7)
    # Add exactly the named European extensions, not every decomposable codepoint.
    for c in 'ǍǎǓǔǦǧǨǩǮǯǾǿȘșȚțȞȟẀẁẂẃẄẅẼẽỲỳ':
        base,mark=unicodedata.normalize('NFD',c)
        top=0 if mark=='\u0326' else (760 if base.isupper() or base in 'bdfhklt' else 560)
        combine(c,widths[base],paths[base],transform(marks[mark],widths[base]/2,top))
    for c,base in [('ª','a'),('º','o')]:combine(c,370,transform(paths[base],20,360,.55,.55))
    combine('¡',230,transform(paths['!'],230,700,-1,-1))
    combine('¿',490,transform(paths['?'],490,700,-1,-1))
    combine('¢',530,paths['c'],stroke(['M280 625 L280 -125'],t*.8))
    add('§',570,'M470 650 C420 700 355 720 280 720 C145 720 85 660 85 565 C85 460 175 425 295 390 C425 350 485 300 485 210 C485 120 415 70 315 70','M100 -20 C150 -70 215 -90 290 -90 C425 -90 485 -30 485 65 C485 170 395 205 275 240 C145 280 85 330 85 420 C85 510 155 560 255 560')
    add('¶',590,'M340 0 L340 700 L250 700 C115 700 65 630 65 500 C65 370 115 300 250 300 L340 300','M495 700 L495 0')
    # Copyright/registered circle with independently scaled original C/R.
    circle='M375 0 C160 0 65 110 65 350 C65 590 160 700 375 700 C590 700 685 590 685 350 C685 110 590 0 375 0 Z'
    for c,base in [('©','C'),('®','R')]:combine(c,750,stroke([circle],t*.7),transform(paths[base],205,150,.55,.55))
    combine('™',760,transform(paths['T'],20,350,.5,.5),transform(paths['M'],330,350,.5,.5))
    for c,m in [('¨','\u0308'),('¯','\u0304'),('´','\u0301'),('¸','\u0327'),('ˆ','\u0302'),('ˇ','\u030c'),('˘','\u0306'),('˙','\u0307'),('˚','\u030a'),('˛','\u0328'),('˜','\u0303'),('˝','\u030b')]:
        combine(c,350,transform(marks[m],175,0 if m in '\u0327\u0328' else 560))
    combine('°',350,transform(marks['\u030a'],175,480))
    add('‹',330,'M255 480 L85 260 L255 40')
    add('›',330,'M75 480 L245 260 L75 40')
    for c,base in [('«','‹'),('»','›')]:combine(c,550,paths[base],transform(paths[base],220))
    for c,base in [('‚','’'),('„','”')]:combine(c,widths[base],transform(paths[base],0,-650))
    # Opening quotations turn in the opposite direction to closing quotations.
    for c,base in [('‘','’'),('“','”'),('ʻ','’')]:combine(c,widths[base],transform(paths[base],widths[base],1290,-1,-1))
    for c in '\u2028\u2029':paths[c]=pathops.Path();widths[c]=0
    p=pathops.Path()
    for n in range(12):
        angle=2*math.pi*n/12;p.addPath(dot(330+230*math.cos(angle),260+230*math.sin(angle),t*.72))
    paths['◌']=p;widths['◌']=660

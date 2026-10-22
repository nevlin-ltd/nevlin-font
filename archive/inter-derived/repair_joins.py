"""Trim needle-like contour junctions after overlap removal.

The maximum trim is 24/2048 em along either adjacent segment. It creates a
small flat at the bottom of a tight join, preserving the surrounding curves.
This is geometry repair, not a QA exclusion. Changes are logged per glyph.
"""
import math
from fontTools.pens.basePen import BasePen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.misc.bezierTools import splitQuadraticAtT

class Segments(BasePen):
    def __init__(self, gs):
        super().__init__(gs); self.contours=[]
    def _moveTo(self,p): self.current=[]; self.start=p; self.last=p
    def _lineTo(self,p):
        if p != self.last:self.current.append((self.last,p))
        self.last=p
    def _qCurveToOne(self,c,p):self.current.append((self.last,c,p));self.last=p
    def _closePath(self):
        self._lineTo(self.start);self.contours.append(self.current)
    def _endPath(self):self._closePath()

def point(s,t):
    if len(s)==2:return tuple(a+(b-a)*t for a,b in zip(s[0],s[1]))
    return tuple((1-t)**2*a+2*(1-t)*t*b+t*t*c for a,b,c in zip(*s))

def cut_time(s,at_end):
    origin=s[-1] if at_end else s[0]
    # Limit trimming to a quarter of a short segment.
    endpoint=point(s,.75 if at_end else .25)
    distance=min(24,math.dist(origin,endpoint))
    lo,hi=0.,1.
    for _ in range(30):
        t=(lo+hi)/2; d=math.dist(origin,point(s,1-t if at_end else t))
        if d<distance:lo=t
        else:hi=t
    return 1-(lo+hi)/2 if at_end else (lo+hi)/2

def portion(s,a,b):
    if len(s)==2:return (point(s,a),point(s,b))
    if b<1:s=splitQuadraticAtT(*s,b)[0]
    if a>0:s=splitQuadraticAtT(*s,a/b)[1]
    return s

def repair_joins(font):
    gs=font.getGlyphSet(); changes=[]; replacements={}
    for name in font.getGlyphOrder():
        glyph=font['glyf'][name]
        if glyph.numberOfContours<=0:continue
        pen=Segments(gs);gs[name].draw(pen)
        result=[];count=0
        for contour in pen.contours:
            n=len(contour);starts=[0.]*n;ends=[1.]*n
            for i,s in enumerate(contour):
                prev=contour[i-1]
                u=(prev[-2][0]-s[0][0],prev[-2][1]-s[0][1])
                v=(s[1][0]-s[0][0],s[1][1]-s[0][1])
                lengths=math.hypot(*u)*math.hypot(*v)
                if not lengths:continue
                angle=math.acos(max(-1,min(1,(u[0]*v[0]+u[1]*v[1])/lengths)))
                if 0<angle<.25:
                    ends[i-1]=cut_time(prev,True);starts[i]=cut_time(s,False);count+=1
            result.append([portion(s,starts[i],ends[i]) for i,s in enumerate(contour)])
        if not count:continue
        output=TTGlyphPen(None)
        for contour in result:
            output.moveTo(contour[0][0])
            for i,s in enumerate(contour):
                if i and s[0]!=contour[i-1][-1]:output.lineTo(s[0])
                if len(s)==2:output.lineTo(s[-1])
                else:output.qCurveTo(s[1],s[2])
            output.closePath()
        replacements[name]=output.glyph();changes.append({'glyph':name,'junctions':count})
    for name,g in replacements.items():font['glyf'][name]=g
    return changes

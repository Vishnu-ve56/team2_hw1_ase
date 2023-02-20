import math
from src.sym import SYM
from src.misc import Misc
import copy
from src.globals import *

def RANGE(at,txt,lo,hi = None):
    return {"at":at,"txt":txt,"lo":lo,"hi":lo or hi or lo ,"y":SYM()}

def bins(cols,rowss):
    out = []
    for col in cols:
        ranges = {}
        for y in rowss:
            for row in rowss[y]:
                x = row.cells[col.at]
                if x != "?":
                    k = int(bin(col,x))
                    if k not in ranges:
                        ranges[k] = RANGE(col.at,col.txt,x)
                    extend(ranges[k], x, y)
        ranges = list(dict(sorted(ranges.items(), key=lambda x:x[1]["lo"])).values())
        out.append(ranges if isinstance(col,SYM) else mergeAny(ranges))

    return out


def extend(range,n,s):
    range["lo"] = min(n, range["lo"])
    range["hi"] = max(n, range["hi"])
    range["y"].add(s)

def bin(col,x):
    if x == "?" or isinstance(col,SYM):
        return x
    misc = Misc()
    the= misc.getThe()
    tmp = (col.hi-col.lo)/(the["bins"]-1)
    return 1 if col.hi == col.lo else math.floor(x / tmp + 0.5) * tmp


def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1, len(t)):
            t[j]["lo"] = t[j-1]["hi"]
        
        t[0]["lo"] = float("-inf")
        t[len(t)-1]["hi"]  = float("inf")
        return t
    
    ranges1 = []
    j = 0
    while j <= len(ranges0)-1:
        left = ranges0[j]
        if( j == len(ranges0) - 1):
            right = None
        else:
            right = ranges0[j+1]
        if right:
            y = merge2(left["y"], right["y"])
            if y:
                j  = j + 1
                left["hi"], left["y"] = right["hi"], y
        
        ranges1.append(left)
        j+=1
    
    if len(ranges0)==len(ranges1):
        return noGaps(ranges0)

    else:
        return mergeAny(ranges1)

def merge2(col1, col2):
  new = merge(col1,col2)
  if new.div() <= (col1.div()*col1.n + col2.div()*col2.n)/new.n:
    return new
  
def merge(col1, col2):
    new  = copy.deepcopy(col1)
    if isinstance(col1, SYM):
        for i in col2.has:
            new.add(i)
    else:
        for i in col2.has:
            new.add(new,i)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi) 
    return new

def value(has,nB = None, nR = None, sGoal = None):
    sGoal,nB,nR = sGoal or True, nB or 1, nR or 1
    b,r = 0,0
    for x,n in has.items():
        if x==sGoal:
            b = b + n
        else:
            r = r + n
    b = b/(nB+1/float("inf"))
    r = r/(nR+1/float("inf"))
    return b**2/(b+r)

def cliffsDelta(ns1, ns2):
    if ns1>256:
        ns1=many(ns1,256)
    if ns2>256:
        ns2=many(ns2,256)
    if ns1>10*len(ns2):
        ns1=many(ns1,10*len(ns2))
    if ns2>10*len(ns1):
        ns2=many(ns2,10*len(ns1))
    n, gt, lt=0, 0, 0
    for a,x in enumerate(ns1):
        for b,y in enumerate(ns2):
            n=n+1
            if x>y:
                gt+=1
            if x<y:
                lt+=1
    obj= Misc()
    return math.abs(lt-gt)/n > obj.getThe()["cliffs"]




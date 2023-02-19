import math

from sym import SYM
from misc import Misc

def RANGE(at,txt,lo,hi):
    return {"at":at,"txt":txt,"lo":lo,"hi":lo or hi ,"y":SYM()}

def bins(cols,rowss):
    out = []
    for _,col in enumerate(cols):
        ranges = {}
        for y,rows in enumerate(rowss):
            for _,row in enumerate(rows):
                x,k = row[col.at]
                if x != "?":
                    k = int(bin(col,x))
                    if k not in ranges:
                        ranges[k] = RANGE(col.at,col.txt,x)
                    extend(ranges[k],x,y)
        ranges = dict(sorted(ranges.items(), key=lambda x:x[1]["lo"]))
        out.append(ranges if isinstance(col,SYM) else mergeAny(ranges))
        

def extend(range,n,s):
    range["lo"] = min(n, range["lo"])
    range["hi"] = max(n, range["hi"])
    range["y"].append(s)

def bin(col,x):
    if x == "?" or isinstance(col,SYM):
        return x
    misc = Misc()
    the= misc.getThe()
    tmp = (col["hi"]-col["lo"])/(the["bins"]-1)
    return 1 if col["hi"] == col["lo"] else math.floor(x / tmp + 0.5) * tmp


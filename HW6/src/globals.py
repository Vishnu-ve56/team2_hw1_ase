import math
import copy
import re
import json


def rnd(n, places=None):
    mult=10**(places or 3)
    return math.floor(n*mult + 0.5)/mult

def coerce(s):
    def fun(s1):
        if s1.lower() == "true":
            return True
        elif s1.lower() == "false":
            return False
        return s1
    try:
        val = float(s)
        if(val == int(val)):
            val = int(val)
    except:
        val = fun(s.strip())
        
    return val 

def kap(t,fun):
    u={}
    for k,v in enumerate(t):
        v,k = fun(k,v)
        u[k or 1+len(u)] = v
    return u

def userdefinedmap(t, fun):
    u={}
    for k,v in enumerate(t):
        v,k = fun(v)
        u[k or 1+len(u)] = v
    return u

def mapNew(t, fun):
    if(type(t[0]) == str):
        fun(t)
    else:
        for row in t:
            fun(row)


def oo(t):
    print(o(t))
    return t

def o(t):
    if type(t)!=dict and type(t)!=list:
        return str(t)
    
    def fun(k,v):
        if(str(k).find('_')!=0):
            v = o(v)
            return ":" + str(k) + " " + o(v)
        
        else:
            return False
    array = []
    if type(t) == dict:
        for key in t:
            output = fun(key, t[key])
            if output:
                array.append(output)
            array.sort()
    elif type(t) == list:
        array = t
    return "{" + " ".join(str(val) for val in array) + "}"

Seed=937162211

# def putSeed():
#     global Seed
#     f=open("seed.txt","w")
#     f.write(str(Seed))
#     f.close()

# def setSeed():
#     global Seed
#     f=open("seed.txt","r")
#     contents=f.read()
#     Seed=int(contents)
#     print(Seed)
#     f.close()


def rand(lo, hi=None):
    global Seed
    lo, hi = lo or 0, hi or 1
    Seed  =  (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed/2147483647 

def rint(lo, hi= None):
    return math.floor(0.5 + rand(lo, hi))

def cosine(a,b,c):
    den = 1 if c == 0 else 2*c
    x1 = (a**2 + c**2 - b**2)/den
    x2 = max(0,min(1,x1))
    y = (a**2 - x2**2)**0.5
    if type(y)==complex:
        y=0
    return x2,y


def many(t,n ):
    u = []
    for i in range(0,n):
        u.append(any(t))
    return u

def last(t):
    return t[len(t)-1]

def any(t):
    return t[rint(0, len(t) - 1)]

def show(node, what=0, cols=0, nPlaces=0,lvl=0):
    if node:
        string=lvl*"|" 
        if node["left"]==None:
            print(string,o(last(last(node["data"].rows).cells)))
        else:
            string1="%.f"%(rnd(100*node["c"]))
            print(string,string1)
        show(node["left"],what,cols,nPlaces,lvl+1)
        show(node["right"],what,cols,nPlaces,lvl+1)

def copyDefined(t):
    return copy.deepcopy(t)

def dofile(file):
    textfile = open(file, "r")
    data = textfile.read()
    x = re.search("return {(.*)}",data,re.DOTALL)
    result = x.groups()[0].replace("=",":")
    result = result.replace("\'","\"")
    result =  result.replace("{","[")
    result =  result.replace("}", "]")
    result = result.replace('_','"_"')
    result = re.sub(r'(\w+):',r'"\1":',result)
    final  = "{" + result + "}"
    mydict = eval(final)
    textfile.close()
    return mydict

def transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez

def firstN(sortedRanges, scoreFun):
    print("")
    for r in sortedRanges:
        print(r["range"]["txt"], r["range"]["lo"], r["range"]["hi"], rnd(r["val"]), o(r["range"]["y"].has))

    first = sortedRanges[0]["val"]

    def useful(range):
        if range["val"] > 0.05 and range["val"] > first / 10:
            return range

    sortedRanges = list(filter(lambda r: r is not None, map(useful, sortedRanges)))
    most, out = -1, -1

    for n in range(1, len(sortedRanges) + 1):
        ranges = list(map(lambda r: r["range"], sortedRanges[:n]))
        tmp, rule = scoreFun(ranges)
        if tmp and tmp > most:
            out, most = rule, tmp

    return out, most

def dictionaryKap(t, fun):
    u = {}
    for k,v in t.items():
        v, k = fun(k,v) 
        u[k or len(u)] = v
    return u

def value(has, nB, nR, sGoal=None):
    sGoal, nB, nR = sGoal or True, nB or 1, nR or 1
    b, r = 0, 0

    for x, n in has.items():
        if x == sGoal:
            b += n
        else:
            r += n

    b, r = b / (nB + 1 / float("inf")), r / (nR + 1 / float("inf"))
    return b ** 2 / (b + r)

def prune(rule, maxSize):
    n = 0
    for txt, ranges in rule.items():
        n += 1
        if len(ranges) == maxSize[txt]:
            n -= 1
            del rule[txt]
    if n > 0:
        return rule

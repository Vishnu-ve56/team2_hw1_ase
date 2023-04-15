import math
import copy
import re
import json
import pandas as pd
import numpy as np
import os




top_table = {'all': {'data' : [], 'evals' : 0},
             'sway1': {'data' : [], 'evals' : 0},
             'sway2': {'data' : [], 'evals' : 0},
             'xpln1': {'data' : [], 'evals' : 0},
             'xpln2': {'data' : [], 'evals' : 0},
             'top': {'data' : [], 'evals' : 0}}

bottom_table = [[['all', 'all'],None],
                [['all', 'sway1'],None],
                [['sway1', 'sway2'],None],
                [['sway1', 'xpln1'],None],
                [['sway2', 'xpln2'],None],
                [['sway1', 'top'],None]]

def avgStat(dataList,iter):
    res={}
    for i in dataList:
        for k,v in i.stats().items():
            res[k]=res.get(k,0)+v
    for k,v in res.items():
        res[k]/=iter
    return res






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

def kap(t, fun):
    u = {}
    for v in t:
        k = t.index(v)
        v, k = fun(k,v) 
        u[k or len(u)] = v
    return u


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


def rand(lo = None, hi=None):
    global Seed
    lo, hi = lo or 0, hi or 1
    Seed  =  (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed/2147483647 

def rint(lo, hi= None):
    return math.floor(0.5 + rand(lo, hi))

def cosine(a,b,c):
    den = 1 if c == 0 else 2*c
    x1 = (a**2 + c**2 - b**2) / den
    return x1


def many(t,n):
    u=[]
    for _ in range(1,n+1):
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
    # for r in sortedRanges:
    #     print(r["range"]["txt"], r["range"]["lo"], r["range"]["hi"], rnd(r["val"]), o(r["range"]["y"].has))

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
    newRule = {}
    for txt, ranges in rule.items():
        n += 1
        if len(ranges) == maxSize[txt]:
            n -= 1
            rule[txt] = None
        else:
            newRule[txt] = ranges
    if n > 0:
        return newRule

    return None

def handleMissingValues(file, Data):

    currentWorkingPath = os.path.dirname(__file__)
    fileName = os.path.join(currentWorkingPath, file)
    df=pd.read_csv(fileName)
    for c in df.columns[df.eq('?').any()]:
        df[c]=df[c].replace('?',np.nan)
        df[c]=df[c].astype(float)
        df[c]=df[c].fillna(df[c].mean())
    file=file.replace('.csv','_handled.csv')
    fileName=fileName.replace('.csv','_handled.csv')
    df.to_csv(fileName, index=False)
    return Data(file)


                              


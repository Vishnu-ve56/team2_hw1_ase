import math
import copy

def rnd(n, places):
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
    x1 = (a**2 + c**2 - b**2)/(2*c)
    x2 = max(0,min(1,x1))
    # print("a",a,"x2",x2)
    y = (a**2 - x2**2)**0.5
    # print("y",y)
    if type(y)==complex:
        y=0
    return x2,y


def many(t,n ):
    u = []
    for i in range(0,n):
        u.append(any(t))
    return u


def any(t):
    return t[rint(len(t))-1]

def show(node, what, cols, nPlaces,lvl=0):
    if node:
        string=lvl*"|" + str(len(node["data"].rows)) + "  "
        if node["left"]==None or lvl==0:
            print(string, o(node["data"].stats("mid", node["data"].cols.y, nPlaces)))
        else:
            print(string, "")
        show(node["left"],what,cols,nPlaces,lvl+1)
        show(node["right"],what,cols,nPlaces,lvl+1)

def copyDefined(t):
    return copy.deepcopy(t)

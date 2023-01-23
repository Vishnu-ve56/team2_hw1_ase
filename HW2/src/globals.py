import math
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
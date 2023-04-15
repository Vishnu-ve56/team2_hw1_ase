from src.globals import *
import sys
from src.misc import Misc


class NUM:
    def __init__(self, at = 0,txt = "", t = None):
        self.at = at
        self.txt = txt
        self.mu = 0
        self.n = 0
        self.m2 = 0
        self.sd = 0
        self.has = {}
        self.hi =-1*sys.maxsize
        self.lo = sys.maxsize
        try:
            self.w = self.txt.index('-')
            self.w = -1

        except:
            self.w = 1

        if t:
            for n in t:
                self.add(n)

    def add(self, n):
        if n != "?":
            self.n = self.n + 1
            all = len(self.has)
            the = Misc().getThe()
            pos = all + 1 if all < the["Max"] else rint(1, all) if rand() < the["Max"] / self.n else 0

            if pos:
                self.has[pos] = n
                self.ok = False
                
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n-self.mu)
            self.lo = min(n,self.lo)
            self.hi = max(n,self.hi)
            self.sd =  0 if self.n<2 else (self.m2/(self.n - 1))**.5

    def mid(self):
        return self.mu
    
    def div(self):
        return (self.m2 < 0 or self.n < 2) and 0 or (self.m2/(self.n-1))**0.5

    def rnd(self, x, n):
        if x=="?":
            return x
        else:
            return rnd(x,n)

    def norm(self, n):
        return n=="?" and n or (n-self.lo)/(self.hi-self.lo + 1e-32)

    def values(self):
        return list(dict(sorted(self.has.items(), key=lambda x: x[1])).values())
    

    def dist(self,n1,n2):
        if n1 == "?" and n2 == "?":
            return 1
        n1,n2 = self.norm(n1), self.norm(n2)
        if n1 == "?":
            n1 = n2<0.5 and 1 or 0
        if n2 == "?":
            n2 = n1<0.5 and 1 or 0
        return abs(n1-n2)
        




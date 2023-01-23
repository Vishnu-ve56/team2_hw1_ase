from src.globals import rnd
import sys
class NUM:
    def __init__(self, at = 0,txt = ""):
        self.at = at
        self.txt = txt
        self.mu = 0
        self.n = 0
        self.m2 = 0
        self.hi =-1*sys.maxsize
        self.lo = sys.maxsize
        try:
            self.w = self.txt.index('-')
            self.w = -1

        except:
            self.w = 1


    def add(self, n):
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n-self.mu)
            self.lo = min(n,self.lo)
            self.hi = max(n,self.hi)
        
    def mid(self):
        return self.mu
    
    def div(self):
        return (self.m2 < 0 or self.n < 2) and 0 or (self.m2/(self.n-1))**0.5

    def rnd(self, x, n):
        if x=="?":
            return x
        else:
            return rnd(x,n)

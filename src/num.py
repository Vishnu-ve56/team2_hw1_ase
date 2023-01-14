import math 
import sys
class NUM:
    def __init__(self):
        self.mu = 0
        self.n = 0
        self.m2 = 0
        self.hi = sys.minint
        self.lo = sys.maxint

    def add(self, n):
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n-self.mu)
            self.lo = math.min(n,self.lo)
            self.hi = math.max(n,self.hi)
        
    def mid(self,x):
        return self.mu
    
    def div(self,x):
        return (self.m2 < 0 or self.n < 2) and 0 or (self.m2/(self.n-1))**0.5
        
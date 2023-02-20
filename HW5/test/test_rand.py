from src.num import NUM
from src.globals import *

class TestRand:
    def __init__(self,seed):
        self.tempSeed = seed
        self.seed = seed
    def testrand(self):
        
        num1 = NUM()
        num2 = NUM()
        for _ in range(1000):
            num1.add(self.rand(0,1))
        self.seed = self.tempSeed
        for _ in range(1000):
            num2.add(self.rand(0,1))
        m1,m2 = rnd(num1.mid(),10), rnd(num2.mid(),10)
        return m1==m2 and 0.5 == rnd(m1,1)

    
    def rand(self,lo,hi):
        lo = lo or 0
        hi = hi or 1
        self.seed = ((16807*self.seed)%2147483647)
        return lo + (hi-lo) * self.seed / 2147483647

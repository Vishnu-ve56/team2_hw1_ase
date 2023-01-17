from src.num import NUM

class TestRand:
    def __init__(self,seed):
        self.seed=seed
    def testrand(self):
        
        num1 = NUM()
        num2 = NUM()
        for _ in range(1000):
            num1.add(self.rand(0,1))
        for _ in range(1000):
            num2.add(self.rand(0,1))
        m1,m2 = round(num1.mid(),10), round(num2.mid(),10)
        return m1==m2 and "0.5" == str(m1)[:3]

    
    def rand(self,lo,hi):
        lo = lo or 0
        hi = hi or 1
        Seed = ((16807*self.seed)%2147483647)
        return lo + (hi-lo) * Seed / 2147483647

'''
eg("rand","generate, reset, regenerate same", function()
  local num1,num2 = NUM(),NUM()
  Seed=the.seed; for i=1,10^3 do num1:add( rand(0,1) ) end
  Seed=the.seed; for i=1,10^3 do num2:add( rand(0,1) ) end
  local m1,m2 = rnd(num1:mid(),10), rnd(num2:mid(),10)
  return m1==m2 and .5 == rnd(m1,1) end )
'''
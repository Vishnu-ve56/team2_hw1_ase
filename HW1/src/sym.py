import math
class SYM:
    def __init__(self):
        self.n=0
        self.has={}
        self.most=0
        self.mode= None
    
    def add(self, x):
        if x != "?":
            self.n+=1
            if x in self.has:
                self.has[x]+=1
            else:
                self.has[x]=1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x
    def mid(self):
        return self.mode

    def div(self):
        def fun(p):
            return p*math.log(p,2)
        e=0
        for i in self.has:
            e+=fun(self.has[i]/self.n)
        return -e



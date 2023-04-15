from src.num import NUM
from src.sym import SYM

class Col:
    def __init__(self,t):
        self.names,self.all,self.x,self.y,self.klass = t,[],[],[],None
        for n,s in enumerate(t):
            if s[0] <= "Z" and s[0] >= "A":
                col = NUM(n, s)
            else:
                col = SYM(n, s)
            
            self.all.append(col)
            if(s[-1]!= 'X'):
                if(s[-1]!='!'):
                    self.klass = col
                if(s[-1]!='!' and s[-1]!='+' and s[-1]!='-'):
                    self.x.append(col)
                else:
                    self.y.append(col)

    def add(self, row):
        self.accepted = self.x + self.y
        for i in self.accepted:
            i.add(row.cells[i.at])
    

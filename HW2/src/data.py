from src.csv import csv
from src.rows import Row
from src.cols import Col
class Data:
    def __init__(self, src):
        self.rows=[]
        self.cols= None
        if type(src)==str:
            cs=csv(src)
            cs.readFromCsv(self.add)
        
    def add(self, t):
        if self.cols:
            t=Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=Col(t)
    
    def stats(self):
        pass
            
data = Data("../data/auto93.csv")

# print(len(data.rows))
# print(data.cols.y[0].w)
# print(len(data.cols.x))
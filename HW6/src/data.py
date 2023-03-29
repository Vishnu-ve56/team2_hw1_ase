from src.csv import csv
from src.rows import Row
from src.cols import Col

from src.globals import *
from src.misc import Misc
from src.discretization import bins
import math

class Data:
    def __init__(self, src):
        self.rows=[]
        self.cols= None
        if type(src)==str:
            cs=csv(src)
            cs.readFromCsv(self.add)
        else:
            mapNew(src, self.add)
        
    def add(self, t):
        if self.cols:
            if(type(t) == list):
                t=Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=Col(t)

    
    def stats(self, what, cols, nPlaces):
        def fun(k, col):
            callable = getattr(col, what)
            return col.rnd(callable(), nPlaces), col.txt
        return kap(cols, fun)

    def clone(self, init):
        data = Data(self.cols.names)
        mapNew(init,data.add)
        return data
    
    def furthest(self,row1, rows,cols=None):
        t=self.around(row1, rows,cols)
        return t[len(t)-1]
    
    
    def dist(self, row1, row2, cols):
        misc = Misc()
        the= misc.getThe()
        n,d = 0,0
        
        for _,col in enumerate(cols or self.cols.x):
            n+=1
            d+=col.dist(row1.cells[col.at],row2.cells[col.at])**the["p"]
        return (d/n) ** (1/the["p"])

    def around(self, row1,rows = None,cols = None):
        def fun(row2):
            return [row2, self.dist(row1, row2, cols)]
        
        val = list(map(fun, rows or self.rows))

        val = sorted(val, key=lambda x: x[1])
        return val

    def half(self, rows = None, cols = None, above = None):
        misc = Misc()
        the = misc.getThe()
        def project(row):
            return [row, cosine(dist(row,A),dist(row,B),c)]
        def dist(row1,row2):
            return self.dist(row1,row2,cols)

        rows = rows or self.rows
        some = many(rows, the["Halves"])
        A = above or any(some)
        listIndice = int((the["Far"] * len(rows))//1)
        

        B = self.around(A,some)[listIndice][0]

        c = dist(A,B)

        val = list(map(project, rows))
        val = sorted(val, key=lambda x: x[1])
        left = []
        right = []

        nums = 0
        mid = None
        for values in val:
            nums+=1
            if nums <= len(rows)/2:
                left.append(values[0])
                mid = values[0]
            else:
                right.append(values[0])
        
        evals= 1 if the['Reuse'] and above else 2
        

        return left, right, A, B, c, evals

    def better(self, row1,row2):
        s1,s2,ys = 0,0,self.cols.y
        for _,col in enumerate(ys):
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (-x+y)/len(ys))
        return s1 < s2
    


    def cluster(self, rows=None, min=None, cols=None, above=None):
        rows=rows or self.rows
        cols=cols or self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows)>=2:
            left, right, node["A"],node["B"], node["mid"],node["c"] = self.half(rows,cols,above)
            node["left"]=self.cluster(left,min,cols,node["A"])
            node["right"]=self.cluster(right,min,cols,node["B"])
        if "left" not in node:
            node["left"]=None
        if "right" not in node:
            node["right"]=None   
        return node

    
    def sway(self):
        misc = Misc()
        the= misc.getThe()
        def worker(rows,worse,evalsZ=None,above=None):
            if len(rows) <= len(self.rows)**the['min']:
                return rows, many(worse, the["rest"]*len(rows)), evalsZ
            else:
                l,r,A,B,_, evals = self.half(rows,None,above)
                if self.better(B,A):
                    l,r,A,B = r,l,B,A
                for i in r:
                    worse.append(i)
                return worker(l,worse,evals+evalsZ,A)
        best,rest, evals = worker(self.rows,[],0)
        return self.clone(best),self.clone(rest), evals
    def xpln(data, best, rest):
        def v(has):
            return value(has, len(best.rows), len(rest.rows), "best")

        def score(self,ranges):
            rule = self.RULE(ranges, maxSizes)
            if rule:
                oo(self.showRule(rule))
                bestr = self.selects(rule, best.rows)
                restr = self.selects(rule, rest.rows)
                if len(bestr) + len(restr) > 0:
                    return v({"best": len(bestr), "rest": len(restr)}), rule

        tmp = []
        maxSizes = {}
        # for ranges in bins(data.cols.x, {"best": best.rows, "rest": rest.rows}).values():
        for ranges in bins(data.cols.x, {"best": best.rows, "rest": rest.rows}):
            maxSizes[ranges[0]['txt']] = len(ranges)
            print("")
            for range in ranges:
                print(range['txt'], range['lo'], range['hi'])
                tmp.append({"range": range, "max": len(ranges), "val": v(range['y'].has)})
        rule, most = firstN(sorted(tmp, key=lambda x: x["val"], reverse=True), score)
        return rule, most

    def selects(self, rule, rows):
        def disjunction(ranges, row):
            for range in ranges:
                lo, hi, at = range["lo"], range["hi"], range["at"]
                x = row.cells[at]
                if x == "?":
                    return True
                if lo == hi and lo == x:
                    return True
                if lo <= x and x < hi:
                    return True
            return False

        def conjunction(row):
            # for ranges in rule:
            for ranges in rule.values():
                if not disjunction(ranges, row):
                    return False
            return True

        return list(filter(lambda r: r is not None, map(lambda r: r if conjunction(r) else None, rows)))

    def RULE(self,ranges, maxSize):
        t = {}
        for range in ranges:
            if range["txt"] not in t:
                t[range["txt"]] = []
            t[range["txt"]].append({"lo": range["lo"], "hi": range["hi"], "at": range["at"]})
        return prune(t, maxSize)

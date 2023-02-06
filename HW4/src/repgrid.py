
from src.data import Data
from src.globals import *
from src.num import NUM
from src.cols import Col

class repgrid:
    def repCols(self, cols):
        cols=copyDefined(cols)
        for i,col in enumerate(cols):
            col[len(col)-1]=col[0]+":"+col[len(col)-1]
            for j in range(1,len(col)):
                col[j-1]=col[j]
            col.pop()
        s = []
        for i in range(len(cols[0])):
            s.append("Num" + str(i))
        cols.insert(0,s)
        cols[0][len(cols[0])-1]="thingX"
        return Data(cols)
    
    def repRows(self,t, rows):
        rows = copyDefined(rows)
        for j,s in enumerate(rows[len(rows)-1]):
            rows[0][j] = rows[0][j]+":"+s
        rows.pop()
        for n,row in enumerate(rows):
            if n==0:
                row.append("thingX")
            else:
                u = t['rows'][len(t['rows'])- n]
                row.append(u[len(u)-1])
        return Data(rows)

    def repPlace(self,data):
        n,g = 20,[]
        for i in range(n+1):
            g.append([])
            for j in range(n):
                g[i].append(" ")
        maxy=0
        print("")
        for r,row in enumerate(data.rows):
            c=chr(65+r)
            print(c,row.cells[-1])
            x,y=row.x *n//1,row.y*n//1
            x=int(x)
            y=int(y)
            maxy = max(maxy,y+1)
            g[y][x]=c
        print("")
        for y in range(maxy):
            oo(g[y])

    def repGrid(self,sfile):
        t=dofile(sfile)
        rows=self.repRows(t,transpose(t.cols))
        cols=self.repCols(t.cols)
        show(rows.cluster)
        show(cols.cluster)
        self.repPlace(rows)






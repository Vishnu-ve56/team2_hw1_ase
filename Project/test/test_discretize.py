from src.data import Data
from src.discretization import *

class TestDiscretize:
    def testdiscretize(self):
        data = Data("../data/auto93.csv")
        best, rest = data.sway()

        print("all","","","",{'best':len(best.rows), 'rest':len(rest.rows)})

        for k,t in enumerate(bins(data.cols.x,{'best':best.rows, 'rest':rest.rows})):
            for _,range in enumerate(t):
                print(range['txt'],range['lo'],range['hi'], rnd(value(range['y'].has, len(best.rows),len(rest.rows),"best")), range['y'].has)
            print("")
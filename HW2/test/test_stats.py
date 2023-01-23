from src.globals import o,oo
from src.data import Data

class TestStats:
    def teststats(self):
        data = Data("../data/auto93.csv")
        xandy = {"y":data.cols.y, "x":data.cols.x}
        # print(xandy)
        for key in xandy:
            print(key, "mid", o(data.stats("mid",xandy[key],2)))
            print(" ","div",o(data.stats("div",xandy[key],2)))

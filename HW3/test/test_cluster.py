from src.data import Data
from src.globals import *

class TestCluster:
    def testcluster(self):
        data = Data("../data/auto93.csv")
        show(data.cluster(),"mid",data.cols.y,1)

        
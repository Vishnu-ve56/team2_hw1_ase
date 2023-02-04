from src.data import Data
from src.globals import *

class TestSway:
    def testsway(self):
        data = Data("../data/auto93.csv")
        show(data.sway(),"mid",data.cols.y,1)
from src.globals import *
from src.repgrid import repgrid

class TestRepGrid2:

    def testrepgrid2(self):
        rep=repgrid()
        rep.repGrid("data/repgrid1.csv")

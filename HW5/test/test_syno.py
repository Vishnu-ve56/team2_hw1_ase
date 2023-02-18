from src.globals import *
from src.repgrid import repgrid

class TestSyno:

    def testsyno(self):
        rep=repgrid()
        show(rep.repCols(dofile('data/repgrid1.csv')['cols']).cluster())
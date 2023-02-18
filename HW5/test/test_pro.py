from src.globals import *
from src.repgrid import repgrid

class TestPro:

    def testpro(self):
        rp=repgrid()
        t=dofile('data/repgrid1.csv')
        rows=rp.repRows(t,transpose(t['cols']))
        show(rows.cluster())


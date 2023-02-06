from src.globals import *
from src.repgrid import repgrid

class TestPos:

    def testpos(self):
        rep=repgrid()
        t=dofile('data/repgrid1.csv')
        rows = rep.repRows(t, transpose(t['cols']))
        rows.cluster()
        rep.repPlace(rows)
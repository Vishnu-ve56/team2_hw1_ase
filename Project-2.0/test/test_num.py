from src.num import NUM
from src.globals import *

class TestNum:

    def testnum(self):

        inp = [1,1,1,1,2,2,3]
        num = NUM()

        for i in inp:
            num.add(i)
        return 11/7 == num.mid() and rnd(num.div(),3) == 0.787

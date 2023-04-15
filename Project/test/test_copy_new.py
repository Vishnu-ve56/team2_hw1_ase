from src.globals import *
class TestCopy:
    def testcopy(self):
        t1={"a":1, "b":{"c":2, "d":[3]}}
        t2 = copyDefined(t1)
        t2["b"]["d"][0] = 1000
        print("b4",o(t1),"\nafter",o(t2))
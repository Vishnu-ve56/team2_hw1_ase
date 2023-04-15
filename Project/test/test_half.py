from src.data import Data
from src.globals import o

class TestHalf:
    def testhalf(self):
        data = Data("../data/auto93.csv")
        left, right, A, B, mid, c = data.half()
        print(len(left), len(right), len(data.rows))
        print(o(A.cells),c)
        print(o(mid.cells))
        print(o(B.cells))


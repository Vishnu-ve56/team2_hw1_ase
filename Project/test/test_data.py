from src.data import Data

class TestData:

    def testdata(self):
        data = Data("../data/auto93.csv")
        return (len(data.rows) == 398) and (data.cols.y[0].w == -1) and (data.cols.x[0].at == 0) and len(data.cols.x) == 4 # Difference Indices in Lua(starts from 1) hence different test case returns

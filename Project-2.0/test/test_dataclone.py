from src.data import Data


class TestClone:
    def testdataclone(self):
        data = Data("../data/auto93.csv")

        data2=data.clone(data.rows)

        return len(data.rows)==len(data2.rows) and (data.cols.y[0].w)==(data2.cols.y[0].w) and (data.cols.x[0].w)==(data2.cols.x[0].w) and len(data.cols.x)==len(data2.cols.x)


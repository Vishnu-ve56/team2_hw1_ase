from src.csv import csv

class TestCSV:

    def __init__(self, filename):
        self.fileName = filename
        self.n = 0
    def testcsv(self):
        cs = csv(self.fileName)
        cs.readFromCsv(self.fun)
        return self.n == 8*399

    def fun(self, t):
        self.n = self.n + len(t)



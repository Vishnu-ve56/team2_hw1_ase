from src.globals import coerce
import os

class csv:
    def __init__(self, fileName):
        self.fileName = fileName

    def readFromCsv(self, fun):
        currentWorkingPath = os.path.dirname(__file__)
        self.fileName = os.path.join(currentWorkingPath, self.fileName)
        with open(self.fileName, 'r') as file:
            for line in file:
                cols = line.split(",")
                parsedRow = []
                for col in cols:
                    parsedRow.append(coerce(col.rstrip("\n")))
                fun(parsedRow)



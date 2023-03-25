from src.data import Data
from src.globals import *

class TestSway:
    def testsway(self):
        data = Data("../data/auto93.csv")
        x, y = data.sway()
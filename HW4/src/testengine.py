from test.test_num import TestNum
from test.test_sym import TestSym
from test.test_rand import TestRand
from test.test_the import TestThe
from test.test_csvfile import TestCSV
from test.test_data import TestData
from test.test_stats import TestStats
from test.test_dataclone import TestClone
from test.test_around import TestAround
from test.test_half import TestHalf
from test.test_cluster import TestCluster
from test.test_sway import TestSway
from test.test_copy_new import TestCopy
from test.test_repgrid import TestrepCols

class testengine:
    def __init__(self,the):
        self.the = the
        self.help = ""
        self.fails=0
        self.testcases= {"sym":["check syms", TestSym().testsym],"num":["check nums", TestNum().testnum],"rand":["generate, reset, regenerate same",TestRand(self.the["seed"]).testrand],
        "the":["show settings",TestThe(self.the).testthe], "csv":["read from csv",TestCSV(self.the["file"]).testcsv],  "data":["read DATA csv",TestData().testdata], "stats": ["stats from DATA",TestStats().teststats], 
        "clone":["duplicate structure",TestClone().testdataclone], "around":["sorting nearest neighbors", TestAround().testaround], "half":["1-level bi-clustering",TestHalf().testhalf],
        "cluster":["N-Level bi-clustering", TestCluster().testcluster],
        "optimize":["semi-supervised optimization", TestSway().testsway]}
        self.testcases.clear()
        self.testcases["the"] = ["show settings",TestThe(self.the).testthe]
        self.testcases["copy"] = ["check copy", TestCopy().testcopy]
        self.testcases["num"] = ["check nums", TestNum().testnum]
        self.testcases["sym"] = ["check syms", TestSym().testsym]
        self.testcases["repcols"] = ["checking repcols cluster", TestrepCols().testrepcols]
        
    def concat(self, help):
        self.help+=help
        for i in self.testcases:
            self.help+=" -g  {0}\t{1}\n".format(i, self.testcases[i][0])
    def runtests(self):
        if(self.the["help"] == True):
            print(self.help)
            exit()
        for i in self.testcases:
            if self.the["go"].lower()=="all" or self.the["go"]==i:
                if self.testcases[i][1]()== False:
                    self.fails+=1
                    print("❌ fail:",i)
                else:
                    print("✅ pass:",i)
        print('\nNumber of failed tests: ', self.fails)

        
    
        



 
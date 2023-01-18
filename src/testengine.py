from test.test_num import TestNum
from test.test_sym import TestSym
from test.test_rand import TestRand
from test.test_the import TestThe
class testengine:
    def __init__(self,the):
        self.the = the
        self.help = ""
        self.fails=0
        self.testcases= {"sym":["check syms", TestSym().testsym],"num":["check nums", TestNum().testnum],"rand":["generate, reset, regenerate same",TestRand(self.the["seed"]).testrand],"the":["show settings",TestThe(self.the).testthe]}
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

        
    
        



 
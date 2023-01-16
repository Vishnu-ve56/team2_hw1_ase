from test.test_num import TestNum
from test.test_sym import TestSym


class testengine:
    def __init__(self):
        self.help = ""
        self.fails=0
        self.testcases= {"sym":["check syms", TestSym().testsym],"num":["check nums", TestNum().testnum]}
    def concat(self, help):
        self.help+=help
        for i in self.testcases:
            self.help+=" -g  {0}\t{1}\n".format(i, self.testcases[i][0])
    def runtests(self, the):
        print(the)
        if(the["help"] == True):
            print(self.help)
            exit()
        for i in self.testcases:
            if the["go"].lower()=="all" or the["go"]==i:
                if self.testcases[i][1]()== False:
                    self.fails+=1
                    print("❌ fail:",i)
                else:
                    print("✅ pass:",i)


        
    
        



 
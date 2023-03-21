
from test.test_stats import *

class testengine:
    def __init__(self):
        self.testcases= {"ok": test_ok, "num" : test_num, "sample" : test_sample, "gauss" : test_gaussian, "bootmu" : test_bootstrap, "basic" : test_basic,  "pre" : test_pre, "five" : test_five, "six" : test_six, "tiles" : test_tiles, "sk" : test_sk}
        self.fails = 0
    def runtests(self):
        for i in self.testcases:
            if self.testcases[i]()== False:
                self.fails+=1
                print("❌ fail:",i)
            else:
                print("✅ pass:",i)
        print('\nNumber of failed tests: ', self.fails)

        
    
        



 
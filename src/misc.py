from src.constants import getConstants
import re
import sys
from src.globals import coerce

class Misc:

    def __init__(self):
        self.help = getConstants('help')
        self.the = {}
        self.settings()
        self.cli()
        # self.check()
    
    def getThe(self):
        return self.the
    
    def getHelp(self):
        return self.help
        
    # def check(self):
    #     if self.the['help'] == True:
    #         print(self.help)
    #         exit()
    
    def settings(self):
        keyVals = re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", self.help)
        
        for vals in keyVals:
            self.the[vals[0]] = coerce(vals[1])
    
    
    # def coerce(self, s):
    #     def fun(s1):
    #         if s1.lower() == "true":
    #             return True
    #         elif s1.lower() == "false":
    #             return False
    #         return s1
    #     try:
    #         val = float(s)
    #         if(val == int(val)):
    #             val = int(val)
    #     except:
    #         val = fun(s.strip())
        
    #     return val  

    def cli(self):
        args = sys.argv
        args = args[1:]
        for key in self.the:
            strKey = str(key)
            strVal = str(self.the[key])
            for i in range(len(args)):
                if(args[i] == "-" + strKey[0] or args[i] == "-" + strKey):
                    strVal = strVal == "False" and "True" or strVal == "True" and "False" or args[i+1]
            
            # print(strVal)
            self.the[key] = coerce(strVal)
            # print(self.the[key])
        # print(self.the)
            
    

from test.test_xpln import TestXpln
from src.globals import *
from src.misc import Misc
from src.data import *
from tabulate import tabulate
from src.stats import *
import random



class testengine:
    def __init__(self,the):
        self.the = the
        self.help = ""
        self.fails=0
        
        self.testcases={}
        self.testcases["xpln"]=["explore explanation sets",TestXpln().testxpln]
    def concat(self, help):
        self.help+=help
        for i in self.testcases:
            self.help+=" -g  {0}\t{1}\n".format(i, self.testcases[i][0])
    def runtests(self):
        if(self.the["help"] == True):
            print(self.help)
            exit()
        misc=Misc()
        the=misc.getThe()
        count=0
        while count < the["n_iter"]:
            print("SHIT", count)
            data=Data(the['file'])

            # data2=handleMissingValues(the['file'],Data)
            best,rest,evals=data.sway()

            rule,_=data.xpln(best,rest)
            if rule!=-1:
                betterC,_=data.betters(len(best.rows))
                top_table['top']['data'].append(data.clone(betterC))
                top_table['xpln1']['data'].append(data.clone(data.selects(rule,data.rows)))
                top_table['xpln2']['data'].append(data.clone(data.selects(rule,data.rows)))
                top_table['all']['data'].append(data)
                top_table['sway1']['data'].append(best)
                top_table['sway2']['data'].append(best)
                top_table['all']['evals'] += 0
                top_table['sway1']['evals'] += evals
                top_table['sway2']['evals'] += evals
                top_table['xpln1']['evals'] += evals
                top_table['xpln2']['evals'] += evals
                top_table['top']['evals'] += len(data.rows)

                for i in range(len(bottom_table)):
                    [b,d],res =bottom_table[i]
                    if res==None:
                        bottom_table[i][1] = ['=' for _ in range(len(data.cols.y))]
                    for k in range(len(data.cols.y)):
                        if bottom_table[i][1][k] == '=':
                            y0, z0 = top_table[b]['data'][count].cols.y[k],top_table[d]['data'][count].cols.y[k]
                            y0Rows, z0Rows = top_table[b]['data'][count].rows, top_table[d]['data'][count].rows

                            y0vals = []
                            for rowY in y0Rows:
                                if len(y0vals) == the["Max"]:
                                    val = rint(0,511)
                                    print(val)    
                                    y0vals[val]  = rowY.cells[y0.at]
                                else:
                                    y0vals.append(rowY.cells[y0.at])

                            z0vals = []
                            for rowZ in z0Rows:
                                if len(z0vals) == the["Max"]:
                                    val = rint(0,511)
                                    print(val)
                                    z0vals[val]  = rowZ.cells[z0.at]
                                else:
                                    z0vals.append(rowZ.cells[z0.at])

                            print(len(y0vals),len(z0vals))
                            is_equal = cliffsDelta(y0vals, z0vals)
                            
                            if not is_equal:
                                bottom_table[i][1][k] = '≠'
                count+=1


        headers = [y.txt for y in data.cols.y]
        table = []
        for k,v in top_table.items():
            stats = [k] + [avgStat(v['data'],the['n_iter'])[y] for y in headers]
            stats += [v['evals']/the['n_iter']]
            table.append(stats)

        print(tabulate(table, headers=headers+["n_evals avg"],numalign="right"))
        print()

        table=[]
        for [base, diff], result in bottom_table:
            table.append([f"{base} to {diff}"] + result)
        print(tabulate(table, headers=headers,numalign="right"))

        for i in self.testcases:
            if self.the["go"].lower()=="all" or self.the["go"]==i:
                if self.testcases[i][1]()== False:
                    self.fails+=1
                    print("❌ fail:",i)
                else:
                    print("✅ pass:",i)









    


        
    
        



 
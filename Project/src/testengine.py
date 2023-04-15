# from test.test_num import TestNum
# from test.test_sym import TestSym
# from test.test_rand import TestRand
# from test.test_the import TestThe
# from test.test_csvfile import TestCSV
# from test.test_data import TestData
# from test.test_stats import TestStats
# from test.test_dataclone import TestClone
# from test.test_around import TestAround
# from test.test_half import TestHalf
# from test.test_cluster import TestCluster
# from test.test_sway import TestSway
# from test.test_copy_new import TestCopy
# from test.test_discretize import TestDiscretize
from test.test_xpln import TestXpln
from src.globals import *
from src.misc import Misc
from src.data import *
from tabulate import tabulate
from src.stats import *



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
                top_table['top']['data'].append(Data(data,betterC))
                top_table['xpln1']['data'].append(Data(data,data.selects(rule,data.rows)))
                top_table['xpln2']['data'].append(Data(data,data.selects(rule,data.rows)))
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
                            is_equal = bootstrap(y0.values(), z0.values()) and cliffsDelta(y0.values(), z0.values())
                            if not is_equal:
                                bottom_table[i][1][k] = '≠'
                count+=1

        # print("Die")
        # with open(the['file'].replace('/data', '/out').replace('.csv', '.out'), 'w') as outfile:
        #     headers = [y.txt for y in data.cols.y]
        #     table = []

        headers = [y.txt for y in data.cols.y]
        table = []
        print("Dead")
        for k,v in top_table.items():
            stats = [k] + [avgStat(v['data'],the['n_iter'])[y] for y in headers]
            stats += [v['evals']/the['n_iter']]
            table.append(stats)

        print(tabulate(table, headers=headers+["n_evals avg"],numalign="right"))
        print()
        # outfile.write(tabulate(table, headers=headers+["n_evals avg"],numalign="right"))
        # outfile.write('\n')

        # table=[]
        # for [base, diff], result in bottom_table:
        #     table.append([f"{base} to {diff}"] + result)
        # print(tabulate(table, headers=headers,numalign="right"))
        # outfile.write(tabulate(table, headers=headers,numalign="right"))

        for i in self.testcases:
            if self.the["go"].lower()=="all" or self.the["go"]==i:
                if self.testcases[i][1]()== False:
                    self.fails+=1
                    print("❌ fail:",i)
                else:
                    print("✅ pass:",i)









    


        
    
        



 
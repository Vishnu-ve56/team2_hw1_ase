
from test.test_xpln import TestXpln
from src.globals import *
from src.misc import Misc
from src.data import *
from tabulate import tabulate
from src.stats import *
import os



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
        means = []
        while count < the["n_iter"]:
            data=Data(the['file'])

            if(the["options"] == 1):
                best,rest,evals = data.sway()
                rule,_ = data.xpln(best,rest)
                txt1 = data.sway.__name__
                txt2 = data.xpln.__name__
                txt3 = the["min"]
            
            elif(the["options"] == 2):
                best,rest,evals = data.sway2()
                rule,_ = data.xpln(best,rest)
                txt1 = data.sway2.__name__
                txt2 = data.xpln.__name__
                txt3 = the["min"]
            
            elif(the["options"] == 3):
                best,rest,evals = data.sway2()
                rule,_ = data.xpln2(best,rest)
                txt1 = data.sway2.__name__
                txt2 = data.xpln2.__name__
                txt3 = the["min"]
            
            elif(the['options'] == 4):
                best,rest,evals = data.sway()
                rule,_ = data.xpln2(best,rest)
                txt1 = data.sway.__name__
                txt2 = data.xpln2.__name__
                txt3 = the["min"]

            elif(the["options"] == 5):
                best,rest,evals = data.sway1iter()
                rule,_ = data.xpln(best,rest)
                txt1 = data.sway1iter.__name__
                txt2 = data.xpln.__name__
                txt3 = the["min"]

            if rule!=-1:
                sta = {"mean": {} , "SD": {}}
                sta['mean'] = best.stats()
                sta['SD'] = best.stats("div")
                means.append(sta)

                betterC,_=data.betters(len(best.rows))
                top_table['top']['data'].append(data.clone(betterC))
                top_table['xpln']['data'].append(data.clone(data.selects(rule,data.rows)))
                top_table['all']['data'].append(data)
                top_table['sway']['data'].append(best)
                top_table['all']['evals'] += 0
                top_table['sway']['evals'] += evals
                top_table['xpln']['evals'] += evals
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
                                    val = rint(0,the["Max"]-1)    
                                    y0vals[val]  = rowY.cells[y0.at]
                                else:
                                    y0vals.append(rowY.cells[y0.at])

                            z0vals = []
                            for rowZ in z0Rows:
                                if len(z0vals) == the["Max"]:
                                    val = rint(0,the["Max"]-1)
                                    z0vals[val]  = rowZ.cells[z0.at]
                                else:
                                    z0vals.append(rowZ.cells[z0.at])

                            is_equal = cliffsDelta(y0vals, z0vals) and bootstrap(y0vals, z0vals)
                            
                            if not is_equal:
                                bottom_table[i][1][k] = 'neq'
                count+=1
                if the["options"] == 5:
                    the["n_iter"] = 1
                    
        currentWorkingPath = os.path.dirname(__file__)
        fileName = os.path.join(currentWorkingPath, the["file"])
        with open(fileName.replace('/data', '/out').replace('.csv', '.out'), 'a') as outfile:

            outfile.write("\n") 
            head = txt1 + " and " + txt2 + " for budget " + str(txt3) + '(the["min"])'

            outfile.write(head)

            outfile.write("\n")  
            headers = [y.txt for y in data.cols.y]
            table = []
        
            for k,v in top_table.items():
                stats = [k] + [avgStat(v['data'],the['n_iter'])[y] for y in headers]
                stats += [v['evals']/the['n_iter']]
                table.append(stats)

            print(tabulate(table, headers=headers+["n_evals avg"],numalign="right"))
            print()
            outfile.write(tabulate(table, headers=headers+["n_evals avg"],numalign="right"))
            outfile.write('\n')

            table=[]
            for [base, diff], result in bottom_table:
                table.append([f"{base} to {diff}"] + result)
            print(tabulate(table, headers=headers,numalign="right"))
            outfile.write(tabulate(table, headers=headers,numalign="right"))

            outfile.write("\n")
            for i in range(len(means)):
                outfile.write("\n")
                outfile.write(str(i) + "th iteration mean and sd:")
                outfile.write("\n")
                outfile.write("Mean: " + str(means[i]["mean"]))
                outfile.write("SD: " + str(means[i]["SD"]))
                outfile.write("\n")


            
            betterC,_=data.betters(80)
            
            outfile.write("\n")
            outfile.write("These are the 80 best ranks according to zitlers domination predicate for the whole dataset")
            outfile.write("\n")
            betterDict = []
            for i in betterC:
                bDict = {}
                outfile.write(str(i.cells))
                outfile.write("\n")
                for col in data.cols.y:
                    bDict[col.txt] = i.cells[col.at]

                betterDict.append(bDict) 
            statsDict = avgStat(top_table["sway"]["data"], the["n_iter"])

            flag = 1
            outfile.write("\n" + "This is the average of the best gotten from sway: " +str(statsDict) + "\n")
            for i in range(len(betterDict)):
                if(data.compareDicts(statsDict, betterDict[i])):
                    outfile.write("The rank with respect to the top 80 is here:(worst than how many from the top): " + str(i))
                    outfile.write("\n")
                    flag = 0
                    break
            
            if flag:
                    outfile.write("The rank with respect to the top 80 is 81, i.e it is worst than everything else")
                    outfile.write("\n")
            

            footer = "-" * 200
            outfile.write(footer)
            outfile.write("\n")











    


        
    
        



 
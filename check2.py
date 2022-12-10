import numpy

lowest = {"num":100, "u":None, "i":None, "o":None, "p":None, "per": None}
minmax = 100
for u in numpy.arange(0, minmax, 1):
    for i in  numpy.arange(0, minmax, 1):
        for o in range(0,minmax):
            for p in range(0,minmax):
                if(i != 0 and o != 0 and p != 0):
                    _ = abs((u/i)**(o/p)-1.6329931618554521799424605887)
                    if(_ <= lowest["num"]):
                        #if(_ == lowest["num"]):
                            #print(lowest, _,i,o,p)
                        lowest["num"] = _
                        lowest["u"] = u
                        lowest["i"] = ((i))
                        lowest["o"] = o
                        lowest["p"] = p
                        lowest["per"] = ((u/i)**(o/p)/1.6329931618554521799424605887)
        print("o over", ((u/i)))
print(lowest, lowest["num"]+1.6329931618554521799424605887, 1.6329931618554521799424605887)
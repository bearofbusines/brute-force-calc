import decimal
lowest = {"num": decimal.Decimal(100), "i": None, "o": None, "p": None}
decimal.getcontext().prec = 28
minmax = 143

for i in range(0, minmax):
    for o in range(0, minmax):
        for p in range(0, minmax):
            if (i != 0 and o != 0 and p != 0):
                _ = (decimal.Decimal(i)**(((decimal.Decimal(o)/decimal.Decimal(p)) -
                     decimal.Decimal(1.6329931618554521799424605887)))).copy_abs()
                if (_ <= lowest["num"]):
                    # if(_ == lowest["num"]):
                    #print(lowest, _,i,o,p)
                    lowest["num"] = _
                    lowest["i"] = i
                    lowest["o"] = o
                    lowest["p"] = p
    print("o over", i)
print(lowest, lowest["num"]+decimal.Decimal(1.6329931618554521799424605887),
      1.6329931618554521799424605887)

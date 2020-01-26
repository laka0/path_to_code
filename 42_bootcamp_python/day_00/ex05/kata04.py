t = (0, 4, 132.42222, 10000, 12345.67)

for i in t:
    if i >= 100 and i < 10000:
        print(round(i, 2))
    
    elif i >= 10000:
        print(format(i, ".2e"))
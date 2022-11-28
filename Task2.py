xp = [True, False]
yp = [True, False]
zp = [True, False] 

for i in range(2):
    xp[i]

for x in xp:
    for y in yp:
        for z in zp:
            print(x, y, z)
            result1 = not (x or y or z)
            result2 = (not x) and (not y) and (not z)
            print(result1 == result2)

f = open('C:/Users/Софья/Desktop/task1.py', 'r')
f = f.readlines()
f = list(map(lambda x: str(x)[:-1], f))
f = [int(x) for x in f]
res = []

for x in f:
    for y in f:
        for z in f:
            if (x + y + z) == 2020:
                res.append(x * y * z)
res = list(set(res)) 
with open('C:/Users/Софья/Desktop/result.py','w') as file:
    for x in res:
        file.write(str(x))
        file.write('\n')
file.close()


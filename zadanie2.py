s = input('Введите строку вида NdM, где:\nN - кол-во кубиков\nM - кол-во сторон одного кубика\n').split('d')

if len(s) != 2: 
	import sys
	sys.exit('Введите корректные данные')
if s[0].isnumeric() == False or s[1].isnumeric() == False:
	import sys
	sys.exit('Введите корректные данные')

n = int(s[0])
m = int(s[1])
l = [i+1 for i in range(m)] 
lol = [i+1 for i in range(n-1,n*m)]

from itertools import *

ss = [0]*(m**n)
prod = product (l, repeat = n)
o = 0
for i in prod:
   for j in range(n):
      ss[o] = ss[o]+int(i[j])
   
   o = o+1
i = 0
while i < m*n-(n-1):
	print (str(lol[i]) + ' = ' + str(round(ss.count(lol[i])*100/(m**n),2)) + '%')
	i += 1

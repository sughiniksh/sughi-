a,b=map(int,input().split(' '))
for s in range(a,b):
   if s > 1:
       for v in range(2,s):
           if (s % v) == 0:
               break
       else:
           print(s, end=' ')

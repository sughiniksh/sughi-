low = int(input(""))  
up = int(input(""))  
  
for n in range(low,up+ 1):  
   if n > 1:  
       for i in range(2,n):  
           if (n % i) == 0:  
               break  
       else:  
           print(n)  

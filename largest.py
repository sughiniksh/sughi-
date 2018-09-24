s1 = 10
s2 = 30
s3 = 20
if (s1 >= s2) and (s1 >= s3):
   largest = s1
elif (s2 >= s1) and (s2 >= s3):
   largest = s2
else:
   largest = s3
print("The largest number between",s1,",",s2,"and",s3,"is",largest)

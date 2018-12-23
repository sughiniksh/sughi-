user_input = input ("")
try:
   val = int(user_input)
   print("Yes")
except ValueError:
   print("no")

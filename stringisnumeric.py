user_input = input ("")
try:
   val = int(user_input)
   print("yes")
except ValueError:
   print("no")

num = input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('yes')
    else:
        print('no')
except ValueError:
    print(" Try Again !")

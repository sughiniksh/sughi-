def is_power_of_two(s):
    if s <= 0:
        return False
    else:
        return s & (s - 1) == 0
s = int(input(''))
if is_power_of_two(s):
    print('yes'.format(s))
else:
    print('no'.format(s))

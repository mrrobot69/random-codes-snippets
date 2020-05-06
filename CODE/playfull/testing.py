import math
pi_in = math.pi

numberofdecimals = int(input('how many places do you want?\n'))

print('pi is {:5.{}f}'.format(pi_in,numberofdecimals))

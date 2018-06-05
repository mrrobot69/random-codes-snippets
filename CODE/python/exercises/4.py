'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''

import math
q=[]
c=50
h=30
x=input()
n=x.split(',')
for d in n:
    Q=str(round(math.sqrt((2*c*int(d))/h)))
    q.append(Q)
print(','.join(q))

'''
The join() method returns a string concatenated with the elements of an iterable.
If the iterable contains any non-string values, it raises a TypeError exception.

The join() method provides a flexible way to concatenate string. It concatenates each element of an iterable (such as list, string and tuple) to the string and returns the concatenated string.

The syntax of join() is:

string.join(iterable)

.split()::
At some point, you may need to break a large string down into smaller chunks, or strings. This is the opposite of concatenation which merges or combines strings into one.

To do this, you use the split function. What it does is split or breakup a string and add the data to a string array using a defined separator.

If no separator is defined when you call upon the function, whitespace will be used by default. In simpler terms, the separator is a defined character that will be placed between each variable.

'''

'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that it 
is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

#################
#################

d={}

def sqr(i):
    for m in range(1,i+1):
        d[m]=m*m
    
i=int(input())
sqr(i)#call to above func.
print(d)

################
################

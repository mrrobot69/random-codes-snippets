def spam():
    global eggs   #this global call makes the egg variable global so whenever this function is called
                  #the var eggs is stored in memory 
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

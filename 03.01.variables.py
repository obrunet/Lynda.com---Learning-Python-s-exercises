#here is a little snippet showing the basics of variable usage

#declare a variable and initialize it
f=0
print (f)

#redeclaring a variable also works
f="abc"
g="defg"
print (f)

#you can't directly concatenate variables of different types, for instance here "this is a string" and "123" by using print("this is a string+123")
#instead use the "str" function for the conversion
print("this is a long string "+str(123))

#local vs. global variables
def someFunction ():   
    f="f in the function is a local variable"
    print(f)
    global g
    g="g in the function is a global var."
    print(g) 

someFunction()  #the local var. f and the global var. g are printed
print(f)        #the var. defined line 8 is printed (ie abc)
print(g)        #the global var. is printed not the one defined line 9

del f           #f is undefined / deleted -> print f would now return an error
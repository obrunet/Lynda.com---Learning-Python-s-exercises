#basic examples of working with functions

#definition of a simple func
def func1():
    print("function 1 is printed")

#func1               #the function is called which results in the printing of the string
print(func1())      #the function is passed like an argument or an object to an other function
print(func1)        #without () the function isn't called -> return an error because func1 isn't a var.
print("_______________________")


#a function with multiples arguments
def func2(arg1, arg2, arg3):
    print(arg1," ",arg2," ",arg3)

func2(10,20,30)
print(func2(40,50,60))  #also returns "none" because func2 doesn't retunr any value
print("_______________________")


#a function that returns a value
def cube(x):
    return (x*x*x)

print(cube (3))         #show the result of cube
print("_______________________")


#a function with default value for an argument
def power(num,x=1):
    result=1
    for i in range(x):
        result=result*num
    return result

print(power (3))           #by default 3^1
print(power (3,2))         #3^2=9
print(power (3,3))         #3^3=27    
print("_______________________")


#a function with multiples args
def multi_add(*args):
    result = 0
    for x in args:
        result = result+ x
    return result

print(multi_add ())        #by default 0
print(multi_add (1,2,3))   #1+2+3=6
print("_______________________")        

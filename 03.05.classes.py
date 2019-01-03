#woking with classes

#definition of a call with 2 methods
class myFirstClass ():
    def myMethod1 (self):
        print("this is method1 of my FirstClass")
    def myMethod2 (self, someString):
        print("this is method2" + someString)


class anotherClass ():
    def myMethod1 (self):
        myFirstClass.myMethod1(self)
        print("anotherClass method1")
    def myMethod2 (self, someString):
        print("anotherClass method2" + someString)


def main():
#useful for the 1st test / commented for the 2nd one    
#    c=myFirstClass()
#    c.myMethod1()
#    c.myMethod2(" and an other string")"

    c2=anotherClass()
    c2.myMethod1()
    c2.myMethod2(" a third string")


if __name__=="__main__":
    main()
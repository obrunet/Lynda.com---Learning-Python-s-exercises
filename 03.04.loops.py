#Few examples to show how to work with while and for loops

def main ():
    x = y = 0
    
    #while loop
    while (x<6):
        x = x+1
        print(x)
    print("________________")
    
    #for loop
    for y in range (5, 10):
        y = y+1
        print(y)
    print("________________")
   
    #use a loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for x in days:
        print(x)

    #use of break
    for y in range (5, 10):
        y = y+1
        print(y)
        if (y==7): break
    print("________________")

    #use of continue
    for y in range (5, 15):
        y = y+1
        if (y % 2 == 0): continue
        print(y)
    print("________________")

    #using the enumerate () function to get index
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for (x,i) in enumerate (months):
        print (x,i)

if __name__=="__main__":
    main()
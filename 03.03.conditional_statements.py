#working with conditional statements

def main():
    x, y = 1000, 100
    v, w = 800, 700
    
    #conditional flow with if, elif and else
    if (x<y):
        st="y is greater than x"
    elif (x==y):
        st="x and y are equal"
    else:
        st="y is less than x"
    print (st)
    
    #conditinal statement in one line
    print("v is less than w") if (v<w) else print("v>w")

if __name__=="__main__":
    main()
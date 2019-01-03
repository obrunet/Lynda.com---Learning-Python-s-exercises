#basic manipulation of files

#def main()

#open a file and create it if it doesn't exist (+), with write access
f=open("textfile.txt", "w+")
for i in range (1,10):
    f.write("this is line nb "+ str(i) + "\r")   #CRLFD
f.close()

#append the file with other lines
f=open("textfile.txt", "a")
for i in range (20,30):
    f.write("added line nb " + str(i) + "\r")
f.close

#reopen file to read it - 1st the whole file - 2nd line by line
f=open("textfile.txt", "r")
if f.mode=='r':                 #check if the file is successfully opened in read mode
#    print (f.read())            #print the content of the whole file in the debug console

    fl=f.readlines()
    for i in fl:
        print(i)
#How to manipulate os.path

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    ourFile="textfile.txt"

    #print the os name
    print(os.name)
    
    #check existence of the file and type
    print("The item exists: " + str(path.exists(ourFile)))
    print("The item is a file: " + str(path.isfile(ourFile)))
    print("The item is a directory: " + str(path.isdir(ourFile)))

    #retrieve the file paht - 2 different ways
    print("The item's path is: " + str(path.realpath(ourFile)))
    print("Item path and name:" + str(path.split(path.realpath(ourFile))))

    #get modification time
    print(time.ctime(path.getmtime(ourFile)))
    print(datetime.datetime.fromtimestamp(path.getmtime(ourFile)))

    #calculate how long ago the file was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been "+ str(td) + " since the file has been modified")
    print("Or, " + str(td.total_seconds()) + " seconds.")

if __name__=="__main__":
    main()

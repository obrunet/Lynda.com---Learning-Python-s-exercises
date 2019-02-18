#How to manipulate os.path

import os
from os import path
import shutil
from shutil import make_archive


def main():

    #duplicate an existing file
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")      #retrieve the path in the current dir
        dest = src + ".bak"                      #append extension .bak
        shutil.copy(src, dest)                   #copy only the content of the file
        shutil.copystat(src, dest)               #also copy metadata

    #rename the copy of the file
    os.rename("textfile.txt.bak", "textnewfile.txt")

    #create a TAR archive
    root_dir, tail = path.split(src)
    shutil.make_archive("textfile.archive", "tar", root_dir)


if __name__=="__main__":
    main()
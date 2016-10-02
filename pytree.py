#!/usr/bin/env python3
import subprocess
import sys
import os


# YOUR CODE GOES here
def printdir(path, padding, dir):
    dir_num = len(dir)
    dirs = os.listdir(path)
    files = []
    for fi in dirs:
        if not fi.startswith('.'):
            files.append(fi)
    file_num=len(files)
    for i in range(file_num):
        for k in range(dir_num):
            if(files[i] == dir[k]):
                print( padding+'├── ' + files[i])
                printdir(path+os.sep+dir[k], padding+'│   ', dir[k:])
            elif(i<k):
            	print(padding + '├── ' + files[i])
        if (i == file_num - 1):
            print(padding + '└── ' + files[i])
        elif(dir_num == 1):
            print(padding + '├── ' + files[i])


def tree(path, padding):
    files_n = []
    dirs_n = []
    root_n = []
    print('.')
    for root, dirs, files in os.walk(path):
        for f in files:
            if not f.startswith('.'):
                files_n.append(f)
        for d in dirs:
            if not d.startswith('.'):
                dirs_n.append(d)
    file_num=len(files_n)
    dir_num = len(dirs_n)
    printdir(path, padding, dirs_n)
    print('')
    print("%s directories, %s files" % (dir_num, file_num))



if __name__ == '__main__':
    # just for demo
    #subprocess.run(['tree'] + sys.argv[1:])

    if len(sys.argv)==1:
    	path = os.getcwd()
    	tree(path, '')
    elif len(sys.argv)==2:
        path = sys.argv[1]
        tree(path, '')
    else:
    	print("Wrong Input")

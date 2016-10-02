#!/usr/bin/env python3
import subprocess
import sys
import os


# YOUR CODE GOES here
def printdir(path, padding, dir):
    dir_num = len(dir)
    dirs = os.listdir(path)
    files = [x for x in os.listdir(path) if x[0] != '.']
    file_num = len(files)
    for i in range(file_num):
        for k in range(dir_num):
            if(files[i] == dir[k]):
                print(padding + '├── ' + files[i])
                printdir(path + os.sep + dir[k], padding + '│   ', dir[k:])
            elif(i < k):
                print(padding + '├── ' + files[i])
        if (i == file_num - 1):
            print(padding + '└── ' + files[i])
        elif(dir_num == 1):
            print(padding + '├── ' + files[i])


def countdir(dirs, dirs_n):
    for d in dirs:
        if not d.startswith('.'):
            dirs_n.append(d)
    return dirs_n


def tree(path):
    dirs_n = []
    file_n = []
    for root, dirs, files in os.walk(path):
        files_n = countdir(files, file_n)
        # file_num = file_num + len(files_n)
        dirs_n = countdir(dirs, dirs_n)
    dir_num = len(dirs_n)
    file_num = len(files_n)
    printdir(path, '', dirs_n)
    print('')
    print("%s directories, %s files" % (dir_num, file_num))


if __name__ == '__main__':
    # just for demo
    # subprocess.run(['tree'] + sys.argv[1:])
    print('.')
    if len(sys.argv) == 1:
        tree(os.getcwd())
    elif len(sys.argv) >= 2:
        path = sys.argv[1]
        tree(path)
    else:
        print('Wrong Input')

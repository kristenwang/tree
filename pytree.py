#!/usr/bin/env python3
import subprocess
import sys
import os
import re


# YOUR CODE GOES here
def printdir(path, padding):
    files = [x for x in os.listdir(path) if x[0] != '.']
    file_num = len(files)
    for i in range(file_num):
        if (i == file_num - 1):
            print(padding + '└── ' + files[i])
            sub_padding = '    '
        else:
            print(padding + '├── ' + files[i])
            sub_padding = '│   '
        if os.path.isdir(os.path.join(path, files[i])):
            path = os.path.join(path, files[i])
            printdir(path, padding + sub_padding)


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
        dirs_n = countdir(dirs, dirs_n)
    dir_num = len(dirs_n)
    file_num = len(files_n)
    printdir(path, '')
    print('')
    print("%s directories, %s files" % (dir_num, file_num))


if __name__ == '__main__':
    print('.')
    if len(sys.argv) == 1:
        path = os.getcwd()
    else:
        path = sys.argv[1]
    tree(path)

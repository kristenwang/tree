#!/usr/bin/env python3
import subprocess
import sys
import os
import re


# YOUR CODE GOES here
def printdir(path, padding):
    files = []
    files = filesort(path)
    file_num = len(files)
    for i in range(file_num):
        if i == file_num - 1:
            print(padding + '└── ' + str(files[i]))
            sub_padding = '    '
        else:
            print(padding + '├── ' + str(files[i]))
            sub_padding = '│   '
        if os.path.isdir(os.path.join(path, files[i])):
            path = os.path.join(path, files[i])
            printdir(path, padding + sub_padding)


def filesort(path):
    files = [f for f in os.listdir(path) if not f.startswith('.')]
    file_sort = sorted(files, key=lambda x: re.sub('[^A-Za-z0-9]+', '', x).lower())
    return file_sort


def countdir(dirs, dirs_n):
    dirs = [d for d in dirs if not d.startswith('.')]
    dirs_n = dirs_n + len(dirs)
    return dirs_n


def tree(path):
    dir_num = 0
    file_num = 0
    for root, dirs, files in os.walk(path):
        file_num = countdir(files, file_num)
        dir_num = countdir(dirs, dir_num)
    printdir(path, '')
    print('')
    print("%s directories, %s files" % (dir_num, file_num))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        path = os.getcwd()
        print('.')
    else:
        path = sys.argv[1]
        print(path)
    tree(path)

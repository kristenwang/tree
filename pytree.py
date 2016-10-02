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


def countdir(dirs, dir_n):
    names = []
    for d in dirs:
        if not d.startswith('.'):
            names.append(d)
    dir_n = len(names)
    return dir_n


def tree(path):
    dirs_num = 0
    files_num = 0
    for root, dirs, files in os.walk(path):
        file_num = countdir(files, files_num)
        files_num += file_num
        dir_num = countdir(dirs, dirs_num)
        dirs_num += dir_num
    printdir(path, '')
    print('')
    print("%s directories, %s files" % (dirs_num, files_num))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        path = os.getcwd()
        print('.')
    else:
        path = sys.argv[1]
        print(path)
    tree(path)

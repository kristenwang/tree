#!/usr/bin/env python3
import subprocess
import sys
import os
import re


# YOUR CODE GOES here
def printdir(path, padding):
    files = []
    files = filesort(path)
    for i, filename in enumerate(files):
        fullpath = path + "/" + filename
        if i == len(files) - 1:
            print(padding + '└── ' + str(filename))
            sub_padding = '    '
        else:
            print(padding + '├── ' + str(filename))
            sub_padding = '│   '
        if os.path.isdir(fullpath):
            printdir(fullpath, padding + sub_padding)


def filesort(path):
    files = [f for f in os.listdir(path) if not f.startswith('.')]
    file_sort = sorted(files, key=lambda x: re.sub('[^a-zA-Z0-9]+', '', x).lower())
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
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        dirs_num = dirs_num + len(dirs)
    printdir(path, '')
    print('')
    print(str(dirs_num) + ' directories, ' + str(files_num) + ' files')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        path = os.getcwd()
        print('.')
    else:
        path = sys.argv[1]
        print(path)
tree(path)

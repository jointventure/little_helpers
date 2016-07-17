#!/usr/bin/env python3
"""List all the files in a directory."""
import os


def walk(dirname):
    """Print the names of all files in dirname and its subdirectories.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            fout.write(os.path.join(root, filename))
            fout.write('\n')

try:
    fout = open('files.txt', 'w')
except:
    print('Something went wrong.')

walk('.')
fout.close()

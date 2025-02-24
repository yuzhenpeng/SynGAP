#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def filter(infile1, infile2, outfile):
    inf1 = open(infile1, 'r')
    inf2 = open(infile2, 'r')
    outf = open(outfile, 'w')
    list1 = inf1.read().split('\n')
    list2 = inf2.read().split('\n')
    for line in list1:
        if line != '' and line in list2:
            list2.remove(line)
    for line in list2:
        outf.write(line + '\n')
    inf1.close()
    inf2.close()
    outf.close()


if __name__ == '__main__':
    infile1 = sys.argv[1]
    infile2 = sys.argv[2]
    outfile = sys.argv[3]
    filter(infile1, infile2, outfile)

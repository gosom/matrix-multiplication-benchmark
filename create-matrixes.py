#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This script is copied from
http://martin-thoma.com/matrix-multiplication-python-java-cpp/
"""
import random
random.seed(1234)


def createRandomMatrix(n):
    maxVal = 1000
    matrix = []
    for _ in xrange(n):
        matrix.append([random.randint(0, maxVal) for el in xrange(n)])
    return matrix


def saveMatrix(matrixA, matrixB, f):
    #f = open(filename, 'w')
    for i, matrix in enumerate([matrixA, matrixB]):
        if i != 0:
            f.write("\n")
        for line in matrix:
            f.write("\t".join(map(str, line)) + "\n")


if __name__ == '__main__':
    import argparse, sys
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', default=3, type=int)
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
        default=sys.stdout)
    args = parser.parse_args()

    n = args.num
    matrixA = createRandomMatrix(n)
    matrixB = createRandomMatrix(n)
    saveMatrix(matrixA, matrixB, args.out)

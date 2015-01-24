#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This script is (almost) copied from
http://martin-thoma.com/matrix-multiplication-python-java-cpp/
"""
import argparse
import sys
import time

import dummy_matrix_mul


def read(f):
    lines = f.read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(map(int, line.split("\t")))
        else:
            matrix = B
    return A, B


def standardMatrixProduct(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=False,
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        help="input file with two matrices")
    parser.add_argument('-o', '--out', required=False,
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    parser.add_argument('-c', '--cpp', action='store_true')
    parser.add_argument('-s', '--size', type=int, required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = parse_args()

    A, B = read(args.input)

    start = time.time()
    if args.cpp:
        C = dummy_matrix_mul.standardMatrixProduct(A, B)
    else:
        C = standardMatrixProduct(A, B)
    elapsed = time.time() - start

    print >> sys.stderr, args.size, '\t', elapsed
    for line in C:
        print >> args.out, "\t".join(map(str, line))

#!/usr/bin/env python
from __future__ import print_function

"""
SYNOPSIS

    prime_factor.py [-h,--help] [-v,--verbose] [--version] -n <number>

DESCRIPTION
    prints the prime factors for any number

EXAMPLES

    prime_factor.py -n 10
    output: 2, 5

EXIT STATUS

    exit code : 0

AUTHOR

    Name <riteshb@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

VERSION

    $Id$
"""

import sys, os, traceback, optparse
import time
import math


# from pexpect import run, spawn

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def main(options, args):
    print("Number is {}".format(options.number))
    ret = find_factors(options.number)
    printTree(ret)
    print("")


def printTree(tree):
    if tree is None:
        return
    printTree(tree.left)
    print(tree.data, end=' ')
    printTree(tree.right)


def find_factors(number):
    trytill = int(math.sqrt(number))
    root = Tree()
    found = False
    for i in range(2, trytill):
        if (number % i) == 0:
            root.data = i
            root.right = find_factors(number / i)
            found = True
            break
    if not found:
        root.data = number
    return root


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'],
                                       version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option('-n', '--number', type='int', dest="number", help='number for which prime factors are needed')
        (options, args) = parser.parse_args()
        if options.verbose:
            print(time.asctime())
        main(options, args)
        if options.verbose:
            print(time.asctime())
            print('TOTAL TIME IN MINUTES:', end='')
            print((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
    except SystemExit as e:  # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)

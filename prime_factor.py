#!/usr/bin/env python
from __future__ import print_function

"""
SYNOPSIS

    prime_factor.py [-h,--help] [-v,--verbose] [--version] -n <number> -p

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
        self.number = None



def main(options, args):
    if options.triangle:
        l = 0
        triangle_term = 1
        p = None
        number = 0
        while l < options.triangle:
           number = triangle_term * (triangle_term +1)/2
           p = getFactors(number, False)
           l = len(p)
           triangle_term=triangle_term + 1
        print ("term number {} value {} {}".format(triangle_term - 1, number, p))
    else:
        print("Number is {}".format(options.number))
        print(sorted(getFactors(options.number, options.primes)))
    

def getFactors(number, primes):
    ret = find_factors(number, primes=primes)
    p=None
    if(primes):
        p = getPrimeFactors(ret)
        return p
    else:
        f,m = getPrimeFactorsAndMultiplicity(ret)
        results = []
        getAllFactors(f, m, 0, 1, results)
        return results


def getAllFactors(primeFactors, multiplicity, currentDivisor, currentResult, resultList):
    if currentDivisor == len(primeFactors):
        resultList.append(currentResult)
        return
    for i in range(0, multiplicity[currentDivisor] + 1):
        getAllFactors(primeFactors, multiplicity, currentDivisor + 1, currentResult, resultList)
        currentResult*=primeFactors[currentDivisor]


def getPrimeFactors(tree):
    if tree is None:
        return []
    listOfPrimeFactors = []
    listOfPrimeFactors.extend(getPrimeFactors(tree.left))
    listOfPrimeFactors.append(tree.data)
    listOfPrimeFactors.extend(getPrimeFactors(tree.right))

    return listOfPrimeFactors


def getPrimeFactorsAndMultiplicity(tree):
    listOfPrimeFactors = getPrimeFactors(tree)
    print(listOfPrimeFactors)
    listOfUniquePrimeFactors = []
    multiplicity = []
    prev = 0
    for i in range(0, len(listOfPrimeFactors)):
       if prev != listOfPrimeFactors[i]:
           listOfUniquePrimeFactors.append(listOfPrimeFactors[i])
           multiplicity.append(1)
           prev = listOfPrimeFactors[i]
       else:
           multiplicity[len(multiplicity) - 1] = multiplicity[len(multiplicity) - 1] + 1
    return listOfUniquePrimeFactors, multiplicity


def printTree(tree):
    if tree is None:
        return
    printTree(tree.left)
    print(tree.data, end=' ')
    printTree(tree.right)


def find_factors(number, primes=True):
    trytill = int(math.sqrt(number))
    root = Tree()
    root.number = number
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
        parser.add_option('-p', '--primes', action='store_true', default=False, help='prime factors only')
        parser.add_option('-n', '--number', type='int', dest="number", help='number for which prime factors are needed')
        parser.add_option('-t', '--triangle', type='int', dest="triangle", help='number for divisor')
        (options, args) = parser.parse_args()
        if options.verbose:
            print(time.asctime())
        if not options.number and not options.triangle:
            parser.print_help()
            sys.exit(1)
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

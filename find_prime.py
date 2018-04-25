#!/usr/bin/env python
from __future__ import print_function

"""
SYNOPSIS

    find_prime.py [-h,--help] [-v,--verbose] [--version] <-n <first_x_prime>> <-b number>

DESCRIPTION
    print the first x primes less than the number

EXAMPLES

    find_prime.py -n 2
    output: 2, 3
    find_prime.py -b 10
    output: 2, 3, 5, 7

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


# from pexpect import run, spawn

def main(options, args):
    i = 0
    prime_list = []
    num = 2
    while True:
        if isprime(num):
            i = i + 1
            prime_list.append(num)
            if options.number and i == options.number:
                print(prime_list)
                break

        num = num + 1
        if options.bound and num > options.bound:
            print(prime_list)
            sum_primes = 0
            for i in prime_list:
                sum_primes = sum_primes + i
            print("Sum is {}".format(sum_primes))
            break


def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

        # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'],
                                       version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option('-n', '--number', type='int', dest="number", help='first x number primes')
        parser.add_option('-b', '--bound', type='int', dest="bound", help='less than number')
        (options, args) = parser.parse_args()
        if options.verbose: print(time.asctime())
        if not options.number and not options.bound:
            parser.print_help()
            sys.exit(1)
        main(options, args)
        if options.verbose: print(time.asctime())
        if options.verbose: print('TOTAL TIME IN MINUTES:', end='')
        if options.verbose: print((time.time() - start_time) / 60.0)
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

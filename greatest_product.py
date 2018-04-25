#!/usr/bin/env python
from __future__ import print_function

"""
SYNOPSIS

    greatest_product.py [-h,--help] [-v,--verbose] [--version] -s <string>

DESCRIPTION
    print the largest palindrome using 2 n digit numbers

EXAMPLES

    prime_factor.py -d 2
    output: 9009 = 91 * 99

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
    # lets find all the strings with length = lstring and no 0's 
    l = list(options.istring)
    alllists = []
    curlist = []
    for i in range(0, len(l)):
        if l[i] != '0' and len(curlist) != options.lstring:
            curlist.append(int(l[i]))
            print(curlist)
        elif l[i] == '0':
            if len(curlist) == options.lstring:
                alllists.append(curlist[:])
            print("discarding", curlist)
            curlist = []
        else:
            print("adding", curlist)
            alllists.append(curlist[:])
            del curlist[0]
            curlist.append(int(l[i]))
    print(alllists)
    maxpr = 0
    for i in alllists:
        k = 1
        for j in i:
            k = k * j
        if maxpr <= k:
            maxpr = k
            res = i
    print(res, maxpr)


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'],
                                       version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option('-s', '--string', dest="istring", help='string')
        parser.add_option('-l', '--length', type='int', dest="lstring", help='length string')
        (options, args) = parser.parse_args()
        if options.verbose: print(time.asctime())
        if not options.istring and not options.lstring:
            print('Invalid input')
            sys.exit(0)
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
        traceback.print_exc()
        print(str(e))
        os._exit(1)

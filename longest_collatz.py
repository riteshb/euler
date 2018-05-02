#!/usr/bin/env python
from __future__ import print_function

"""
SYNOPSIS

    palindrome.py [-h,--help] [-v,--verbose] [--version] -d <digits>

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

import sys
import os
import traceback
import optparse
import time


def main(options, args):
    max_len = 0
    number = 0
    longest_seq = []
    for i in range(3,options.max_number+1):
        lc = get_collatz_sequence(i)
        if max_len <= len(lc):
            max_len = len(lc)
            number = i
            longest_seq = lc
    print("Number which produces longest seq {} length {} seq {}".format(number, max_len, longest_seq))


def get_collatz_sequence(number):
    lc = []
    val = number
    while val >1:
        if val%2 ==0:
            val=val/2
            lc.append(val)
        else:
            val=3*val + 1
            lc.append(val)
    return lc


def options_check(options, args, parser):
    if not options.max_number:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'],
                                       version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option('-m', '--max', type='int', dest="max_number", help='max number to start the collatz sequence')
        (options, args) = parser.parse_args()
        if options.verbose: print(time.asctime())
        options_check(options, args, parser)
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

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

import sys, os, traceback, optparse
import time


# from pexpect import run, spawn

def main(options, args):
    pass


def options_check(options, args):
    if not options.verbose:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'],
                                       version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option('-d', '--digits', type='int', dest="digit", help='digits in the numbers')
        (options, args) = parser.parse_args()
        if options.verbose: print(time.asctime())
        options_check(options, args)
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

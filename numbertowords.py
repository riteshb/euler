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


def main(options, args):
    total = 0
    for i in range(1,options.number + 1):
        print("{} - {}".format(i, numToWords(i)), end=' ')
        a=numToWords(i, join=False)
        print(a, end=' ')
        for j in a:
            total=total+len(j)
            print(j, len(j), total, end=' ')
        print("")
    print("\nTotal - {}".format(total))

def options_check(options, args, parser):
    if not options.number:
        parser.print_help()
        sys.exit(1)

def numToWords(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)/3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                if h>=1: 
                    words.append('and')
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if h>=1: 
                    words.append('and')
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: 
                    if h>=1:
                        words.append('and')
                    words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g])
    if join: return " ".join(words)
    return words


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'],
                                       version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option('-n', '--number', type='int', dest="number", help='number to word')
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

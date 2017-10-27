#!/usr/bin/python

import argparse
import os
import sys
import math

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('hashlen', metavar='N', type=int, nargs=1, help='Length of a hash function output in bits.\
                                                                                     Valid values: 64, 96, 128')
parser.add_argument('--input', default='0', help='File to be hashed. If no argument is provided data to be hashed is \
                                                                                    taken from the standard input.')
parser.add_argument('--output', default='0', help='File, where hash ouput will be saved. If no argument is provided \
                                                                                    digest is  written on standard output.')

args = parser.parse_args()
print('Length of a hash: {}'.format(args.hashlen))
print(args.input)
print(args.output)


def buffering(inputFile, indicator):
    inputFile.seek(indicator)
    data = inputFile.read((indicator + 8) - indicator)
    return data


def hashFunction(datum):
    datum = datum + bytes([2])
    return datum


data = None
output = args.output
if not args.output == '0':
    if os.path.isfile(args.output):
        output = open(args.output, 'w')
    else:
        print "There is no such file! as %s" % args.output
        sys.exit(0)

if not args.input == '0':
    if os.path.isfile(args.input): 
        inputFile = open(args.input, 'rb')
        indicator = 0
        size = os.path.getsize(args.input)

        for i in range(int(math.ceil(size/8))):
            data = buffering(inputFile, indicator)
            output.write(str(hashFunction(data)))
            indicator = indicator + 8
    else:
        print "There is no such file! as %s" % args.input
        sys.exit(0)
else:
    data = raw_input('Enter data to be hashed: ')

if output == '0':
    print(hashFunction(data))

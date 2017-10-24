#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')


parser.add_argument('hashlen', metavar='N', type = int, nargs = 1, help = 'Length of a hash function output in bits. Valid values: 64, 128, 256')
parser.add_argument('--input', default='0', help = 'File to be hashed. If no argument is provided data to be hashed is taken from the standard input.')
parser.add_argument('--output', default='0', help = 'File, where hash ouput will be saved. If no argument is provided digest is  written on standard output.')

args = parser.parse_args()
print('Length of a hash: {}'.format(args.hashlen))
print(args.input)
print(args.output)


def hashFunction ( datum ):
	datum = datum+'aaaa'
	return datum


data = None
output = args.output

if not args.input == '0':
	inputFile = open(args.input, 'r')
	data = inputFile.read()
else: 
	data = raw_input('Enter data to be hashed: ') 


if not args.output == '0': 
	output = open(args.output, 'w')


if output == '0':
	print (hashFunction(data))
else:
	output.write(hashFunction(data))


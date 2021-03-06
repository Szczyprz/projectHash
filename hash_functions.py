#!/usr/bin/python

import argparse
import os
import sys
import math

# parser = argparse.ArgumentParser(description='Process some integers.')
#
# parser.add_argument('hashlen', metavar='N', type=int, help='Length of a hash function output in bits. Valid values: 64, 128, 256')
# parser.add_argument('--input', default='0', help='File to be hashed. If no argument is provided data to be hashed is taken from the standard input.')
# parser.add_argument('--output', default='0', help='File, where hash ouput will be saved. If no argument is provided digest is  written on standard output.')
#
# args = parser.parse_args()
hashlen = 64
input_f = "a.txt"
output_f = "o.txt"

def hashFunctionLapa(datum):
    ascii=[]
    data_binary = bytearray(datum)
    for i in range(len(datum)):
        hashkey = i * 5
        ascii.append(data_binary[i-1] ^ hashkey)
    ascii_to_str = ''.join(map(chr, ascii))
    print ascii_to_str
    return ascii_to_str



def hash_p(data,k):
    data = bytearray(data)
    print bin(data[0])
    print
    s1 = [0, 0, 0, 0, 0, 0]
    s2 = [0, 0, 0]

    for i in range(len(data) - 2):
        s1[i] = data[i] & data[i+2]
        s1[i]=bin(s1[i])

    print "step 1"
    print s1

    for i in range(len(s1)):
        if s1[i] == 0:
            s1[i] = bin(int(s1[i-1],2) | i)

    j = 0
    for i in range(len(s1)-1):
        if i % 2 == 0:
            print j
            s2[j] = bin(int(s1[i],2) ^ int(s1[i+1],2))
            print s1[i]
            print s1[i + 1]
            j = j + 1
        else:
            continue

    print "step 2"
    print s2

    s2[0] = bin(int(s2[0],2) << 2)
    s2[1] = bin(int(s2[1], 2) >> 1)
    s2[2] = bin(int(s2[2], 2) << 3)

    print "step 3"
    print s2

    s3 = bin(int(s2[0],2) ^ int(s2[2],2))

    print "mod"
    print s3

    k = s3 and s2[1]

    print "hashkey"
    print k


    #print "output"

    ascii=[]
    data_binary = bytearray(data)
    for i in range(len(data)):
        hashkey = i * int(k,2);
        ascii.append(data_binary[i-1] ^ hashkey)
    ascii_to_str = ''.join(map(chr, ascii))
    print ascii_to_str
    return (ascii_to_str, k)



if hashlen not in [64, 128, 256]:
    print hashlen, " is not valid number for hash length"
    print "try 64, 128 or 256"
    sys.exit(1)

print('Length of a hash: {}'.format(hashlen))
print(input_f)
print(output_f)


def buffering(inputFile, indicator):
    inputFile.seek(indicator)
    data = inputFile.read((indicator + 8) - indicator)
    return data


def hashFunction(datum):
    datum = datum + bytes([2])
    return datum


data = None
output = output_f
k=0;
if not output_f == '0':
    # if os.path.isfile(output_f):
    output = open(output_f, 'w')
    # else:
    #     print "There is no such file! as %s" % output_f
    #     sys.exit(0)

if not input_f == '0':
    if os.path.isfile(input_f):
        inputFile = open(input_f, 'rb')
        indicator = 0
        size = os.path.getsize(input_f)

        for i in range(int(math.ceil(float(size) / 8))):
            data = buffering(inputFile, indicator)
            print data
            out, k = hash_p(data,k)
            output.write(out)
            indicator = indicator + 8
    else:
        print "There is no such file! as %s" % input_f
        sys.exit(0)
else:
    data = raw_input('Enter data to be hashed: ')

if output == '0':
    print(hashFunction(data))

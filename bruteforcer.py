import random
try:
    import sha3
except:
    print "You must install sha3 to use this. Run pip install pysha3 to install it. "
try:
    import argparse
except: 
    print "You must install argparse to use this. "
import sys

def findLowestHash(blockHash):
    start = random.randrange(0,999999999999999999999999999999999999999999999999999999999999999999999999999999999)       #big random range making it so multi-threading is easy. 
    lowest = (-1,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999L)       #just a big number
    try:
        while True:
            hashInt = int(sha3.sha3_256(blockHash + str(start)).hexdigest(), 16)
            if hashInt < lowest[1]:
                lowest = (start, hashInt)
    except:
        print "anceled Search. Search results are: "
        return (str(lowest[0]), str(lowest[1]))

parser = argparse.ArgumentParser()
parser.add_argument("blockhash")
args = parser.parse_args()

print "Press control C once in order to exit the program. "
print "The first part of the tuple is the number. The second part of the tuple is the hash"
print findLowestHash(args.blockhash)

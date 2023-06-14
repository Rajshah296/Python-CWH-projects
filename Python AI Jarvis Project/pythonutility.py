from ast import parse
from email import parser
from importlib import import_module
import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o =="mul" :
        return args.x * args.y
    elif args.o =="sub" :
        return args.x - args.y
    elif args.o =="div" :
        return args.x / args.y
    else : return "Something went wrong."
    
def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="Enter first number.This is a command line utility.Please contact Raj for more")
    parser.add_argument('--y',type=float,default=3.0,help="Enter second number.This is a command line utility.Please contact Raj for more")
    parser.add_argument('--o',type=str,default="add",help="This is a command line utility for calculation.Please contact Raj for more")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    
if __name__ == '__main__' : 
    main()

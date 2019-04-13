import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-input', type=str, help='input file', required=True)
parser.add_argument('-m', type=float, help='m', required=False)
parser.add_argument('-sig', type=float, help='sig', required=False)
args   = vars(parser.parse_args())
input = args['input']
m     = args['m']
sig   = args['sig']

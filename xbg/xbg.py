import argparse
import socket

parser = argparse.ArgumentParser(description='Use this tool to grab the banner from the specified target.')
parser.add_argument('t', metavar='IP', type=str, nargs='+',
                    help='TARGET IP')
parser.add_argument('p', metavar='PORT', type=int, nargs='+',
                    help='TARGET PORT')

args = parser.parse_args()
if args.t!=None and args.p!=None:
    bangrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bangrab.connect ((args.t[0], args.p[0]))
    print (bangrab.recv(4096))
    
else:
    print("-h, --help  show this help message and exit")

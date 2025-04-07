import argparse

parser = argparse.ArgumentParser(
    prog='argumentos2',
    description='Show top lines from each file')

parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
parser.add_argument('-t', '--texto', type=str, default='Ninguno')

args = parser.parse_args()

print(args)

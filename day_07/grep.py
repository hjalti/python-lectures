import argparse
import sys
import re
from collections import deque


def regex(string):
    try:
        return re.compile(string)
    except Exception as ex:
        raise argparse.ArgumentTypeError('Invalid regular expression\n%s' % ex.msg)

parser = argparse.ArgumentParser(description='Grep some stuff')
parser.add_argument('pattern', metavar='RE', type=regex, help='Regular expression')
parser.add_argument('input', metavar='N', type=argparse.FileType('r'), default=sys.stdin, nargs='?', help='Input')
parser.add_argument('-v', '--invert-match', default=False, action='store_true',  help='Select non-matching lines')
parser.add_argument('-c', '--count', default=False, action='store_true',  help='Count matching lines')
parser.add_argument('-o', '--only-matching', default=False, action='store_true',  help='Print only matched parts of matching lines')
parser.add_argument('-n', '--line-number', default=False, action='store_true',  help='Print each line of output with 1-based line number')
parser.add_argument('-C', '--context', type=int, metavar='NUM', default=0,  help='Print %(metavar)s lines of context (default: %(default)s)')

args = parser.parse_args()


def flush_cache(cache):
    if cache:
        print('--')
    for line in cache:
        output_line(*line)
    cache.clear()

def output_line(i, line, match=None):
    if args.count:
        return
    if args.line_number:
        print('%03d:' % i, end=' ')
    if match and args.only_matching:
        print(match.group())
    else:
        print(line, end='')

cache = deque(maxlen=args.context)

counter = 0
lines_after_match = 0

for i, line in enumerate(args.input):
    m = re.search(args.pattern, line)
    if (m and not args.invert_match) or (args.invert_match and not m):
        flush_cache(cache)
        lines_after_match = args.context
        output_line(i + 1, line, m)
        counter += 1
    elif not lines_after_match:
        cache.append( (i + 1, line) )
    else:
        output_line(i + 1, line)
        lines_after_match -= 1

if args.count:
    print(counter)

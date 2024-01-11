from sys import argv
from args import parse_args

if __name__ == '__main__':
    args = parse_args(args=argv[1:])
    # processor = build_processor(type=args['processor'])

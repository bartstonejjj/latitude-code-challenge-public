from fixed_width.convert_fwf_to_csv import FixedWidthToCSV
from argparse import ArgumentParser

if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--input_file')
    arg_parser.add_argument('--output_file')
    arg_parser.add_argument('--spec_file')
    args = vars(arg_parser.parse_args())
    FixedWidthToCSV(args['spec_file']).run(args['input_file'], args['output_file'])
from fixed_width.generate_fixed_width_file import generate_test_fwf
from fixed_width.helper import parse_spec_file
from argparse import ArgumentParser

if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--header', nargs='*', type = str)
    arg_parser.add_argument('--exclude_header')
    arg_parser.add_argument('--num_lines', type = int)
    arg_parser.add_argument('--offsets', nargs='*', type = int)
    arg_parser.add_argument('--encoding', default = 'utf-8')
    arg_parser.add_argument('--pad_char', default = ' ')
    arg_parser.add_argument('--output_file', default = 'output.txt')
    arg_parser.add_argument('--spec_file')

    args = vars(arg_parser.parse_args())

    if args['spec_file']:
        spec_file_args = parse_spec_file(args['spec_file'])
        new_args = {}
        new_args['header'] = spec_file_args['header']
        new_args['include_header'] = spec_file_args['include_header']
        new_args['num_lines'] = args['num_lines']
        new_args['offsets'] = spec_file_args['offsets']
        new_args['encoding'] = spec_file_args['output_encoding']
        new_args['pad_char'] = args['pad_char']
        new_args['output_file'] = args['output_file']
        args = new_args

    else :
        args['header'] = ','.join(args['header'])
        del args['spec_file']
        args['include_header'] = not args['exclude_header']
        del args['exclude_header']

    generate_test_fwf(**args)
from fixed_width.generate_fixed_width_file import generate_test_fwf
from fixed_width.convert_fwf_to_csv import FixedWidthToCSV
from fixed_width.helper import parse_spec_file

if __name__ == '__main__':

    # Config for end to end test
    fixed_width_file = 'fwf.txt'
    spec_file = 'fixed_width/spec.json'
    num_lines = 10
    pad_char = ' '
    output_file = 'tmp/output.csv'

    args = {}
    spec_file_args = parse_spec_file(spec_file)
    args['header'] = spec_file_args['header']
    args['include_header'] = spec_file_args['include_header']
    args['num_lines'] = num_lines
    args['offsets'] = spec_file_args['offsets']
    args['encoding'] = spec_file_args['output_encoding']
    args['pad_char'] = pad_char
    args['output_file'] = fixed_width_file

    generate_test_fwf(**args)

    FixedWidthToCSV(spec_file).run(fixed_width_file, output_file)
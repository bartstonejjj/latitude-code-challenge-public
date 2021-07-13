from argparse import ArgumentParser
from fixed_width.helper import parse_spec_file
import io

def generate_test_line(offsets, pad_char):
    return ''.join(['1' + pad_char * (offset - 1) for offset in offsets])

def generate_test_fwf(header, include_header, num_lines, offsets, encoding, pad_char, output_file):
    with io.open(output_file, mode='w', encoding = encoding, newline = None) as file:
        if include_header:
            file.write(header + '\n')
        line = generate_test_line(offsets, pad_char)
        for i in range(num_lines):
            file.write(line + '\n')


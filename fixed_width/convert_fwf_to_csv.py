import json
import csv
from fixed_width.iterate_columns import column_iter
from fixed_width.FileLineIterator import FileLineIterator 
from fixed_width.helper import parse_spec_file
from argparse import ArgumentParser

class FixedWidthToCSV():
    def __init__(self, spec_file, input_encoding = None, output_encoding = None):
        self.pad_char = ' '
        self.spec_file = parse_spec_file(spec_file)

    def set_input_encoding(self, input_encoding):
        self.spec_file['input_encoding'] = input_encoding

    def set_output_encoding(self, output_encoding):
        self.spec_file['output_encoding'] = output_encoding

    def run(self, input_file, output_file):
        input_file_iter = FileLineIterator(
            file = input_file, 
            include_header = self.spec_file['include_header'],
            encoding = self.spec_file['input_encoding'])

        with open(output_file, mode='w', encoding = self.spec_file['output_encoding'], newline = '') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            if self.spec_file['include_header']:
                writer.writerow(input_file_iter.header.split(','))
            
            for line in input_file_iter.data_line_iter():
                writer.writerow(list(column_iter(line = line, offsets = self.spec_file['offsets'], pad_char = self.pad_char)))
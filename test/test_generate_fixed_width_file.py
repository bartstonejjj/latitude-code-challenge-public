from fixed_width.generate_fixed_width_file import *
from encodings_python_36 import get_encodings
import os

offsets = [1,2,3]
pad_char = ' '

def test_generate_test_line():
    assert generate_test_line(offsets, pad_char) == '11 1  '

def test_generate_test_fwf():
    output_file = 'test.txt'
    encoding = 'utf-8'
    assert_var = False
    generate_test_fwf(
        header = 'a,b,c', 
        include_header = True,
        num_lines = 3, 
        offsets = offsets, 
        encoding = encoding, 
        pad_char = pad_char, 
        output_file = output_file)
    with open(output_file, 'r', encoding = encoding) as file:
        assert_var = file.read() == 'a,b,c\n11 1  \n11 1  \n11 1  \n'
    os.remove(output_file)
    assert assert_var

def working_encodings():
    not_working_encodings = [
    "cp65001" # only works on windows
    ]
    for encoding in get_encodings():
        if encoding not in not_working_encodings:
            yield encoding

def test_generate_test_fwf_with_all_encodings():
    for encoding in working_encodings():
        output_file = 'test.txt'
        encoding = encoding
        assert_var = False
        generate_test_fwf(
            header = 'a,b,c', 
            include_header = True,
            num_lines = 3, 
            offsets = offsets, 
            encoding = encoding, 
            pad_char = pad_char, 
            output_file = output_file)
        with open(output_file, 'r', encoding = encoding) as file:
            assert_var = file.read() == 'a,b,c\n11 1  \n11 1  \n11 1  \n'
        os.remove(output_file)
        assert assert_var
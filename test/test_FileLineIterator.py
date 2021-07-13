from fixed_width.FileLineIterator import FileLineIterator
from copy import deepcopy

import os
file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'twolines.txt')
# File contents (without |):
# |aa,b,cc|
# |1 23 |
# |5 78 |
encoding = 'windows-1252'
include_header = True

itr = FileLineIterator(file = file, include_header = include_header, encoding = encoding)
itr_no_header = deepcopy(itr)
itr_no_header.include_header = False

def test_get_header():
    assert itr.get_header() == 'aa,b,cc'
    assert itr_no_header.get_header() == None

def test_line_iter():
    li = itr.line_iter()
    assert next(li) == 'aa,b,cc'
    assert next(li) == '1 23 '
    assert next(li) == '5 78 '

def test_data_line_iter():
    dli = itr.data_line_iter()
    assert next(dli) == '1 23 '
    assert next(dli) == '5 78 '

def test_data_line_iter_no_header():
    dli_no_header = itr_no_header.data_line_iter()
    assert next(dli_no_header) == 'aa,b,cc'
    assert next(dli_no_header) == '1 23 '
    assert next(dli_no_header) == '5 78 '


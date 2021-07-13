from fixed_width.iterate_columns import *

offsets = [4, 3, 4]
pad_char = ' '
line = '  a  bbccc '

def test_padded_column_iter():
    pci = padded_column_iter(line, offsets)
    assert next(pci) == '  a '
    assert next(pci) == ' bb'
    assert next(pci) == 'ccc '

def test_get_pad_start_index():
    assert get_pad_start_index('1234   ', pad_char) == 4
    assert get_pad_start_index(' 2345     ', pad_char) == 5

def test_unpad_value():
    assert unpad_value('1234   ', pad_char) == '1234'
    assert unpad_value(' 2345     ', pad_char) == ' 2345'

def test_column_iter():
    pci = column_iter(line, offsets, pad_char)
    assert next(pci) == '  a'
    assert next(pci) == ' bb'
    assert next(pci) == 'ccc'
    assert list(column_iter(line, offsets, pad_char)) == ['  a', ' bb', 'ccc']

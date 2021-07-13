def padded_column_iter(line, offsets):
    last_index = 0
    for offset in offsets:
        yield line[last_index:last_index + offset]
        last_index += offset

def get_pad_start_index(chars, pad_char):
    for i, char in enumerate(reversed(chars)):
        if char != pad_char:
            return len(chars) - i

def unpad_value(chars, pad_char):
    return chars[:get_pad_start_index(chars, pad_char)]

def column_iter(line, offsets, pad_char):
    for padded_column in padded_column_iter(line, offsets):
        yield unpad_value(chars = padded_column, pad_char = pad_char)
from fixed_width.convert_fwf_to_csv import FixedWidthToCSV

import os
current_folder = os.path.dirname(os.path.realpath(__file__))

input_file = os.path.join(current_folder, 'twolines.txt')
# File contents (without |):
# |aa,b,cc|
# |1 23 |
# |5 78 |

spec_file = os.path.join(current_folder, 'test_spec.json')
# File contents:
# {
#     "ColumnNames":"f1, f2, f3",
#     "Offsets":"2,1,2",
#     "InputEncoding":"windows-1252",
#     "IncludeHeader":"True",
#     "OutputEncoding":"utf-8"
# }

output_file = 'test.csv'
fwtcsv = FixedWidthToCSV(spec_file)

def test_run_with_spec():
    FixedWidthToCSV(spec_file).run(input_file, output_file)
    assert_var = False

    with open(output_file, 'r', encoding = 'utf-8') as file:
        assert_var = file.read()
        assert assert_var == 'aa,b,cc\n1,2,3\n5,7,8\n'
    
    os.remove(output_file)
    assert assert_var

def run_and_read_output(input_encoding, output_encoding):
    fwtcsv.set_input_encoding(input_encoding)
    fwtcsv.set_output_encoding(output_encoding)
    fwtcsv.run(input_file, output_file)

    output = None
    with open(output_file, 'r', encoding = output_encoding) as file:
        output = file.read()
    os.remove(output_file)
    return output

def test_run():
    assert run_and_read_output(input_encoding = 'windows-1252', output_encoding = 'utf-8') \
        == 'aa,b,cc\n1,2,3\n5,7,8\n'

def test_run_with_encoding_combinations():
    # Can't ensure all input and output encoding combinations work, so only test these:
    encodings = \
    ['ascii',
     'big5',
     'big5hkscs',
     # 'cp037',
     # 'cp273',
     # 'cp424',
     'cp437',
     # 'cp500',
     # 'cp720',
     # 'cp737',
     'cp775',
     # 'cp850',
     # 'cp852',
     # 'cp855',
     # 'cp856',
     # 'cp857',
     # 'cp858',
     # 'cp860',
     # 'cp861',
     # 'cp862',
     # 'cp863',
     # 'cp864',
     # 'cp865',
     # 'cp866',
     # 'cp869',
     # 'cp874',
     # 'cp875',
     # 'cp932',
     # 'cp949',
     'cp950',
     'cp1006',
     # 'cp1026',
     # 'cp1125',
     # 'cp1140',
     'cp1250',
     'cp1251',
     'cp1252', # windows_1252
     'cp1253',
     'cp1254',
     'cp1255',
     'cp1256',
     'cp1257',
     'cp1258',
     # 'cp65001',
     'euc_jp',
     'euc_jis_2004',
     'euc_jisx0213',
     'euc_kr',
     'gb2312',
     'gbk',
     'gb18030',
     'hz',
     'iso2022_jp',
     'iso2022_jp_1',
     'iso2022_jp_2',
     'iso2022_jp_2004',
     'iso2022_jp_3',
     'iso2022_jp_ext',
     'iso2022_kr',
     'latin_1',
     'iso8859_2',
     'iso8859_3',
     'iso8859_4',
     'iso8859_5',
     'iso8859_6',
     'iso8859_7',
     'iso8859_8',
     'iso8859_9',
     'iso8859_10',
     'iso8859_11',
     'iso8859_13',
     'iso8859_14',
     'iso8859_15',
     'iso8859_16',
     'johab',
     'koi8_r',
     'koi8_t',
     'koi8_u',
     'kz1048',
     'mac_cyrillic',
     'mac_greek',
     'mac_iceland',
     'mac_latin2',
     'mac_roman',
     'mac_turkish',
     'ptcp154',
     'shift_jis',
     'shift_jis_2004',
     'shift_jisx0213',
     # 'utf_32',  
     # 'utf_32_be', 
     # 'utf_32_le',
     # 'utf_16',
     # 'utf_16_be',
     # 'utf_16_le', 
     'utf_7',
     'utf_8',
     'utf_8_sig']
    
    for input_encoding in encodings:
        for output_encoding in encodings:
            print('Testing input ouput encoding pair', input_encoding, output_encoding)
            assert run_and_read_output(input_encoding = input_encoding, output_encoding = output_encoding) \
                == 'aa,b,cc\n1,2,3\n5,7,8\n'

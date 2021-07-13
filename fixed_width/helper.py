import json

def parse_offsets(offsets):
	return [int(x) for x in offsets.replace(' ', '').split(',')]

def parse_spec_file(spec_file):
    spec = json.load(open(spec_file))
    ans = {}
    ans['header'] = spec['ColumnNames'].replace(' ', '')
    ans['include_header'] = spec['IncludeHeader']
    ans['input_encoding'] = spec['InputEncoding']
    ans['offsets'] = parse_offsets(spec['Offsets'])
    ans['output_encoding'] = spec['OutputEncoding']
    return ans
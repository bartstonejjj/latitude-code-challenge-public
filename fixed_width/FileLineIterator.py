import io
class FileLineIterator():
    def __init__(self, file, include_header, encoding):
        self.file = file
        self.include_header = include_header
        self.encoding = encoding
        self.header = self.get_header()

    def get_header(self):
        return next(self.line_iter()) if self.include_header else None

    def line_iter(self):
        with io.open(self.file, 'r', encoding = self.encoding, newline = None) as file:
            for line in file:
                yield line.replace('\n', '')

    def data_line_iter(self):
        itr = self.line_iter()
        if self.include_header:
            next(itr)
        for line in itr:
            yield line
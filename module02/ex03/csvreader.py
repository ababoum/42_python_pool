"""
Implement a context manager
"""


import sys
import time


class CsvReader():
    def __init__(
            self, filename=None, sep=',', header=False,
            skip_top=0, skip_bottom=0):
        # ... Your code here ...
        if not filename:
            print("You must provide a non-empty filename to CsvReader",
                  file=sys.stderr)
            self = None
            return None
        self.filename = filename
        self.sep = sep
        self.header = header
        self.first_index = skip_top
        self.last_index = - skip_bottom
        self.items_per_line = 0
        self.nb_lines = 0

    def __enter__(self):
        try:
            self.filestream = open(self.filename, 'r')
            if self.is_file_corrupted():
                return None
            # print(f'number of lines: {self.nb_lines}')
            return self
        except FileNotFoundError:
            print(f"No such file or directory: '{self.filename}'")
            self.filestream = None
            return None

    def __exit__(self, type, value, traceback):
        if self.filestream:
            self.filestream.close()

    def is_file_corrupted(self):
        if self.filestream:
            line = self.filestream.readline().strip('\n').split(self.sep)
            self.items_per_line = len(line)
            if line:
                self.nb_lines += 1
            while line:
                line = self.filestream.readline().strip('\n')
                if line:
                    self.nb_lines += 1
                    if len(list(filter(lambda x: len(x) > 0, line.split(self.sep)))) != self.items_per_line:
                        print(f"'{self.filename}' is corrupted")
                        return True
            self.filestream.seek(0)
            self.first_index += (0, 1)[self.header]
            self.last_index += self.nb_lines
        return False

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        if self.filestream:
            line_number = 1
            line = self.filestream.readline()
            while line_number < self.first_index:
                line = self.filestream.readline()
                line_number += 1
            ret = []
            while line and line_number < self.last_index:
                ret.append(line.split(self.sep))
                line = self.filestream.readline().strip('\n')
                line_number += 1
            return ret
        return None

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.filestream:
            line = self.filestream.readline().strip('\n').split(self.sep)
            self.items_per_line = len(line)
            if self.header:
                return [item for item in line]
        return None


if __name__ == "__main__":

    filename = sys.argv[1]
    with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")

    print("*******************************************")
    with CsvReader(filename, header=True, skip_top=17, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")
    print("*******************************************")
    with CsvReader(filename, header=True, skip_top=15, skip_bottom=1) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")
    print("*******************************************")
    with CsvReader(filename, header=True, skip_top=15, skip_bottom=2) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")
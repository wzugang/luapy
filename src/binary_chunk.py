from binary_reader import BinaryReader
from binary_chunk_header import BinaryChunkHeader
from prototype import Prototype


class BinaryChunk:
    def __init__(self, path):
        self.binary_reader = BinaryReader(path)
        self.header = BinaryChunkHeader(self.binary_reader)
        self.size_upvalues = self.binary_reader.read_uint8()
        self.main_func = Prototype(self.binary_reader, '')

    def print_header(self):
        self.header.dump()

    def check_header(self):
        self.header.check()

    def print_main_func(self):
        self.main_func.dump()

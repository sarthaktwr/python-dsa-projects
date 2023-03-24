from file_zipper import HuffmanCoding
import os

path = os.path.join(os.getcwd(), 'test.txt')
h = HuffmanCoding(path= path)
h.compress()
h.decompress(input_path = r'C:\PYTHON\learnings\python-dsa-projects\test.bin')
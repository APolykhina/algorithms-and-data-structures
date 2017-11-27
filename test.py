import unittest
import filecmp
import os
from solve import solve


class MyTest(unittest.TestCase):
    output_file = 'tmp.txt'

    def test_program_001(self):
        with open('input_data/001.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/001.txt', self.output_file, shallow=False))

    def test_program_002(self):
        with open('input_data/002.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/002.txt', self.output_file, shallow=False))

    def test_program_003(self):
        with open('input_data/003.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/003.txt', self.output_file, shallow=False))

    def test_program_004(self):
        with open('input_data/004.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/004.txt', self.output_file, shallow=False))

    def test_program_005(self):
        with open('input_data/005.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/005.txt', self.output_file, shallow=False))

    def test_program_006(self):
        with open('input_data/006.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/006.txt', self.output_file, shallow=False))

    def test_program_007(self):
        with open('input_data/007.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/007.txt', self.output_file, shallow=False))

    def test_program_008(self):
        with open('input_data/008.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/008.txt', self.output_file, shallow=False))

    def test_program_009(self):
        with open('input_data/009.docx', 'r') as Rfile, open(self.output_file, 'w') as Wfile:
            solve(Rfile, Wfile)
        self.assertTrue(filecmp.cmp('answer_data/009.txt', self.output_file, shallow=False))

    def tearDown(self):
        if os.path.isfile(self.output_file):
            os.remove(self.output_file)



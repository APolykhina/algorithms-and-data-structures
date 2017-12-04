import unittest
import filecmp
import os
from solve import solve


class MyTest(unittest.TestCase):
    output_file = 'tmp.txt'

    def test_program(self):
        for i in range(11):
            input_file = 'input_data/' + str(i+1) + '.docx'
            answer_file = 'answer_data/' + str(i+1) + '.txt'
            with open(input_file, 'r') as Rfile, open(self.output_file, 'w') as Wfile:
                solve(Rfile, Wfile)
            self.assertTrue(filecmp.cmp(answer_file, self.output_file, shallow=False))
            if os.path.isfile(self.output_file):
                os.remove(self.output_file)




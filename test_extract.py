import unittest
from unittest.mock import patch
import os
import extract

FILENAME = "test_pages.txt"

class ExtractTestCase(unittest.TestCase):

    def setUp(self):
        f = open(FILENAME, "w")
        f.close()

    def test_correct_test_pages(self):
        test_pages_list = []
        with open(FILENAME, "w") as file:
            for i in range(5):
                file.write(str(i)+" test"+"\n")
                test_pages_list.append(i)

        self.assertEqual(extract.get_page_numbers(FILENAME), test_pages_list,
                         'incorrect page numbers extracted')
    
    def test_incorrect_test_pages(self):
        with open(FILENAME, "w") as file:
            file.write("test")

        with self.assertRaises(ValueError):
            extract.get_page_numbers(FILENAME)
    
    @patch('builtins.input', return_value='2')
    @patch('extract.USER_INPUT', True)
    @patch('extract.PAGE_NUMS', FILENAME)
    def test_input_page_num(self, mock_input):
        name = "Test Plan"
        page_num = extract.get_page_num(0, [], name)

        self.assertEqual(page_num, 2)
        mock_input.assert_called_once_with("Enter page num of lighting page: ")

    @patch('extract.USER_INPUT', False)
    def test_non_input_page_num(self):
        name = "Test Plan"
        page_num = extract.get_page_num(2, [1,2,3,4], name)

        self.assertEqual(page_num, 3)


    def tearDown(self):
        os.remove(FILENAME)



if __name__ == "__main__":
    unittest.main()

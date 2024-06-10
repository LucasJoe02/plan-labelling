import unittest
import os
import extract

class ExtractTestCase(unittest.TestCase):
    def setUp(self):
        with open("test_pages.txt", "a") as file:
            for i in range(5):
                file.write(str(i)+" test"+"\n")

    def test_correct_test_pages(self):
        test_pages_list = [0,1,2,3,4]
        self.assertEqual(extract.get_page_numbers("test_pages.txt"), test_pages_list,
                         'incorrect page numbers extracted')

    def tearDown(self):
        os.remove("test_pages.txt")



if __name__ == "__main__":
    unittest.main()

import unittest
from fun_with_collections import sort_and_search_list

class MyTestCase( unittest.TestCase ):
    def test_item_found(self):
        self.assertEqual(sort_and_search_list.search_list(listA,9), x )


    def test_item_not_found(self):
        self.assertEqual(sort_and_search_list.search_list(listA,77), x)

listA = [4, 3, 5, 1, 9, 3, 8 ]

if __name__ == '__main__':
    unittest.main()

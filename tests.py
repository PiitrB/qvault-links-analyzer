import unittest
from report import remove_none_values
from report import sort_pages
from crawl import get_urls_from_string



class Tests(unittest.TestCase):
    def test_remove_none_values(self):
        self.assertEqual({}, remove_none_values({"1": None}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1", "2": None}))
        self.assertEqual({}, remove_none_values({}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1"}))

    def test_sort_pages(self):
        self.assertEqual([("first", 45),("second", 25),("third", 15)], sort_pages({"first": 45,"third": 15,"second": 25}))
        self.assertEqual([("first", 45),("second", 25),("third", 15)], sort_pages({"first": 45,"second": 25, "third": 15}))
        self.assertEqual([], sort_pages({}))
    
    def test_get_urls(self):
        self.assertEqual(["https://qvault.io"],get_urls_from_string('<html><body><a href="https://qvault.io"><span>Qvault></span></a></body></html>',"https://qvault.io"))
        self.assertEqual(["https://qvault.io", "https://wagslane.dev"],get_urls_from_string('<html><body><a href="https://qvault.io"><span>Qvault></span></a><a href="https://wagslane.dev"><span>Qvault></span></a></body></html>',"https://qvault.io"))


if __name__ == "__main__":
    unittest.main()
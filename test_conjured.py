#test_conjured.py
import unittest
from gilded_rose import Item, update_quality, CONJURED

class TestConjuredItem(unittest.TestCase):
    def test_conjured_degrades_twice_as_fast(self):
        item = Item(CONJURED, 0, 10)
        update_quality([item])
        self.assertEqual(6, item.quality)

if __name__ == '__main__':
    unittest.main()

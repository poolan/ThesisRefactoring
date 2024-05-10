import unittest
from gilded_rose import Item, update_quality

AGED_BRIE = "Aged Brie"

class TestAgedBrie(unittest.TestCase):
    def test_aged_brie_increases_quality(self):
        item = Item(AGED_BRIE, 0, 0)
        update_quality([item])
        self.assertEqual(2, item.quality)

if __name__ == "__main__":
    unittest.main()

import unittest
from gilded_rose import Item, update_quality

SULFURAS = "Sulfuras, Hand of Ragnaros"

class TestSulfuras(unittest.TestCase):
    def test_item_sulfuras_sell_in_doesnt_decrease(self):
        item = Item(SULFURAS, 1, 0)
        update_quality([item])
        self.assertEqual(1, item.sell_in)

    def test_item_sulfuras_quality_doesnt_decrease(self):
        item = Item(SULFURAS, 1, 80)
        update_quality([item])
        self.assertEqual(80, item.quality)

if __name__ == "__main__":
    unittest.main()

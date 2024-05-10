import unittest
from gilded_rose import Item, update_quality

AGED_BRIE = "Aged Brie"

class TestItem(unittest.TestCase):
    #initial test
    def test_item_doesnt_change_name(self):
        item = Item("foo", 0, 0)
        update_quality([item])
        self.assertEqual("foo", item.name)
    #All `items` have a `SellIn` value which denotes 
    #the number of days we have to sell the `items`
    def test_item_sell_in_decreases(self):
        item = Item("foo", 1, 0)
        update_quality([item])
        self.assertEqual(0, item.sell_in)
    #All `items` have a `Quality` value which 
    #denotes how valuable the item is
    def test_item_quality_decreases(self):
        item = Item("foo", 0, 1)
        update_quality([item])
        self.assertEqual(0, item.quality)
    #Once the sell by date has passed, 
    #'Quality' degrades twice as fast.
    def test_item_quality_degrades_twice_as_fast_after_sell_in(self):
        item = Item("foo", 0, 10)
        update_quality([item])
        self.assertEqual(8, item.quality)
    #The 'Quality' of an item is never negative
    def test_item_quality_is_never_negative(self):
        item = Item("foo", 0, 0)
        update_quality([item])
        self.assertEqual(0, item.quality)
    #The 'Quality' of an item is never more than '50'
    def test_item_quality_is_never_more_than_50(self):
        item = Item(AGED_BRIE, 0, 50)
        update_quality([item])
        self.assertEqual(50, item.quality)

    

if __name__ == "__main__":
    unittest.main()

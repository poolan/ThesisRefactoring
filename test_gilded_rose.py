# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, update_quality


class GildedRoseTest(unittest.TestCase):
    def test_item_doesnt_change_name(self):
        item = Item("foo", 0, 0)
        update_quality([item])
        self.assertEqual("foo", item.name)

        
if __name__ == '__main__':
    unittest.main()

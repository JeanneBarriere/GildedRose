# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, Product


class GildedRoseTest(unittest.TestCase):
    def test_deacrease_quality(self):
        item = Item("Bubble Gum", 2, 50)
        item.decrease_quality()
        self.assertEquals(49, item.quality)

    def test_deacrease_quality_equals_zero(self):
        item = Item("Item", 0, 0)
        item.decrease_quality()
        self.assertEquals(0, item.quality)

    def test_decrease_sellIn(self):
        item = Item("Item", 3, 50)
        item.decrease_sell_in()
        self.assertEquals(2, item.sell_in)

    def test_decrease_sellIn_equals_zero(self):
        item = Item("Item", 0, 50)
        item.decrease_sell_in()
        self.assertEquals(-1, item.sell_in)


if __name__ == '__main__':
    unittest.main()

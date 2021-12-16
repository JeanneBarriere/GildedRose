# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from texttest_fixture import texttest


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_start(self):
        result = "OMGHAI!-------- day 0 --------name, sellIn, quality+5 Dexterity Vest, 10, 20Aged Brie, 2, 0Elixir of the Mongoose, 5, 7Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 15, 20Backstage passes to a TAFKAL80ETC concert, 10, 49Backstage passes to a TAFKAL80ETC concert, 5, 49Conjured Mana Cake, 3, 6-------- day 1 --------name, sellIn, quality+5 Dexterity Vest, 9, 19Aged Brie, 1, 1Elixir of the Mongoose, 4, 6Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 14, 21Backstage passes to a TAFKAL80ETC concert, 9, 50Backstage passes to a TAFKAL80ETC concert, 4, 50Conjured Mana Cake, 2, 5"
        assert result == texttest()


if __name__ == '__main__':
    unittest.main()

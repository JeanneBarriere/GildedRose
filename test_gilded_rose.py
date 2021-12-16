# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from texttest_fixture import golden_test_two_days
from texttest_fixture import golden_test_ten_days

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        
    def test_Backstage_less_than_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality_part_2()
        self.assertEquals(3, items[0].quality)
        
    def test_Backstage_less_than_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality_part_2()
        self.assertEquals(2, items[0].quality)

    def test_two_days(self):
        result = "OMGHAI!-------- day 0 --------name, sellIn, quality+5 Dexterity Vest, 10, 20Aged Brie, 2, 0Elixir of the Mongoose, 5, 7Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 15, 20Backstage passes to a TAFKAL80ETC concert, 10, 49Backstage passes to a TAFKAL80ETC concert, 5, 49Conjured Mana Cake, 3, 6-------- day 1 --------name, sellIn, quality+5 Dexterity Vest, 9, 19Aged Brie, 1, 1Elixir of the Mongoose, 4, 6Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 14, 21Backstage passes to a TAFKAL80ETC concert, 9, 50Backstage passes to a TAFKAL80ETC concert, 4, 50Conjured Mana Cake, 2, 5"
        assert result == golden_test_two_days()

    def test_ten_days(self):
        result = "OMGHAI!-------- day 0 --------name, sellIn, quality+5 Dexterity Vest, 10, 20Aged Brie, 2, 0Elixir of the Mongoose, 5, 7Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 15, 20Backstage passes to a TAFKAL80ETC concert, 10, 49Backstage passes to a TAFKAL80ETC concert, 5, 49Conjured Mana Cake, 3, 6-------- day 1 --------name, sellIn, quality+5 Dexterity Vest, 9, 19Aged Brie, 1, 1Elixir of the Mongoose, 4, 6Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 14, 21Backstage passes to a TAFKAL80ETC concert, 9, 50Backstage passes to a TAFKAL80ETC concert, 4, 50Conjured Mana Cake, 2, 5-------- day 2 --------name, sellIn, quality+5 Dexterity Vest, 8, 18Aged Brie, 0, 2Elixir of the Mongoose, 3, 5Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 13, 22Backstage passes to a TAFKAL80ETC concert, 8, 50Backstage passes to a TAFKAL80ETC concert, 3, 50Conjured Mana Cake, 1, 4-------- day 3 --------name, sellIn, quality+5 Dexterity Vest, 7, 17Aged Brie, -1, 4Elixir of the Mongoose, 2, 4Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 12, 23Backstage passes to a TAFKAL80ETC concert, 7, 50Backstage passes to a TAFKAL80ETC concert, 2, 50Conjured Mana Cake, 0, 3-------- day 4 --------name, sellIn, quality+5 Dexterity Vest, 6, 16Aged Brie, -2, 6Elixir of the Mongoose, 1, 3Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 11, 24Backstage passes to a TAFKAL80ETC concert, 6, 50Backstage passes to a TAFKAL80ETC concert, 1, 50Conjured Mana Cake, -1, 1-------- day 5 --------name, sellIn, quality+5 Dexterity Vest, 5, 15Aged Brie, -3, 8Elixir of the Mongoose, 0, 2Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 10, 25Backstage passes to a TAFKAL80ETC concert, 5, 50Backstage passes to a TAFKAL80ETC concert, 0, 50Conjured Mana Cake, -2, 0-------- day 6 --------name, sellIn, quality+5 Dexterity Vest, 4, 14Aged Brie, -4, 10Elixir of the Mongoose, -1, 0Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 9, 27Backstage passes to a TAFKAL80ETC concert, 4, 50Backstage passes to a TAFKAL80ETC concert, -1, 0Conjured Mana Cake, -3, 0-------- day 7 --------name, sellIn, quality+5 Dexterity Vest, 3, 13Aged Brie, -5, 12Elixir of the Mongoose, -2, 0Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 8, 29Backstage passes to a TAFKAL80ETC concert, 3, 50Backstage passes to a TAFKAL80ETC concert, -2, 0Conjured Mana Cake, -4, 0-------- day 8 --------name, sellIn, quality+5 Dexterity Vest, 2, 12Aged Brie, -6, 14Elixir of the Mongoose, -3, 0Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 7, 31Backstage passes to a TAFKAL80ETC concert, 2, 50Backstage passes to a TAFKAL80ETC concert, -3, 0Conjured Mana Cake, -5, 0-------- day 9 --------name, sellIn, quality+5 Dexterity Vest, 1, 11Aged Brie, -7, 16Elixir of the Mongoose, -4, 0Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 6, 33Backstage passes to a TAFKAL80ETC concert, 1, 50Backstage passes to a TAFKAL80ETC concert, -4, 0Conjured Mana Cake, -6, 0"
        assert result == golden_test_ten_days()


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import unittest

from gilded_rose import AgedBrie, Backstage


class GildedRoseTest(unittest.TestCase):
    def test_decrease_sell_in_Backstage(self):
        item = Backstage(10, 10)
        item.decrease_sell_in()
        self.assertEquals(9, item.sell_in)

    def test_increase_quality(self):
        item = Backstage(10, 10)
        item.increase_quality()
        self.assertEquals(11, item.quality)
        item = Backstage(10, 50)
        item.increase_quality()
        self.assertEquals(50, item.quality)
        
    def test_decrease_sell_in_aged_brie_sell_in_positive(self):
        item = AgedBrie(3, 12)
        item.decrease_sell_in()
        self.assertEquals(2, item.sell_in)

    def test_increase_quality_aged_brie_sell_in_positive(self):
        item = AgedBrie(3, 12)
        item.increase_quality()
        self.assertEquals(13, item.quality)
        
    def test_increase_quality_aged_brie_quality_max(self):
        item = AgedBrie(3, 50)
        item.increase_quality()
        self.assertEquals(50, item.quality)
        
    def test_increase_quality_aged_brie_sell_in_zero(self):
        item = AgedBrie(0, 12)
        item.increase_quality()
        self.assertEquals(13, item.quality)
    
    def test_increase_quality_aged_brie_sell_in_negative(self):
        item = AgedBrie(-1, 12)
        item.increase_quality()
        self.assertEquals(14, item.quality)
        
    def test_increase_quality_aged_brie_sell_in_negative_max(self):
        item = AgedBrie(-1, 49)
        item.increase_quality()
        self.assertEquals(50, item.quality)
    


if __name__ == '__main__':
    unittest.main()

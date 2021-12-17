# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.sell_in = self.sell_in-1
        self.quality = (self.quality, self.quality-1)[self.quality > 0]
        self.quality = (self.quality, self.quality-1)[self.sell_in < 0]

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    

class Backstage (Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def increase_quality(self):
        self.quality = self.quality + 1

    def increase_quality_under_eleven(self):
        self.quality = self.quality + 2

    def increase_quality_under_six(self):
        self.quality = self.quality + 3

    def decrease_quality_equals_zero(self):
        self.quality = 0

    def decrease_sell_in(self):
        self.sell_in = self.sell_in-1

    def update_quality(self):
        self.decrease_sell_in()
        if self.sell_in < 0:
            self.decrease_quality_equals_zero()
        elif self.sell_in < 6:
            self.increase_quality_under_six()
        elif self.sell_in < 11:
            self.increase_quality_under_eleven()


class Sulfura (Item):
    def __init__(self, sell_in):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, 80)

    def update_quality(self):
        return


class AgedBrie (Item):
    def __init__(self, sell_in, quality):
        super().__init__("AgedBrie", sell_in, quality)
        self.name = "Aged Brie"

    def decrease_sell_in(self):
        self.sell_in = self.sell_in-1

    def increase_quality(self):
        if self.quality == 50:
            return
        self.quality = self.quality + ((1, 2)[self.sell_in < 0])

    def update_quality(self):
        self.decrease_sell_in()
        self.increase_quality()

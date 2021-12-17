# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
                item.decrease_quality()
            else:
                item.increase_quality()
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 6:
                        item.increase_quality()
                    if item.sell_in < 11:
                        item.increase_quality()

    # deuxième partie

    def update_quality_part_2(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.decrease_sell_in()
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.decrease_quality()
                    else:
                        item.quality = 0
                else:
                    item.increase_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality-1

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality+1

    def decrease_sell_in(self):
        self.sell_in = self.sell_in-1

    def increase_sell_in(self):
        self.sell_in = self.sell_in+1

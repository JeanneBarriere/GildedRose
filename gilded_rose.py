class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class ItemFactory(object) :
    def create(self, name, sell_in, quality):
        if name == "Sulfuras, Hand of Ragnaros": return Sulfuras(sell_in)
        if name == "Backstage passes to a TAFKAL80ETC concert": return Backstage(sell_in, quality)
        if name == "Aged Brie": return AgedBrie(sell_in, quality)
        if name == "Conjured Mana Cake": return Conjured(sell_in, quality)
        else:
            return Item(name, sell_in, quality)


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.sell_in = self.sell_in-1
        self.quality = (self.quality, self.quality-1)[self.quality > 0]
        self.quality = (self.quality, self.quality-1)[self.sell_in < 0 and self.quality > 0]

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    

class Backstage (Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def increase_quality(self):
        self.quality = self.quality + 1
        self.quality = (self.quality,50) [self.quality > 50]

    def decrease_sell_in(self):
        self.sell_in = self.sell_in-1

    def update_quality(self):
        if self.quality < 50:
            self.increase_quality()
        if self.sell_in < 11:
            self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()
        self.decrease_sell_in()
        self.quality = ( self.quality, 0) [self.sell_in < 0]
            
        
        
class Sulfuras (Item):
    def __init__(self, sell_in):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, 80)

    def update_quality(self):
        return


class AgedBrie (Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def decrease_sell_in(self):
        self.sell_in = self.sell_in-1

    def increase_quality(self):
        self.quality = self.quality + ((1, 2)[self.sell_in < 0])
        self.quality = (self.quality,50) [self.quality > 50]

    def update_quality(self):
        self.decrease_sell_in()
        self.increase_quality()

class Conjured (Item):
    def __init__(self, sell_in, quality):
        super().__init__("Conjured Mana Cake", sell_in, quality)

    def update_quality(self):
        self.sell_in = self.sell_in-1
        self.quality = (self.quality, self.quality-2)[self.quality > 0]
        self.quality = (self.quality, self.quality-2)[self.sell_in < 0 and self.quality > 0]

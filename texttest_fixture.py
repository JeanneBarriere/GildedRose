# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *


def golden_test_two_days():

    result = ""
    result = result + "OMGHAI!"
    item = ItemFactory()
    items = [
             item.create(name="+5 Dexterity Vest", sell_in=10, quality=20),
             item.create(name="Aged Brie", sell_in=2, quality=0),
             item.create(name="Elixir of the Mongoose", sell_in=5, quality=7),
             item.create(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             item.create(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             item.create(name="Conjured Mana Cake", sell_in=3, quality=6), 
            ]
    
    days = 2
    for day in range(days):

        result = result+"-------- day "+str(day)+" --------"
        result = result + "name, sellIn, quality"
        for item in items:
            result = result+str(item)
        GildedRose(items).update_quality()

    return result

def golden_test_ten_days():

    result = ""
    result = result + "OMGHAI!"
    item = ItemFactory()
    items = [
        item.create(name="+5 Dexterity Vest", sell_in=10, quality=20),
        item.create(name="Aged Brie", sell_in=2, quality=0),
        item.create(name="Elixir of the Mongoose", sell_in=5, quality=7),
        item.create(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        item.create(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        item.create(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=15, quality=20),
        item.create(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=10, quality=49),
        item.create(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=5, quality=49),
        item.create(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 10
    for day in range(days):

        result = result+"-------- day "+str(day)+" --------"
        result = result + "name, sellIn, quality"
        for item in items:
            result = result+str(item)
        GildedRose(items).update_quality()

    return result
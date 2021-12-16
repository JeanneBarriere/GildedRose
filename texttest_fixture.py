# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *


def golden_test_two_days():

    result = ""
    result = result + "OMGHAI!"
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 2
    for day in range(days):

        result = result+"-------- day "+str(day)+" --------"
        result = result + "name, sellIn, quality"
        for item in items:
            result = result+str(item)
        GildedRose(items).update_quality()
        GildedRose(items).update_quality_part_2()

    return result

def golden_test_ten_days():

    result = ""
    result = result + "OMGHAI!"
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 10
    for day in range(days):

        result = result+"-------- day "+str(day)+" --------"
        result = result + "name, sellIn, quality"
        for item in items:
            result = result+str(item)
        GildedRose(items).update_quality()
        GildedRose(items).update_quality_part_2()

    return result
# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def is_brie(self, item):
        return item.name == "Aged Brie"

    def is_backstage(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"
    
    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1
    
    def decrease_quality(self, item):
        if item.quality > 0:
            if not self.is_sulfuras(item):
                item.quality = item.quality - 1
    
    def handle_brie(self, item):
        self.increase_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.increase_quality(item)
    
    def handle_backstage(self, item):
        self.increase_quality(item)
        if item.sell_in < 11:
            self.increase_quality(item)
        if item.sell_in < 6:
            self.increase_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0
    
    def handle_others(self, item):
        self.decrease_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item)
        

    def update_quality(self):
        for item in self.items:
            if self.is_sulfuras(item):
                continue
            elif self.is_brie(item):
                self.handle_brie(item)
            elif self.is_backstage(item):
                self.handle_backstage(item)
            else:
                self.handle_others(item)


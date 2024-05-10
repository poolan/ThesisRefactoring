from typing import Iterable

# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single_item(item)

def update_quality_single_item(item: Item):
        if item.name != SULFURAS:
            item.sell_in = item.sell_in - 1
        if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
            if item.quality > 0:
                if item.name != SULFURAS:
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == BACKSTAGE_PASSES:
                    if item.sell_in < 10:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 5:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE_PASSES:
                    if item.quality > 0:
                        if item.name != SULFURAS:
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1



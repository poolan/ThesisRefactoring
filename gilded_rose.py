from typing import Iterable, Protocol

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
    
def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(0, item.quality - amount)

def increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    item.quality = min(max_quality, item.quality + amount)

def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single_item(item)

class ItemUpdater(Protocol): 
    def update_quality(self, item: Item) -> None:
        ...
    def update_sell_in(sel, item: Item) -> None:
        ...

class DefaultItemUpdater:
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item)
        if item.sell_in < 0:
            decrease_item_quality(item)

class AgedBrieUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 0:
            increase_item_quality(item)
        
class BackStagePassesUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        if item.sell_in < 10:
            increase_item_quality(item)
        if item.sell_in < 5: 
            increase_item_quality(item)
        if item.sell_in < 0:
            item.quality = 0

class SulfurasUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        pass

    def update_sell_in(self, item: Item) -> None:
        pass


def update_quality_single_item(item: Item):
        if item.name == SULFURAS:
            pass
        else:
            item.sell_in = item.sell_in - 1

        if item.name == AGED_BRIE:
            increase_item_quality(item)
            if item.sell_in < 0:
                increase_item_quality(item)
        elif item.name == BACKSTAGE_PASSES:
            increase_item_quality(item)
            if item.sell_in < 10:
                increase_item_quality(item)
            if item.sell_in < 5:
                increase_item_quality(item)
            if item.sell_in < 0:
                item.quality = 0
        elif item.name == SULFURAS:
          pass
        else: 
            decrease_item_quality(item)
            if item.sell_in < 0:
                decrease_item_quality(item)
            
                    
        
                



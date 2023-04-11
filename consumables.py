# consumables class
class Consumable:
    def __init__(self, name, affected_stat, stat_change):
        self.name = name
        self.affected_stat = affected_stat
        self.stat_change = stat_change
        
# variables of consumable items
bread = Consumable("bread", "hunger", 2)
raw_meat = Consumable("raw meat", "hunger", 3)
cooked_meat = Consumable("cooked meat", "hunger", 5)
health_potion = Consumable("health potion", "health", 5)
water_bottle = Consumable("water bottle", "thirst", 2)

# dictionary of consumable items
consumable_items = {
    "bread": bread,
    "raw meat": raw_meat,
    "cooked meat": cooked_meat,
    "health potion": health_potion,
    "water bottle": water_bottle
}

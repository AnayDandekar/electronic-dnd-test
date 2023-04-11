# import assets
from materials import materials

# items class
class Item:
    def __init__(self, name, materials):
        self.name = name
        self.materials = materials

# weapons subclass
class Weapon(Item):
    def __init__(self, name, materials, damage, weapon_range):
        super().__init__(name, materials)
        self.damage = damage
        self.weapon_range = weapon_range

# variables of weapons
sword = Weapon("sword", [materials.get("wood")], 5, "short")
bow_and_arrow = Weapon("bow and arrow", [materials.get("wood")], 2, "long")
hammer = Weapon("hammer", 7, [materials.get("wood")], "short")
dagger = Weapon("dagger", 3, [materials.get("wood")], "short")

# dictionary of items
items = {
    "weapons": {
        "sword": sword,
        "bow and arrow": bow_and_arrow,
        "hammer": hammer,
        "dagger": dagger
        }
}

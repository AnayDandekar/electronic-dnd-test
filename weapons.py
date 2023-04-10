# weapons class
class Weapon:
    def __init__(self, name, damage, weapon_range):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type

# variables of weapons
sword = Weapon("sword", 5, "short")
bow_and_arrow = Weapon("bow and arrow", 2, "long")
hammer = Weapon("hammer", 7, "short")
dagger = Weapon("dagger", 3, "short")

# dictionary of weapons
weapons = {
    "sword": sword,
    "bow and arrow": bow_and_arrow,
    "hammer": hammer,
    "dagger": dagger
}

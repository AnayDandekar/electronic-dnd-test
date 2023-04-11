# import assets
from voicefunctions import speak_text
from materials import materials
from items import items

# players class
class Player:
    def __init__(self, player_num, inventory, health, position, hunger, thirst):
        self.player_num = player_num
        self.inventory = inventory
        self.health = health
        self.position = position
        self.hunger = hunger
        self.thirst = thirst
    def craft_item(self, item):
        for material in item.materials:
            # check if all materials required to craft item are in player's inventory
            if material not in self.inventory:
                # notify player that they don't have all the required materials to craft the item
                speak_text(f"you don't have the materials to craft {item}", False, 120, 10)
                break
        else:
            # if all items required for crafting are present, remove them from player's inventory
            for material in item.materials:
                self.inventory.remove(material)
            # add crafted item to player's inventory
            self.inventory.append(item)
            # notify player that new item has been crafted
            speak_text(f"you successfully crafted {item}", False, 120, 10)

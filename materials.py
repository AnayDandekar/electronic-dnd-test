# materials class
class Material:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# variables of materials
wood = Material("wood", "can be harvested from all trees")
rope = Material("rope", "a thick bundle of string")
cloth = Material("cloth", "a large piece of rugged fabric")
thread = Material("thread", "like rope, but thinner")

# dictionary of materials
materials = {
    "wood": wood,
    "rope": rope,
    "cloth": cloth,
    "thread": thread
}

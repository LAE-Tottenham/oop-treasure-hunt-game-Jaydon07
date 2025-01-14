class Item():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Healing_item(Item):
    def __init__(self, name, desc, hp):
            super().__init__(name, desc)
            self.hp = hp

class Attack_item(Item):
    def __init__(self, name, desc, damage):
            super().__init__(name, desc)
            self.damage = damage
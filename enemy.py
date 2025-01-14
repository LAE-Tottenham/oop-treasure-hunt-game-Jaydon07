class Enemy():
    def __init__(self, name, health, damage, item, weakness):
        self.name = name
        self.health = health
        self.damage = damage
        self.item = item
        self.weakness = weakness
    
    def add_item(self, item_instance):
        self.item.append(item_instance)
        pass

    def remove_item(self, item_instance):
        self.item.remove(item_instance)
        pass

    def attack(self, player):
        player.health -= self.damage
        print(f"{self.name} inflicted {self.damage} of damage to {player.name}!")

    def death(self, player):
        print(f"{self.name} successfully defeated!")
        player.inventory.append(self.item)
        print(f"{self.name} has dropped for you you: {self.item.name}!")
        #self.remove_item(self.item)
class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.inventory = []
        self.weaponry = []
        self.lunchbox = []
        # add more atributes as needed

    def calculate_inventory_size(self):
        inventory_size = 0
        for i in range(len(self.inventory)):
            inventory_size += 1
        return inventory_size

    def add_item(self, item_instance, place):
        self.inventory.append(item_instance)
        place.remove_item(item_instance)

    def add_weapon(self, item_instance):
        self.weaponry.append(item_instance)
    
    def add_food(self, item_instance):
        self.lunchbox.append(item_instance)

    def eat(self, item_instance):
        if item_instance.type == "food":
            if self.health < 100:
                self.health += item_instance.hp
                if self.health >= 100:
                    self.health = 100
                print(f"{self.name} has been healed by {item_instance.hp} HP. Current health: {self.health} HP")
        else:
            pass
    
    def attack(self, enemy):
        for i in range(len(self.weaponry)):
            print(f"{i}: {self.weaponry[i].name}")
        weapon_num = int(input("Which weapon would you like to use? If you want to quit the battle, type '9'.\n"))
        weapon_used = self.weaponry[weapon_num]
        if weapon_used == enemy.weakness:
            enemy.health -= weapon_used.damage
            print(f"{self.name} inflicted {weapon_used.damage} of damage to {enemy.name}!")
        elif weapon_num == 9:
            quit_battle = True
        else:
            print(f"{enemy.name} is resistant to this weapon. No damage done by {self.name}!")

    def death(self):
        print("You have not survived your journey. Goodbye…")
        quit()
    # add more methods as needed
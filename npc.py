from item import Attack_item

class NPC():
    def __init__(self, given_name, dialogue):
        self.name = given_name
        self.dialogue = dialogue
        self.item = []

    def set_details(self, given_name, dialogue):
        self.name = given_name
        self.dialogue = dialogue

    def add_item(self, item_instance):
        self.item.append(item_instance)
        pass

    def remove_item(self, item_instance):
        self.item.remove(item_instance)
        pass
    
    def execute_dialogue(self, player):
        print(f"Now talking to… {self.name}!")
        print(self.dialogue)
        for i in range(len(self.item)):
            if isinstance(self.item[i], Attack_item):
                player.weaponry.append(self.item[i])
            else:
                player.inventory.append(self.item[i])
            print(f"{self.name} has given you: {self.item[i].name}!")
            self.remove_item(self.item[i])
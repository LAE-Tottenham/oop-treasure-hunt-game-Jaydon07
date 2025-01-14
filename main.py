from place import Place
from player import Player
from item import Item
from item import Healing_item
from item import Attack_item
from npc import NPC
from enemy import Enemy

class Game():
    def __init__(self):
        self.current_place = None
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # items
        hammer = Attack_item('Hammer', '', 15)
        pistol = Attack_item('Toy pistol', '', 20)
        cutlass = Attack_item('Toy cutlass', '', 12)
        
        pen = Item('Pen', '')
        boat = Item('Toy boat', '')
        light = Item('Flashlight', '')
        teleporter = Item('Teleport watch', '')
        real_treasure = Item('The real treasure', '')

        sandwich = Healing_item('Sandwich', '', 15)
        banana = Healing_item('Banana', '', 20)
        water = Healing_item('Drinking water', '', 30)
        chocolate = Healing_item('Box of chocolate coins', '', 50)

        # NPC
        self.lil_bro = NPC('Little Brother Jimmy', "Heard about that quest that Susanna decided you to trick you to go on, huh? I wouldn't exactly trust her, you know how she is… but, y'know, you do you! And before you set off, how about you take this? A hammer, to take down the bad guys guarding the treasure!")
        self.lilbro_dialogue = True
        self.lil_bro.add_item(hammer)

        self.scarlett = NPC("Scarlett", "Hey, buddy! What brings you out today? What's that? Another one of your sister's 'quests'? Yeah, about what I was expecting. I'm telling you, she's a LUNATIC. But, y'know, always got your best friend here when you need 'er. Speaking of… I just wanted to give you this! Use it wisely…")
        self.scarlett_dialogue = True
        self.scarlett.add_item(cutlass)

        #enemies
        self.crab = Enemy("The imaginary crab", 20, 4, pen, hammer)
        self.crab_instance = True

        self.shark = Enemy("Zackary T. Shark", 40, 8, pistol, cutlass)
        self.shark_instance = True

        # places
        living = Place('Living room', 1, None)
        bedroom = Place('Bedroom', 2, None)
        attic = Place('Attic', 6, None)
        kitchen = Place('Kitchen', 7, None)
        bathroom = Place('Bathroom', 3, pen, True) # bathroom is locked
        garden = Place('Garden', 4, cutlass, True)
        shed = Place('Shed', 5, None)
        park = Place('Park', 9, None, True)
        river = Place('River', 10, boat, True)
        cave = Place('Cave', 20, light, True)
        
        living.add_next_place(garden)
        living.add_next_place(bedroom)
        living.add_next_place(bathroom)
        living.add_next_place(kitchen)
        bedroom.add_next_place(living)
        bathroom.add_next_place(living)
        kitchen.add_next_place(living)
        kitchen.add_next_place(garden)
        garden.add_next_place(kitchen)
        

        # Item setup 
        bedroom.add_item(light)
        shed.add_item(boat)
        
        # home will be our starting place
        self.current_place = living
        
        # finish the setup function...
    
    def battle(self, player, enemy):
        print(f"Initiating battle with: {enemy.name}!")
        while player.health > 0 and enemy.health > 0:
            player.attack(enemy)
            enemy.attack(player)

            if player.health <= 0:
                player.death(enemy)
            elif enemy.health <= 0:
                enemy.death(player)
                player.quit_battle = True

    def start(self):
        gameplay_over = False
        while gameplay_over == False:
            print("You are currently in " + self.current_place.name)

            self.current_place.show_next_places()
            opt = input("""
What would you like to do?
1. Go to a place
2. Pick up item
3. Interact with NPC
4. Fight enemy
5. Check for puzzle 
6. Fast-travel
7. Check inventory
8. Use healing item
""")
            if opt == "1":
                for i in range(len(self.current_place.next_places)):
                    if self.current_place.next_places[i].name != "Attic":
                        print(f"{i}: {self.current_place.next_places[i].name}")
                place_num = int(input(("Where would you like to go?\n")))
                next_place = self.current_place.next_places[place_num]
                if next_place.locked == True:
                    #instead of saying the room is locked, check the user's backpack to see if they have the necessary unlock item. If they have the item, let them through; otherwise, lock them.
                    for i in range(len(player.inventory)):
                        if player.inventory[i] == next_place.unlock_item:

                            if next_place.unlock_item.name == "Pen":
                                pen_proceed = False
                                while pen_proceed == False:
                                    pen_input = input("Decrypt the following message in order to proceed:\nUjkxgt og vkodgtu!")
                                    if pen_input == "Shiver me timbers!":
                                        next_place.locked == False
                                        print("Good job! You have unlocked the next room.")
                                        self.current_place = self.current_place.next_places[place_num]
                                    else:
                                        print("Incorrect! Access denied.")
                                        pass

                            else:
                                next_place.locked == False
                                print("Good job! You have unlocked the next room.")
                                self.current_place = self.current_place.next_places[place_num]
                        elif next_place.unlock_item not in player.inventory:
                            print("Room locked! You need the following item to unlock:" + next_place.unlock_item.name)
                    continue
                else:
                    self.current_place = self.current_place.next_places[place_num]
            
            elif opt == "2":
                if len(self.current_place.items) == 0:
                    print("No items lying around!")
                    pass
                else:   
                    for i in range(len(self.current_place.items)):
                        print(f"{i}: {self.current_place.items[i].name}")
                    item_num = int(input(("Which item would you like to pick up?\n")))
                    player.add_item(self.current_place.items[item_num], self.current_place)
                    pass
            
            elif opt == "3":
                if self.lilbro_dialogue == True and self.current_place.name == 'Living room':
                    self.lil_bro.execute_dialogue(player)
                    self.lilbro_dialogue = False
                elif self.scarlett_dialogue == True and self.current_place.name == 'park':
                    self.scarlett.execute_dialogue(player)
                    self.scarlett_dialogue = False
                else:
                    print("Nobody to talk to!")

            elif opt == "4":
                if self.shark_instance == True and self.current_place.name == 'Bedroom':
                    self.battle(player, self.crab)

            elif opt == "7":
                if len(player.inventory) == 0:
                    print("Your inventory's currently empty. Try and find more items!")
                else:
                    for i in range(len(player.inventory)):
                        print(f"{player.inventory[i].name}: {player.inventory[i].desc}")
                pass
            



Gametest = Game()
Gametest.setup()
#print("Welcome to my game...")
name = input("Enter player name: ")
player = Player(name)
#print("Storyline...\n\nWelcome to a place of wonder, excitement, thrills… your house!\n\nWell, it may not seem like much… but you're a kid. You can do anything here if you're creative enough!")
#print("Your mission: collect enough clues set by your older sister, Susanna, in order to find the hidden treasure of gold.")
#game = False
#start = input("Speak up if you're up to the task!")
#if start == "":
#    print("Alright then. Goodbye!")
#    quit()
#else:
#    game = True
#    while game == True:
Gametest.start()
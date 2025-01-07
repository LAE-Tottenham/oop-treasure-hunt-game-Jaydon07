from place import Place
from player import Player
from item import Item

class Game():
    def __init__(self):
        self.current_place = None
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # places
        home = Place('Home', 1)
        bedroom = Place('Bedroom', 2)
        bathroom = Place('Bathroom', 3, True) # bathroom is locked
        garden = Place('Garden', 4, True)
        shed = Place('Shed', 5)
        river = Place('River', 10)
        cave = Place('Cave', 20)
        
        home.add_next_place(garden)
        home.add_next_place(bedroom)
        #bedroom.add_next_place(bathroom)
        #garden.add_next_place(shed)
        # etc. 
        
        # items
        hammer = Item('Hammer', '')
        pen = Item('Pen', '')

        home.add_item(hammer)
        bedroom.add_item(pen)

        # home will be our starting place
        self.current_place = home
        
        # finish the setup function...

    def start(self):
        print("Welcome to my game...")
        print("Storyline...\n\nWelcome to a place of wonder, excitement, thrills… your house!\n\nWell, it may not seem like much… but you're a kid. You can do anything here if you're creative enough!")
        print("Your mission: collect enough clues set by your older sister, in order to find the hidden treasure of gold.")
        name = input("Enter player name: ")
        player = Player(name)

        gameplay_over = False
        while gameplay_over == False:
            print("You are currently in " + self.current_place.name)
            self.current_place.show_next_places()
            opt = input("""
What would you like to do?
1. Go to a place
2. Interact
3. Use item
4. Check inventory
etc.
""")
            if opt == "1":
                if len(self.current_place.next_places) == 1:
                    self.current_place = self.current_place.next_places[0]
                else: 
                    for i in range(len(self.current_place.next_places)):
                        print(f"{self.current_place.next_places[i].id}: {self.current_place.next_places[i].name}")
                    self.current_place.id = int(input(("Where would you like to go?")))
            elif opt == "2":
                # add code
                pass
            elif opt == "4":
                if len(player.inventory) == 0:
                    print("Your inventory's currently empty. Try and find more items!")
                else:
                    for i in range(len(player.inventory)):
                        print(f"{player.inventory[i].name}: {player.inventory[i].desc}")
                pass
            



Gametest = Game()
Gametest.setup()
Gametest.start()
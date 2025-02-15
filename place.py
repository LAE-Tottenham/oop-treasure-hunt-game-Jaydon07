class Place():
    def __init__(self, given_name, place_id, unlock_item, locked=False):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.id = place_id
        self.locked = locked
        self.next_places = []
        self.items = []
        self.unlock_item = unlock_item
        # add more atributes as needed

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.items.append(item_instance)
        pass

    def remove_item(self, item_instance):
        self.items.remove(item_instance)
        pass
    
    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            # remember that next_places is a list of Place instances hence why we can use place.name
            print(place.name)

    # add more methods as needed

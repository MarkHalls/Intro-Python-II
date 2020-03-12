from print_wrap import print_wrap

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """
    The Player object contains details about the player

    Args: 
        name (str): The players name
        current_room (Room): The room the player is currently in
    """

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = list()

    def move(self, cmd):
        newRoom = getattr(self.current_room, cmd + "_to")
        if newRoom:
            self.current_room = newRoom
            print(self.current_room)
            return ""
        else:
            return "Error: You can't go that way."

    def get_inventory(self):
        if len(self.inventory) > 0:
            print_wrap("Your inventory: ")
            for item in self.inventory:
                print_wrap(item.name)
        else:
            print_wrap("You don't currently have any items")

    def set_inventory(self, item):
        if item:
            self.inventory.append(item)

    def take_item(self, item_name):
        item = self.current_room.take_item(item_name)
        if item:
            self.set_inventory(item)
            item.on_take()

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.current_room.set_items(item)
                self.inventory.remove(item)
                item.on_drop()
            else:
                print_wrap(f"You don't have {item_name} in your inventory")

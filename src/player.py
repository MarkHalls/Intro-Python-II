from print_wrap import print_wrap
import re

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
        else:
            print_wrap(f"You can't go that way.")

    def get_inventory(self):
        if len(self.inventory) > 0:
            print_wrap("Your inventory: ")
            for item in self.inventory:
                print_wrap(f"*{item.name} - {item.description}")
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

    def commands(self, command):
        directions = ("n", "s", "e", "w")

        if command.lower() in directions:
            self.move(command.lower())

        elif "take" in command.lower():
            item_name = re.sub(re.escape("take "), "", command, flags=re.IGNORECASE)
            self.take_item(item_name)

        elif "drop" in command.lower():
            item_name = re.sub(re.escape("drop "), "", command, flags=re.IGNORECASE)
            self.drop_item(item_name)

        elif "i" in command.lower():
            self.get_inventory()

        elif command in ("Q", "q", "quit", "exit"):
            exit(0)

        elif command in ("?", "help", "h"):
            command_list = [
                "Command List",
                "n - Move North",
                "n - Move North",
                "n - Move North",
                "n - Move North",
                "i - View inventory",
                "take <item> - Take an item from the room",
                "q - exit the game",
                "h - display this text",
            ]
            for item in command_list:
                print_wrap(item)

        else:
            pass

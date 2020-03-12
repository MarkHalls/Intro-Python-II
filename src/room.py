from item import Item
from print_wrap import print_wrap

# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """
    The Room object contains details about a room

    Args: 
        name (str): The rooms name
        description (str): The rooms description

    Attributes: 
        n_to (Room): The room to the north
        s_to (Room): The room to the south
        e_to (Room): The room to the east
        w_to (Room): The room to the west
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = list()

    def __str__(self):
        room_details = [
            "****************************",
            f"Room: {self.name}",
            " ",
            "Details:",
            f"{self.description}",
            " ",
        ]

        for line in room_details:
            print_wrap(line)

        # show list of items in the room
        if len(self.items) > 0:
            print_wrap("You see some items")
            for item in self.items:
                print_wrap(item.name)

        # get directions and print them to the screen
        for line in self.get_directions():
            print_wrap(line)

        return ""

    def take_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        print_wrap(f"You searched the room but couldn't find {item_name}")

    def get_items(self):
        for item in self.items:
            print_wrap(item.name)

    def set_items(self, item):
        if isinstance(item, Item):
            self.items.append(item)

    def get_directions(self):
        compass = {
            "n_to": "north",
            "s_to": "south",
            "e_to": "east",
            "w_to": "west",
        }
        directions = []

        for key, value in vars(self).items():
            if "_to" in key and value:
                directions.append(compass[key])

        direction_string = str(directions).strip("[]").replace("'", "")

        return [
            " ",
            f"There are rooms to the {direction_string}",
            " ",
            "  N  ",
            "W   E",
            "  S  ",
        ]


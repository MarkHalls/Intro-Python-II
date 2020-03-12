from room import Room
from player import Player
from print_wrap import print_wrap
from item import Item

import re

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# create some items
item = Item("map", "I'm a map")
room["outside"].set_items(item)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Mae", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(player.current_room)

while True:
    move = None

    cmd = input("\n  ~~> ")

    directions = ("n", "s", "e", "w")

    if cmd.lower() in directions:
        move = player.move(cmd.lower())

    elif "take" in cmd.lower():
        item_name = re.sub(re.escape("take "), "", cmd, flags=re.IGNORECASE)
        player.take_item(item_name)

    elif "drop" in cmd.lower():
        item_name = re.sub(re.escape("drop "), "", cmd, flags=re.IGNORECASE)
        player.drop_item(item_name)

    elif "i" in cmd.lower():
        player.get_inventory()

    elif cmd in ("Q", "q", "quit", "exit"):
        exit(0)

    elif cmd in ("?", "help", "h"):
        available_commands = [
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
        for command in available_commands:
            print_wrap(command)

    else:
        pass

    if move and "Error" in move:
        print_wrap(move.replace("Error: ", ""))

from room import Room
from player import Player
from textwrap import TextWrapper

# initialize TextWrapper with 40 character width
wrapper = TextWrapper(
    initial_indent="  ", subsequent_indent="  ", drop_whitespace=False, width=40
)

# custom print command for wrapped text
def print_wrap(text):
    line_list = wrapper.wrap(text)
    for line in line_list:
        print(line)


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

while True:
    move = None
    room_details = [
        "****************************",
        f"Room: {player.current_room.name}",
        " ",
        "Details:",
        f"{player.current_room.description}",
        " ",
    ]

    for line in room_details:
        print_wrap(line)

    # get directions and print them to the screen
    for line in player.current_room.get_directions():
        print_wrap(line)

    cmd = input("\n  Enter a command: ")

    if cmd in ("N", "n"):
        move = player.move(player.current_room.n_to)
    elif cmd in ("W", "w"):
        move = player.move(player.current_room.w_to)
    elif cmd in ("E", "e"):
        move = player.move(player.current_room.e_to)
    elif cmd in ("S", "s"):
        move = player.move(player.current_room.s_to)
    elif cmd in ("Q", "q", "quit", "exit"):
        exit(0)
    else:
        pass

    if move and "Error" in move:
        print_wrap(move.replace("Error: ", ""))

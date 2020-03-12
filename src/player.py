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

    def move(self, newRoom):
        if newRoom:
            self.current_room = newRoom
            return ""
        else:
            return "Error: You can't go that way."

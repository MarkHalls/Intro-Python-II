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

    def get_directions(self):
        compass = {
            "n_to": "north",
            "s_to": "south",
            "e_to": "east",
            "w_to": "west",
            "e_to": "east",
        }
        directions = []

        for key, value in vars(self).items():
            if "_to" in key and value:
                directions.append(compass[key])

        direction_string = str(directions).strip("[]").replace("'", "")

        return [
            f"There are rooms to the {direction_string}",
            " ",
            "  N  ",
            "W   E",
            "  S  ",
        ]


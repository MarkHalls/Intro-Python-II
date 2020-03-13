from print_wrap import print_wrap


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print_wrap(f"You have picked up {self.name}")

    def on_drop(self):
        print_wrap(f"You have dropped the {self.name}")

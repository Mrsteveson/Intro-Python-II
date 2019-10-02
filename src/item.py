# Create an Item class
# Player wants to be able to pickup and drop

class Item:
    """Player Collectable Items"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_pickup(self):
        print(f"\nSuccessfully added, {self.name} to your inventory.")

    def on_drop(self):
        print(f"\nSuccessfully dropped, {self.name}, on the room floor.")
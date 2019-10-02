# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        if items == None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"Greetings, {self.name}, you are currently in {self.room}."

    def move(self, direction):
        if getattr(self.room, f"{direction}_to") is not None:
            self.room = getattr(self.room, f"{direction}_to")
        else:
            print("\nThere is no room in that direction, please choose again.")
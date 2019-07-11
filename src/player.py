# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def __str__(self):
        return f'Greetings, {self.name}, you are currently in {self.room}'

    def move(self, direction):
        if getattr(self.room, f"{direction}_to") is not None:
            self.room = getattr(self.room, f"{direction}_to")
        else:
            print('\nThere is no room in that direction')

    def take(self, item):
        # print('take firing!?')
        if item in self.room.items:
            self.items.append(item)
            self.room.items.remove(item)
            item.on_take()
        else:
            print(f'\n {item} is not in this room')

    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            self.room.items.append(item)
            item.on_drop()
        else:
            print(f'\n {item} is not in your inventory')

    def show_items(self):
        print(f"\n{self.name}'s stuff:\n" + ", " .join([item.name for item in self.items]))
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def __str__(self):
        return f'Greetings, {self.name}, you are currently in {self.room}'

    def take(self, item):
        for item in self.room.items:
            if item.name == item:
                self.items.append(item)
                self.room.items.remove(item)
                item.on_take()
            else:
                print(f'\n {item} is not in this room')

    def drop(self, item):
        for items in self.items:
            if item.name == item:
                self.items.remove(item)
                self.room.items.append(item)
                item.on_drop()
            else:
                print(f'\n {item} is not in your inventory')
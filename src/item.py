class Item:
    """Collectable Items"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'\n You have picked up {self.name}')

    def on_drop(self):
        print(f'\n You have dropped {self.name}')
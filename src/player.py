# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player():
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        if len(items):
            for n, d in items:
                self.items.append(Item(n, d))

    def __str__(self):
        return f"Player: {self.name}"

    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.current_room)})"

    def add_item( self, item ):
        self.items.append(Item(item[0], item[1]))

    def remove_item( self, item ):
        for item in self.items:
            if item.description == item:
                self.items.remove(item)


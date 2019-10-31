# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room():
    def __init__(self, name, description,items=[]):
        self.name = name
        self.description = description
        if len(items):
            for n, d in items:
                self.items.append(Item(n, d))

    def __str__(self):
        return f"Room: {self.name}"

    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"

    def add_item( self, item ):
        self.items.append(Item(item[0], item[1]))

    def remove_item( self, item ):
        for item in self.items:
            if item.description == item:
                self.items.remove(item)
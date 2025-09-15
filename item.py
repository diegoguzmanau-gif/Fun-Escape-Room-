import time
import sys

def slow_print(text, delay=0.003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
class Item():

    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name
#if you see this you are cool!
    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def describe(self):
        slow_print("The [" + self.name + "] is here - " + self.description, delay=0.05)

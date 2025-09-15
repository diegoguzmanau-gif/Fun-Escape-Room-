
import time
import sys

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None


    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            slow_print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    enemies_to_defeat = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None 
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You give " + self.name + " the " + combat_item ) #you give troy the finger 😱
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True
        else:
            print(self.name + " doesnt want it...")
            return False
    
    def steal(self):
        print("You steal from " + self.name)

class Friend(Character):
  
    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        slow_print(self.name + " hugs you back!", delay=0.05)


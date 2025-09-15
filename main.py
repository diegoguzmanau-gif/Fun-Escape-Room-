from room import Room, slow_print #i love the slow print <3
from character import Enemy, Friend, Character
from RPGinfo import RPGInfo
from item import Item
import time
import sys
import random
class Main():

    escape_room = RPGInfo("The Cool Escape Room") #what a cool name!
    escape_room.welcome()
    RPGInfo.info()
    RPGInfo.author = "\033[94mDiego\033[0m"

    door = Room("Door")
    door.set_description("3 digits code lock? i wonder how to \033[94m'open'\033[0m it")

    middle = Room("Middle ")
    middle.set_description("The center of the room, move where you want.")

    wall_1 = Room("Wall one") #1
    wall_1.set_description("The name is pretty self explanitory.")

    wall_2 = Room("Wall 2")
    wall_2_poem = """
    On this wall, a curious puzzle lies.

    At the top, forks are crossed, their silver teeth pointing out.

    Below them, a cluster of oranges forms a bright, round shape.

    To the side, an umbrella hangs open, its handle curved like a secret smile.

    And finally, a row of roses trails along the bottom, their petals whispering red.
    """ #the starting letter of the noun (thing) in each sentence gives you the second digit, F O U R.
    wall_2.set_description(wall_2_poem)

    wall_3 = Room("Wall 3")
    wall_3.set_description("Blank wall, wonder how that paint chip got there... ")
    lectern = Friend("Lectern", "A sturdy wooden lectern stands here, waiting for a book.")
    lectern.set_conversation("""
On the first day of Christmas, my true love gave to me: a partridge in a pear tree.
On the second day of Christmas, my true love gave to me: two turtle doves,
On the third day of Christmas, my true love gave to me: three French hens,
On the fourth day of Christmas, my true love gave to me: four calling birds,
On the fifth day of Christmas, my true love gave to me: five golden rings,
On the sixth day of Christmas, my true love gave to me: six geese a-laying,
On the seventh day of Christmas, my true love gave to me: seven swans a-swimming...
The rest of the pages are ripped out.
""") #wow the poem is long, too bad you have to read it all. Scince the number the poem stops at is seven and its at wall 3, the third number is 7.
    wall_3.set_character(lectern)

    hallway = Room("Hallway")
    hallway.set_description("A dark hallway. You can't go back. Choose left or right.")

    print("There are " + str(Room.number_of_rooms - 2) + " rooms to explore.")

    door.link_room(middle, "south")
    wall_2.link_room(middle, "north")
    wall_3.link_room(middle, "west")
    middle.link_room(door, "north")
    middle.link_room(wall_3, "east")
    middle.link_room(wall_2, "south")
    middle.link_room(wall_1, "west")
    wall_1.link_room(middle, "east")
    door.link_room(hallway, "forward")#once you are in the hallway, theres no going back!

    troy = Enemy("troy", "he only has one finger") #I dont even know a troy, just made it random.
    troy.set_conversation("Please give me my finger back")
    troy.set_weakness("finger")
    wall_1.set_character(troy)

    cheese = Item("finger")
    cheese.set_description("I think this came from someone")
    wall_3.set_item(cheese)

    book = Item("book")
    book.set_description("'12 days of christmas', what is this doing here? maybe the lectern wants it...")
    middle.set_item(book)

    current_room = middle
    backpack = []

    door_unlocked = False  
    book_read = False

    dead = False
    while dead == False:
        slow_print("\n")
        current_room.get_details()
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()
        time.sleep(1)
        item = current_room.get_item()
        if item is not None:
            item.describe()
        time.sleep(1)
        print("you can also '\033[94mtake\033[0m', '\033[94mgive\033[0m', and '\033[94mtalk\033[0m'") #found out how to make colours, now im abusing it!!
        time.sleep(1)

        command = input(">>  ")
        
        # Check whether a direction was typed
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
        
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                # If the inhabitant is the lectern and player has the book
                if inhabitant == lectern:
                    if "book" in backpack:
                        inhabitant.talk()
                        book_read = True
                        slow_print("\033[92mYou have read the book!\033[0m", delay=0.05) #acheivement in the game
                        time.sleep(1)
                    else:
                        print("You need a book to read at the lectern.")
                        time.sleep(1)
                else:
                    inhabitant.talk()
                    time.sleep(1)
            else:
                print("There is no one here to talk to")
                command = input(">>  ")
        
        elif command == "give":
            # You can check whether an object is an instance of a particular
            # class with isinstance() - useful! This code means
            # "If the character is an Enemy"
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                # Fight with the inhabitant, if there is one
                slow_print("What will you give?", delay=0.05)
                fight_with = input()
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, he put the finger back on!")
                        current_room.set_character(None)
                        if Enemy.enemies_to_defeat == 0:
                            time.sleep(3)
                            slow_print("wow, troy opened the door for you, \033[92mYou Win!\033[0m", delay=0.05)
                            dead = True #another way of wining
                    else:
                        # What happens if you lose?
                        time.sleep(0.5)
                        print("...")
                        time.sleep(2)
                        slow_print("Or maybe he doesn't like you...", delay=0.3)
                        time.sleep(3)
                        dead = False
                else:
                    slow_print("You don't have a " + fight_with , delay=0.05)
            else:
                print("There is no one here to give someonting")
                command = input(">>  ")

        elif command == "take":
            if item is not None:
                slow_print("You put the " + item.get_name() + " in your backpack", delay=0.05) #imagine if you renamed the backpack to bum and it says 'you put the finger in your bum'! -Ved nimbalkar
                backpack.append(item.get_name())
                current_room.set_item(None)
                time.sleep(1)
            else:
                print("There's nothing here to take!")
                command = input(">>  ")
        elif command == "open":
                    if current_room == door:
                        print("You try to open the door, what is the 3 digit code?")
                        code = input()
                        if code == "147":
                            print("The door opens, just continte \033[94mforward\033[0m")
                            door_unlocked = True  # Set flag when unlocked
                        else:
                            print("Wrong code")
                            dead = True
                            slow_print('as you look up, an anvil falls on your head, \033[91myou die\033[0m', delay=0.05)
                    else:
                        print("There is nothing to open here")
                        command = input(">>  ")

        elif command == "forward":
            if current_room == door and door_unlocked:
                if book_read:
                    current_room = hallway
                else:
                    slow_print("You feel like you should read something important before moving forward...", delay= 0.05)
                    time.sleep(1)
            elif current_room == door and not door_unlocked:
                print("The door is still locked.")
                time.sleep(1)
                command = input(">>  ")
            else:
                print("There's nowhere to go forward here.")
                time.sleep(1)
                command = input(">>  ")
        if current_room == hallway: #lwft and right are rooms, trust me
            slow_print("You are in the hallway. You must choose: left or right.", delay= 0.05)
            time.sleep(2)
            choice = input("Which way do you go? (left/right): ").strip().lower()
            if choice in ["left", "right"]:
                if random.choice([True, False]): #random because its funny!!!!!
                    slow_print(f"You chose {choice} and found the exit! \033[92mYou win!\033[0m")
                    dead = True
                else:
                    slow_print(f"You chose {choice} and fell into a trap! \033[91mYou lose!\033[0m")
                    dead = True
            else:
                print("You stand in the hallway, unable to decide...")
                dead = False
        elif command == "hug":
            if inhabitant is not None:
                if inhabitant == lectern:
                    slow_print("dumbass, lecterns cant hug you back, but you still try...", delay=0.05)
                if inhabitant == Enemy:
                    slow_print("i wouldnt do that if i were you, he might bite", delay=0.05)
                else:
                    inhabitant.hug()
            else:
                print("There's no one here to hug.")

    RPGInfo.credits()

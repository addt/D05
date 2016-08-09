#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(name_s, count = 0):
    print("You walk through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print(name_s +" take the stairs")
        if (count > 0):
            print("but "+ name_s +" is not happy about it")
        infinite_stairway_room(name_s,count + 1)
    # option 2 == ?????
    if next == "turn around":
        print("tada")


def gold_room(name_s):
    print("This room is full of gold.  How much do " + name_s +" take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room(name_s):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are " + name_s +" going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at " + name_s +" then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door." + name_s +" can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room(name_s)
        else:
            print("I got no idea what that means.")


def cthulhu_room(name_s):
    print("Here " + name_s +" see the great evil Cthulhu.")
    print("He, it, whatever stares at " + name_s +" and " + name_s +" go insane.")
    print("Do " + name_s +" flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    user_name = input("Enter your name")
    print(user_name +" is in a dark room.")
    print("There is a door to your right, left and ahead")
    print("Which one does " + user_name +" take?")

    
    next = input("> ")

    if next == "left":
        bear_room(user_name)
    elif next == "right":
        cthulhu_room(user_name)
    elif next == "ahead":
        infinite_stairway_room(user_name)
    else:
        dead("You stumble around the room until " + user_name +" starve.")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import random

def display_menu():
    print("The Wizard Inventory Program")
    print()
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def check_inventory():
    inventory = []

def walk(inventory):
    wai = "wizard_all_items.txt"
    with open(wai) as item_list:
        items = item_list.readlines();
        item = random.choice(items)
        print("While walking down a path, you see", item)
        grab = input("Do you want to grab it? (y/n):  ")
        if grab == "y":
            if grab == "y" and len(inventory) == 4:
                print("You can't carry any more items. Drop something first.")
                print()
            else:
                print("You picked up", item)
                inventory.append(item)
        if grab == "n":
            print("You decide to leave " + item + "behind.")
            print()

def show(inventory):
    i = 1
    for item in inventory:
        print(str(i) + ": " + item)
        i += 1
    if len(inventory) == 0:
        print("You haven't found any loot yet. Keep searching!")

def drop(inventory):
    num = int(input("Number:  "))
    if num < 1 or num > len(inventory):
        print("That inventory spot isn't filled yet.\n")
    else:
        item = inventory.pop(num-1)
        print("You dropped", item)

def exit():
    print("Good luck on your quest!")

def main():
    display_menu()
    inventory = []
    while True:
        command = input("Command: ")
        if command == "walk":
            walk(inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop(inventory)
        elif command =="exit":
            exit()
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()

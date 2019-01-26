rjct = ("You can't do that here.")

yesList = ["yes", "yeah", "y", "sure"]
noList = ["no", "nah", "nevermind", "n"]

contList = ["continue", "proceed", "go forward", "go ahead"]
goList = ["go back", "go", "leave", "go away"]

def adventure():

    import time
    import random
    dungeonRooms = ["puzzle", "enemy", "journal", "loot", "pretty", "loop", "body", "nothing"]

    roomNum = random.randint(3,10)
    dungeon = True
    while dungeon:
        #- make this prettier
        print("You enter the dungeon.\n")
        time.sleep(2)
        currentRoom = random.choice(dungeonRooms)
        if roomNum <= 0:
            print("Dungeon end")
            break

        elif currentRoom == "nothing":
            roomNum -= 1
            print("There is nothing remarkable about this room.")
            inpt = input("What do you want to do?\n").lower()

            if inpt in contList:
                print("You press on.")
            elif inpt in goList:
                print("You leave the dungeon.")
            elif inpt in ["look", "look around", "stay"]:
                #- continues generating rooms
                print("It's just a plain, empty room. The most interesting thing here is the spider crawling through a crack in the wall.")
            else:
                print(rjct)

##            progression()
        elif currentRoom == "enemy":
            roomNum -= 1
            opponentHealth = random.randint(3,15)
            print(opponentHealth)
            print("enemy")

        elif currentRoom == "journal":
            roomNum -= 1
            print("journal")

        elif currentRoom == "loot":
            roomNum -= 1
            print("loot")
        elif currentRoom == "pretty":
            roomNum -= 1
            print("pretty")
        elif currentRoom == "loop":
            roomNum -= 1
            print("loop")
        elif currentRoom == "body":
            roomNum -= 1
            print("body")
        elif currentRoom == "puzzle":
            roomNum -= 1
            print("puzzle")

        print(roomNum, currentRoom)

adventure()

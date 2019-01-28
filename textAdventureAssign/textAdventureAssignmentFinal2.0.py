##General Responses
rjct = ("You can't do that here.\n")

yesList = ["yes", "yeah", "y", "sure", "ye"]
contList = ["continue", "keep going"]
noList = ["no", "nah", "nevermind", "n"]
goList = ["go back", "go", "leave", "go away", "nothing", "none", "nevermind", "back"]

##Player's Stats
inv = ["shortsword", "mysterious note"]
coin = 200

lvl = 1
health = 10
tempHealth = 10
force = 5
panache = 5
dmg = 1 + round(force / 2)
rep = 1 + round(panache / 2)

won = False

##item values
price = {"health potion": 35, "shortsword": 75, "handaxe": 65, "worker's tools": 15, "fancy quill": 15, "lockpick": 25, "wagon": 175, "sweet wine": 10, "plain necklace": 20, "love story": 5, "horse carving": 1, "flattering letter": 1, "candle": 3, "old bones": 1, "fake jewels": 5}
marketItems = ["shortsword", "handaxe"]

##equipment values
equipped = {"weapon": "shortword", "armour": "no armour"}
if "shortsword" in equipped:
    force += 1

if "handaxe" in equipped:
    force += 2

if "plain necklace" in equipped:
    panache += 1

##imports
import time
import random

##Player Functions

##level up
def levelUp():
    global lvl
    global health
    global panache
    global force

    lvl += 1
    health += 5 + (round(lvl/2))
    if panache > force:
        panache += 3 + (round(lvl/2))
        force += 3 + (round(lvl/3))

    elif force > panache:
        panache += 3 + (round(lvl/3))
        force += 3 + (round(lvl/2))

    elif force == panache:
        panache += 3 + (round(lvl/3))
        force += 3 + (round(lvl/3))

    print("You leveled up!\nYou are now level {0}. Your panache is at {1} and your force at {2}. You have {3} coin.".format(lvl, panache, force, coin))
    time.sleep(2)

##market
def market():
    global coin
    market = True

    while market:

        inpt = input("Do you wish to 'buy', 'sell', or 'leave'?\n").lower()
        time.sleep(1)

        ##buying
        if inpt in  ["buy", "purchase"]:
            inpt = input("The items on sale are: " + (", ").join(marketItems) + ". What do you want to buy?\n").lower()
            time.sleep(1)
            if inpt in price:
                cost = price.get(inpt) - round(rep / 10)
                item = inpt
                inpt = input("This will cost " + str(cost) + " coin. Proceed?\n").lower()
                time.sleep(1)

                if inpt in yesList:
                    if coin >= cost:
                        coin -= cost
                        inv.append(item)
                        print("You are now the proud owner of a '{0}'. You have {1} coin.\n".format(item, coin))
                        time.sleep(2)

                    else:
                        print("You don't have enough coin for that!\n")
                        time.sleep(2)

                elif inpt in noList:
                    print("You decide not to buy.\n")
                    time.sleep(2)

                elif inpt in goList:
                    print("You leave the market.\n")
                    time.sleep(2)
                    break

                else:
                    print(rjct)
                    time.sleep(2)
        #selling
        elif inpt in ["sell", "give"]:
            inpt = input("In your inventory, you have " + (", ").join(inv) + ". What would you like to sell?\n").lower()
            time.sleep(1)
            if inpt in inv:
                if inpt in price:
                    cost = price.get(inpt) + round(rep / 10)
                    item = inpt
                    inpt = input("Sell your '" + item + "' for " + str(cost) + "?\n").lower()
                    time.sleep(1)
                    if inpt in yesList:
                        coin += cost
                        inv.remove(item)
                        print("You no longer have your '" + item + "'. You have " + str(coin) + " coin.\n")
                        time.sleep(2)

                    elif inpt in noList:
                        print("You decide not to sell.\n")
                        time.sleep(2)
                else:
                    print(rjct)
                    time.sleep(2)

        elif inpt in goList:
            print("You leave the market.\n")
            time.sleep(2)
            break


        else:
            print(rjct)
            time.sleep(2)

##use item
def useItem():
    global tempHealth
    global health
    global panache
    global force

    use = True
    while use:
        inpt = input("You have " + (", ").join(inv) + ". What do you want to use? Alternatively, you could 'leave'.\n").lower()
        time.sleep(1)

        if inpt in inv:

            if inpt in ["axe", "handaxe", "hand axe", "hand-axe"]:
                equipped["weapon"] = "handaxe"
                print("You equip your handaxe.\n")
                time.sleep(2)

            elif inpt in ["sword", "shortsword", "short sword", "short-sword"]:
                equipped["weapon"] = "shortsword"
                print("You equip your shortsword.\n")
                time.sleep(2)
                
            elif inpt == "plain necklace":
                equipped["armour"] = "plain necklace"
                print("You equip your plain necklace.\n")
                time.sleep(2)

            elif inpt in ["health", "health potion", "potion", "drink potion", "drink health potion"]:
                tempHealth += 5
                inv.remove("health potion")
                if tempHealth > health:
                    tempHealth = health
                print("You drink the potion! Your health is now " + str(tempHealth) + ".\n")
                time.sleep(2)

            elif inpt in ["wine", "sweet wine", "drink wine", "drink sweet wine"]:
                panache += 3
                inv.remove("sweet wine")
                print("Your head feels funny. That was good wine - very good. Perhaps drinking the whole bottle was a bad idea. But you feel a lot more confident now. Your panache has increased to " + str(panache) + "!\n")
                time.sleep(2)

            elif inpt in ["mysterious note", "note", "letter"]:
                print("The letter reads: '" + name + ". Escape the Free Spirit. - J.B.' You don't know any J.B., but the letter gives off a weird energy. Perhaps it is the distinct smell of salted meat coming off of the page.\n")
                time.sleep(2)

            elif inpt in ["quill", "fancy quill", "pen"]:
                print("You pen a lovely letter. The words seem to flow spectacularly from your mind; it is a shame you have no one to send it to.\n")
                inv.append("flattering letter")
                print("You now have a 'flattering letter'!\n")
                time.sleep(2)

            elif inpt == "worker's tools":
                print("You find a chunk of wood on the ground and carve a small horse into it. What a charming little trinket.\n")
                inv.append("horse carving")
                print("You now have a 'horse carving'!\n")
                time.sleep(2)

            elif inpt == "love story":
                print("The stolen glances, mutual pining, breathless confessions... Oh my! This story is so beautifully written, it brings a tear to your eye.\n")
                time.sleep(2)

            elif inpt == "lockpick":
                print("You're sure this could come in handy someday. People around here don't seem too worried about locking their doors though...")
                time.sleep(2)

            elif inpt == "horse carving":
                print("You're rather impressed with your own handy work. Then again, you're not sure the local merchants would agree when it came to haggling.")
                time.sleep(2)

            elif inpt == "flattering letter":
                print("The words on this page are filled with admiration and praise. It's sure to make its recipient feel appreciated!")
                time.sleep(2)

            elif inpt == "candle":
                print("It's just a plain old candle. Surely you can find a use for it. Presumably by lighting it.")
                time.sleep(2)

            elif inpt == "old bones":
                print("They almost crumble at your touch. You question why you still have these.")
                time.sleep(2)

            elif inpt == "fake jewels":
                print("They look pretty enough, but they're not fooling anyone.")
                time.sleep(2)

            elif inpt == "wagon":
                print("Hopefully it'll serve you well in the journey to come. It's never let you down so far, but then again you haven't had it long.\n")
                time.sleep(2)
            
            else:
                print(rjct)
                time.sleep(2)

        elif inpt in goList:
            print("You close your pack and continue.\n")
            time.sleep(2)
            break

        else:
            print("You don't have that item...\n")
            time.sleep(2)
            
##adventure
def adventure():
    global opponentHealth
    global tempHealth
    global health
    global coin

    import time
    import random
    dungeonRooms = ["puzzle", "enemy", "journal", "loot", "pretty", "loop", "body", "nothing"]
    
    ##randomly generating size & room
    roomNum = random.randint(3,10)
    dungeon = True
    print("You enter the dungeon.\n")
    while dungeon:
        time.sleep(2)
        currentRoom = random.choice(dungeonRooms)
        if roomNum <= 0:
            print("You've reached the end of the dungeon! You find some loot and head off.\n")
            time.sleep(2)
            coin += 50
            print("You gained 50 coin!\n")
            time.sleep(2)
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "nothing":
            roomNum -= 1
            print("There is nothing remarkable about this room.")
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "enemy":
            roomNum -= 1
            opponentHealth = (round(random.randint(3,15)) + (lvl / 3))
            print("You hear a dull thud of footsteps as you enter the next room. Barely illuminated by a nearby fire is a disturbingly tall creature, walking upright like a man but with antlers on its head, dripping with what appears to be a thick black... goo.\n")
            time.sleep(2)
            print("Get ready for a fight!")
            time.sleep(2)
            fightMode()
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "journal":
            roomNum -= 1
            print("Scattered across the floor of the next room are pages from an adventurer's journal. Most of the pages are damaged beyond repair, but you can make out one of the accounts. It details a scandalous love affair! The participants are anonymous, but you pocket it anyway.")
            inv.append("love story")
            time.sleep(2)
            print("You now have a 'love story'!\n")
            time.sleep(2)
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "loot":
            roomNum -= 1
            print("Searching the next room, you catch something glinting in your torch light. Upon further inspection, it appears to be some loot! Score!")
            coin += 5
            time.sleep(2)
            print("You gained 5 coin!\n")
            time.sleep(2)
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "pretty":
            roomNum -= 1
            print("The next room is so strikingly beautiful. Moonlight barely graces the moss on the cracks of the stone walls, the cracked floor tracing a natural pattern. There's nothing else here, but you stop for a minute to take it all in.\n")
            time.sleep(2)
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "loop":
            roomNum += 1
            print("Wait a second - you've been here before! It appears that the dungeon has looped around and you've lost some progress.\n")
            time.sleep(2)
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "body":
            roomNum -= 1
            print("The next room you enter is quite dark. As you walk through, your foot hits something... odd. You shine your light on it, and discover a dead body! It's not fresh, but it's not old enough for you to be entirely comfortable with it either.\n")
            time.sleep(2)
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

        elif currentRoom == "puzzle":
            roomNum -= 1
            print("Three pillars stand before a locked door in this room, each with a switch held in place by a different object.\n1. On the left pillar, a pile of bones crumbles to dust atop a pedestal of rotting wood.\n2. The middle pillar is ceramic, with a candle and a feathered quill on top.\n3. The final pillar on the right is solid gold, and on top is an assortment of fine jewels.\n")
            time.sleep(2)
            inpt = input("Which one do you take?\n").lower()
            time.sleep(1)
            
            if inpt in ["1", "bones", "wooden pillar", "left pillar", "left"]:
                inv.append("old bones")
                tempHealth -= 4
                if tempHealth < 0:
                    tempHealth = 0
                print("As you take the bones, the switch lifts and they cling to your hand! You manage to prize them off, but your heart is still racing from the initial shock. At least the door ahead has opened.\n")
                time.sleep(2)
                print("Your health has decreased to " + str(tempHealth) + "!\n You now have 'old bones'!\n")
                time.sleep(2)
            elif inpt in ["2", "candle", "quill", "ceramic pillar", "middle pillar"]:
                inv.append("candle")
                inv.append("fancy quill")
                print("Gingerly taking the items, the switch lifts and the door ahead opens. It appears there were no repurcussions!\n")
                time.sleep(2)
                print("You now have 'candle' and 'fancy quill'!\n")
                time.sleep(2)
            elif inpt in ["3", "right pillar", "gold pillar", "jewels"]:
                inv.append("fake jewels")
                tempHealth -= 6
                if tempHealth < 0:
                    tempHealth = 0
                print("You hastily grab the jewels, and as you do, a spike protrudes from the pillar and goes through your hand! You inspect the jewels, hoping to take solace in your new gains - only to find they're fake.\n")
                time.sleep(2)
                print("Your health has decreased to " + str(tempHealth) + "!\n You now have 'fake jewels'!\n")
                time.sleep(2)
                
            inpt = input("'Proceed' to the next room, 'leave' the dungeon, 'check status', or 'use item'?\n").lower()
            time.sleep(1)

            if inpt in yesList or inpt in contList:
                print("You press on.\n")
                time.sleep(2)
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.\n")
                time.sleep(2)
                break
            elif inpt in ["use item"]:
                useItem()
                print("You press on.\n")
                time.sleep(2)
            elif inpt in ["check status", "status"]:
                status()
                print("You press on.\n")
                time.sleep(2)
            else:
                print(rjct)
                time.sleep(2)

##rest town
def tRest():
    global health
    global tempHealth
    global panache
    global force
    global coin

    townRest = True
    while townRest:

        inpt = input("Resting here will cost you 30 coin. Proceed?\n").lower()
        time.sleep(1)
        if inpt in yesList:
            if coin >= 30:
                tempHealth += 7
                if tempHealth > health:
                    tempHealth = health

                import random

                eventList = ["loot", "break in", "friend", "nothing"]
                restEvent = random.choice(eventList)

                print("You find a place in town to rest.\n")
                time.sleep(2)

                if restEvent == "break in":
                    print("You hear someone attempt to force the door open. Leaping up and grabbing your weapon, you shout to alert the guards. The person on the other side stops, and with guards now on the lookout you decide it is safe to go back to sleep.")
                    force += 3
                    time.sleep(2)
                    print("Your health has been restored to " + str(tempHealth) + ".")
                    time.sleep(2)
                    print("Your Force has increased to " + str(force) + ".\n")
                    time.sleep(2)
                    break

                elif restEvent == "friend":
                    print("You strike up a conversation with a charming patron. He imparts some wisdom before you head off to bed.")
                    time.sleep(2)
                    panache += 3
                    if panache < 0:
                        panache = 0
                    time.sleep(2)
                    print("Your health has been restored to " + str(tempHealth) + ".")
                    time.sleep(2)
                    print("Your Panache has increased to " + str(panache) + ".\n")
                    time.sleep(2)
                    break

                elif restEvent == "nothing":
                    print("Your rest is uneventful.")
                    time.sleep(2)
                    print("Your health has been restored to " + str(tempHealth) + ".\n")
                    time.sleep(2)
                    break

                elif restEvent == "loot":
                    print("As you enter your lodging, you notice it's previous occupier left some loose change. Finders Keepers!")
                    coin += 5 + (round(lvl / 3))
                    time.sleep(2)
                    print("Your health has been restored to " + str(tempHealth) + ".")
                    time.sleep(2)
                    print("You gained " + str(5 + (round(lvl / 3))) + " coin!\n")
                    time.sleep(2)
                    break

            elif coin < 30:
                print("You don't have enough coin! Try resting in the wilderness.\n")
                time.sleep(2)
                break

        elif inpt in noList:
            break
        
        else:
            print(rjct)

##rest wilderness
def wRest():
    global health
    global tempHealth
    global panache
    global force

    wildRest = True
    while wildRest:

        tempHealth += 5
        if tempHealth > health:
            tempHealth = health

        import random

        eventList = ["animal", "dream", "stranger", "nothing"]
        restEvent = random.choice(eventList)

        print("You set up camp in the wilderness to rest.\n")
        time.sleep(2)

        if restEvent == "animal":
            print("Just as you're dozing off, a fox seems disturbingly interested in some of your provisions. You don't wish to aggravate it, so you head back to sleep.")
            time.sleep(2)
            print("Your health has been restored to " + str(tempHealth) + ".")
            time.sleep(2)
            force -= 3
            if force < 0:
                force = 0
            print("Your Force has decreased to " + str(force) + ".\n")
            time.sleep(2)
            break

        elif restEvent == "dream":
            print("You toss and turn all night. Your dreams are plagued by thoughts of your family turning to ash. You don't have a family. Needless to say, this rest wasn't very productive.")
            time.sleep(2)
            tempHealth = health - 3
            print("Your health has only been restored to " + str(tempHealth) + "!\n")
            time.sleep(2)
            break

        elif restEvent == "stranger":
            print("A haggard stranger happens upon your camp. She shares some of her harrowing tales before departing, leaving you feeling uneasy.")
            time.sleep(2)
            print("Your health has been restored to " + str(tempHealth) + ".")
            time.sleep(2)
            panache -= 3
            if panache < 0:
                panache = 0
            print("Your Panache has decreased to " + str(panache) + ".\n")
            time.sleep(2)
            break

        elif restEvent == "nothing":
            print("Your rest is uneventful.")
            time.sleep(2)
            print("Your health has been restored to " + str(tempHealth) + ".\n")
            time.sleep(2)
            break

##check status
def status():
    global inv
    global coin
    global lvl
    global health
    global force
    global panache

    print("You are level {0}. Your health is currently at {1}. Your Force is at {2}, and your Panache is at {3}.".format(lvl, tempHealth, force, panache))
    time.sleep(2)
    print("The items in your pack are: " + (", ").join(inv) + ". You have " + str(coin) + " in coin.")
    time.sleep(2)
    print("Right now, you have " + str((", ").join(equipped.values())) + " equipped.\n")
    time.sleep(2)

##fighting
def fightMode():
    fight = True
    global health
    global opponentHealth
    global tempHealth
    global won
    global coin

    loot = (opponentHealth * 3)

    while fight == True:

        import random

        print("Your health is: ", tempHealth)
        print("Opponent's health is: ", opponentHealth)
        time.sleep(2)

        responseChoice = ["Aggressive", "Defensive", "Stealthy"]
        positionChoice = ["Defensive", "Stealthy", "Aggressive"]
        position = random.choice(positionChoice)
        print("\nYour opponent is taking a " + position + " stance.\n")
        time.sleep(2)
        p = positionChoice.index(position)

        inpt = input("How do you react? (1: Aggressive, 2: Defensive, 3: Stealthy)\n")

        if not inpt.isdigit():
            print("Invalid input - you forfeit your turn! Please type the NUMBER of the stance you wish to take.\n")
            tempHealth -= (1 + (round(opponentHealth / 3)))
            if tempHealth < 0:
                    tempHealth = 0
            print("That didn't work...\n")
            time.sleep(2)
            if opponentHealth <= 0:
                print("You won the fight!\n")
                time.sleep(2)
                won == True
                tempHealth = health
                coin += loot
                print("You gained " + str(loot) + " coin!")
                time.sleep(2)
                print("Your victory invigorates you - your health has been restored to " + str(tempHealth) + "!\n")
                time.sleep(2)
                break
            elif tempHealth <=0:
                print("You lost the fight!\n")
                time.sleep(2)
                won == False
                if coin >= (round(loot / 2)):
                    coin -= (round(loot / 2))
                    tempHealth = 3
                    print("You lost " + str(round(loot / 2)) + " coin!")
                    time.sleep(2)
                    print("You lost some health! Rest or use a potion to regain some health.\n")
                    time.sleep(2)
                else:
                    print("You don't even have enough coin to take!")
                    time.sleep(2)
                    print("You lost some health! Rest or use a potion to regain some health.\n")
                    time.sleep(2)
                break
            else:
                continue
            
        else:
            response = int(inpt) -1
    
            if response < 0 or response > 2:
                print("Invalid input - you forfeit your turn! Please type the NUMBER of the stance you wish to take.\n")
                tempHealth -= (1 + (round(opponentHealth / 3)))
                if tempHealth < 0:
                        tempHealth = 0
                print("That didn't work...\n")
                time.sleep(2)
                if opponentHealth <= 0:
                    print("You won the fight!\n")
                    time.sleep(2)
                    won == True
                    tempHealth = health
                    coin += loot
                    print("You gained " + str(loot) + " coin!")
                    time.sleep(2)
                    print("Your victory invigorates you - your health has been restored to " + str(tempHealth) + "!\n")
                    time.sleep(2)
                    break
                elif tempHealth <=0:
                    print("You lost the fight!\n")
                    time.sleep(2)
                    won == False
                    if coin >= (round(loot / 2)):
                        coin -= (round(loot / 2))
                        tempHealth = 3
                        print("You lost " + str(round(loot / 2)) + " coin!")
                        time.sleep(2)
                        print("You lost some health! Rest or use a potion to regain some health.\n")
                        time.sleep(2)
                    else:
                        print("You don't even have enough coin to take!")
                        time.sleep(2)
                        print("You lost some health! Rest or use a potion to regain some health.\n")
                        time.sleep(2)
                    break
                else:
                    continue
                
            else:
                print(responseChoice[response])
                time.sleep(1)

                if response == p:
                    opponentHealth -= round(dmg)
                    print("It worked!\n")
                    time.sleep(2)
                    if opponentHealth <= 0:
                        print("You won the fight!\n")
                        time.sleep(2)
                        won == True
                        tempHealth = health
                        coin += loot
                        print("You gained " + str(loot) + " coin!")
                        time.sleep(2)
                        print("Your victory invigorates you - your health has been restored to " + str(tempHealth) + "!\n")
                        time.sleep(2)
                        break
                    elif tempHealth <=0:
                        print("You lost the fight!\n")
                        time.sleep(2)
                        won == False
                        if coin >= (round(loot / 2)):
                            coin -= (round(loot / 2))
                            tempHealth = 3
                            print("You lost " + str(round(loot / 2)) + " coin!")
                            time.sleep(2)
                            print("You lost some health! Rest or use a potion to regain some health.\n")
                            time.sleep(2)
                        else:
                            print("You don't even have enough coin to take!")
                            time.sleep(2)
                            print("You lost some health! Rest or use a potion to regain some health.\n")
                            time.sleep(2)
                        break

                elif response != p:
                    tempHealth -= (1 + (round(opponentHealth / 3)))
                    if tempHealth < 0:
                        tempHealth = 0
                    print("That didn't work...\n")
                    time.sleep(2)
                    if opponentHealth <= 0:
                        print("You won the fight!\n")
                        time.sleep(2)
                        won == True
                        tempHealth = health
                        coin += loot
                        print("You gained " + str(loot) + "!")
                        time.sleep(2)
                        print("Your victory invigorates you - your health has been restored to " + str(tempHealth) + "!\n")
                        time.sleep(2)
                        break
                    elif tempHealth <=0:
                        print("You lost the fight!\n")
                        time.sleep(2)
                        won == False
                        if coin >= (round(loot / 2)):
                            coin -= (round(loot / 2))
                            tempHealth = 3
                            print("You lost " + str(round(loot / 2)) + " coin!")
                            time.sleep(2)
                            print("You lost some health! Rest or use a potion to regain some health.\n")
                            time.sleep(2)
                        else:
                            print("You don't even have enough coin to take!")
                            time.sleep(2)
                            print("You lost some health! Rest or use a potion to regain some health.\n")
                            time.sleep(2)
                        break
                    else:
                        continue 

##game
gameOn = True
fight = False

while gameOn == True:

    name = input("What is your name?\n")
    time.sleep(1)

    print("In this land, there are many different regions, each providing its citizens with unique benefits.\n")
    time.sleep(2)
    print("1. The 'mountains' are home to talented artisans; those from these rocky settlements tend to be more hardworking and robust.")
    time.sleep(2)
    print("2. The 'coast' is the cultural gem of the land, and its citizens are often more taken to extravagance and charisma than fighting.\n")
    time.sleep(2)

    inpt = input("From where do you hail, " + name +"?\n")
    time.sleep(1)
    if inpt in ["1", "mountain", "mountains", "mountain town", "artisans", "mountainous town", "mountainous"]:

        inv.append("worker's tools")
        force += 2
        background = "mountain"

    elif inpt in ["2", "coast", "coastal", "coast town", "culture", "coasts", "coastal town", "cultural town", "cultural"]:
        inv.append("fancy quill")
        panache += 2
        background = "coast"

    else:
        print("I've never heard of that place.")
        time.sleep(2)
        continue

    status()
    time.sleep(2)
    print("\nYour health determines how long you can fight before an enemy takes your money. Force increases the amount of damage you do to your enemies, which is increased by equipping hardy weapons. Panache increases your reputation, which provides better haggling prices at the market, and is increased by using fancier items. Increasing your level will increase your stats.\n")
    time.sleep(5)
    
    print("'" + name + ". Escape the Free Spirit. - J.B.'\n")
    time.sleep(2)
    print("Despite the vague nature of the note handed to you by the courier, something within you knew that it meant you had to leave. You hopped onto the first wagon out of your " + background + " town, beginning your search for answers.")
    time.sleep(2)
    print("However you've barely escaped the county when tragedy strikes! Your driver falls dead when an arrow is shot through his chest. Your eyes meet those of the attacker; a highwayman attempting to rob you!\n")
    time.sleep(2)

    opponentHealth = (round(8 + (lvl / 3)))
    fightMode()

    print("It's a shame your driver didn't make it, but you like to look on the bright side: You now have a wagon with which you can do whatever you want.\n")
    time.sleep(2)
    inv.append("wagon")

    explore1 = True
    while explore1:

        print("You know there's a nearby 'forest town' with a well-stocked market. If you think your skills could do with some work, there's a 'temple' that's likely to have trainers, but it's a bit of a ride. Or of course, you could always go on an 'adventure' to look for treasure.")
        time.sleep(2)
        print("Alternatively, you could: 'rest', 'use item', or 'look for trouble', or 'check status'.\n")
        time.sleep(2)

        inpt = input("What would you like to do?\n").lower()
        time.sleep(1)
        if inpt in ["forest town", "forest", "town"]:
            forestTown = True

            while forestTown:
                print("You are in the Forest Town.\n")
                time.sleep(2)
                print("The 'market' here is renowned for its forgiving economy. You wonder if it has anything to do with the convenient location; surrounded by major cities and only a short ride to the docks.")
                time.sleep(2)
                print("Alternatively, you could: 'rest', 'use item', or 'look for trouble', or 'check status'.\n")
                time.sleep(2)

                inpt = input("Where would you like to go?\n").lower()
                if inpt in ["market"]:
                    marketItems = ["health potion", "lockpick", "handaxe", "worker's tools", "candle"]
                    market()

                elif inpt in ["use item"]:
                    useItem()

                elif inpt in ["look for trouble"]:
                    import random

                    enemyList = ["bandit", "guardsman", "ruffian"]
                    opponent = random.choice(enemyList)
                    if opponent == "bandit":
                        opponentHealth = (round(8 + (lvl / 3)))
                    elif opponent == "guardsman":
                        opponentHealth = (round(12 + (lvl / 3)))
                    elif opponent == "ruffian":
                        opponentHealth = (round(4 + (lvl / 3)))

                    time.sleep(1)
                    print("You're itching for a fight, and you come across a rough-looking " + opponent + ". Get ready for a fight!\n")
                    time.sleep(2)
                    fightMode()

                elif inpt in ["check status", "status"]:
                    status()

                elif inpt in ["rest"]:
                    tRest()

                elif inpt in goList:
                    print("You leave the Forest Town.\n")
                    break

                else:
                    print(rjct)

        elif inpt in ["temple"]:
            temple = True

            while temple:
                print("You are at the Temple.\n")
                time.sleep(2)
                print("The air here is stiff with discipline. The local monks barely notice you as a kind lady takes you by the hand. She offers to show you around the Temple - she can take you directly to the 'monks', who can help train you. There's also a small 'market' here. You were hoping this place would be a little less tourist-y.")
                time.sleep(2)
                print("Alternatively, you could: 'rest', 'use item', or 'look for trouble', or 'check status'.\n")
                time.sleep(2)

                inpt = input("Where would you like to go?\n").lower()
                time.sleep(1)

                if inpt in ["market", "gift market", "shop", "store"]:
                    marketItems = ["sweet wine", "plain necklace"]
                    market()

                elif inpt in ["monks", "monk", "training", "train"]:
                    print("You visit the monks.\n")
                    time.sleep(2)
                    print("The Monks are willing to train you, for a fee. It's pricey, but you will level up.")
                    time.sleep(2)
                    inpt = input("Do you wish to train for " + str(150 + (round(lvl / 2))) + " coin?\n").lower()
                    time.sleep(1)
                    if inpt in yesList:
                        if coin >= 150 + (round(lvl / 2)):
                            coin -= 150 + (round(lvl / 2))
                            levelUp()
                        elif coin < 150 + (round(lvl / 2)):
                            print("You don't have enough coin to level up! Come back when you have enough coin.\n")
                            time.sleep(2)

                    elif inpt in noList:
                        print("You thank the monks for their time, and leave their presence.\n")
                        time.sleep(2)

                    else:
                        print(rjct)
                        time.sleep(2)

                elif inpt in ["use item"]:
                    useItem()

                elif inpt in ["look for trouble"]:
                    import random

                    enemyList = ["bandit", "guardsman", "ruffian"]
                    opponent = random.choice(enemyList)
                    if opponent == "bandit":
                        opponentHealth = (round(8 + (lvl / 3)))
                    elif opponent == "guardsman":
                        opponentHealth = (round(12 + (lvl / 3)))
                    elif opponent == "ruffian":
                        opponentHealth = (round(4 + (lvl / 3)))

                    time.sleep(1)
                    print("You're itching for a fight, and you come across a rough-looking " + opponent + ". Get ready for a fight!\n")
                    time.sleep(2)
                    fightMode()

                elif inpt in ["check status", "status"]:
                    status()

                elif inpt in ["rest"]:
                    tRest()

                elif inpt in goList:
                    print("You leave the Temple.\n")
                    time.sleep(2)
                    break

                else:
                    print(rjct)

        elif inpt in ["adventure"]:
            adventure()

        elif inpt in ["check status", "status", "check", "checkstatus"]:
            status()

        elif inpt in ["rest"]:
            wRest()

        elif inpt in ["use item", "use", "item"]:
            useItem()

        elif inpt in ["trouble", "look for trouble", "look for a fight"]:
            import random

            enemyList = ["bandit", "guardsman", "ruffian"]
            opponent = random.choice(enemyList)
            if opponent == "bandit":
                opponentHealth = (round(8 + (lvl / 3)))
            elif opponent == "guardsman":
                opponentHealth = (round(12 + (lvl / 3)))
            elif opponent == "ruffian":
                opponentHealth = (round(4 + (lvl / 3)))

            time.sleep(2)
            print("You're itching for a fight, and you come across a rough-looking " + opponent + ". Get ready for a fight!\n")
            fightMode()

        else:
            print(rjct)
            time.sleep(2)

##General Responses
rjct = ("You can't do that here.")

yesList = ["yes", "yeah", "y", "sure"]
noList = ["no", "nah", "nevermind", "n"]
goList = ["go back", "go", "leave", "go away"]

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
price = {"health potion": 35, "shortsword": 75, "handaxe": 65, "worker's tools": 15, "fancy quill": 15, "lockpick": 25, "wagon": 175, "sweet wine": 10, "plain necklace": 20, "love story": 5}
marketItems = ["sword", "axe"]

equipped = {"weapon": "shortword", "armour": "no armour"}
if "shortsword" in equipped:
    dmg += 1

if "handaxe" in equipped:
    dmg += 2

#if "plain necklace" in equipped:


#if "fancy quill" in equipped:

##Player Functions

##if panache >= (lvl * 10) and force >= (lvl * 10):
##    print("You've become so skilled that you've leveled up!")
##    levelUp()

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

    print("You leveled up! You are now level {0}. Your panache is at {1} and your force at {2}. You have {3} coin.".format(lvl, panache, force, coin))


##market
def market():
    global coin
    market = True

    while market:

        inpt = input("Do you wish to buy, sell, or leave? ").lower()

        if inpt in  ["buy", "purchase"]:
            inpt = input("The items on sale are: " + (", ").join(marketItems) + ". What do you want to buy? ").lower()
            if inpt in price:
                cost = price.get(inpt)
                item = inpt
                inpt = input("This will cost " + str(cost) + " coin. Proceed? ").lower()

                if inpt in yesList:
                    if coin >= cost:
                        coin -= cost
                        inv.append(item)
                        print("You are now the proud owner of a {0}. You have {1} coin.".format(item, coin))

                    else:
                        print("You don't have enough coin for that!")

                elif inpt in noList:
                    print("You decide not to buy.")

                elif inpt in goList:
                    print("You leave the market.")
                    break

                else:
                    print(rjct)

        elif inpt in ["sell", "give"]:
            inpt = input("In your inventory, you have " + (", ").join(inv) + ". What would you like to sell? ").lower()
            if inpt in inv:
                if inpt in price:
                    cost = price.get(inpt)
                    item = inpt
                    inpt = input("Sell your " + item + " for " + str(cost) + "? ").lower()
                    if inpt in yesList:
                        coin += cost
                        inv.remove(item)
                        print("You no longer have your " + item + ". You have " + str(coin) + " coin.")

                    elif inpt in noList:
                        print("You decide not to sell.")
                else:
                    print(rjct)

        elif inpt in goList:
            print("You leave the market.")
            break


        else:
            print(rjct)

##use item
def useItem():
    global tempHealth
    global health
    global panache
    global force

    use = True
    while use:
        inpt = input("You have " + (", ").join(inv) + ". What do you want to use? ").lower()

        if inpt in inv:

            if inpt in ["axe", "handaxe", "hand axe", "hand-axe"]:
                equipped["weapon"] = "handaxe"
                print("You equip your handaxe.")

            elif inpt in ["sword", "shortsword", "short sword", "short-sword"]:
                equipped["weapon"] = "shortsword"
                print("You equip your shortsword.")
            #- equipping item prints rjct
            elif inpt == "plain necklace":
                equipped["armour"] = "plain necklace"
                print("You equip your plain necklace.")

            elif inpt in ["health", "health potion", "potion", "drink potion", "drink health potion"]:
                tempHealth += 5
                inv.remove("health potion")
                if tempHealth > health:
                    tempHealth = health
                print("You drink the potion! Your health is now " + str(tempHealth) + ".")

            elif inpt in ["wine", "sweet wine", "drink wine", "drink sweet wine"]:
                panache += 3
                inv.remove("sweet wine")
                print("Your head feels funny. That was good wine - very good. Perhaps drinking the whole bottle was a bad idea. But you feel a lot more confident now. Your panache has increased to " + str(panache) + "!")

            elif inpt in ["mysterious note", "note", "letter"]:
                print("The letter reads: '" + name + ". Escape the Free Spirit. - J.B.' You don't know any J.B., but the letter gives off a weird energy. Perhaps it is the distinct smell of salted meat coming off of the page.")

            elif inpt in ["quill", "fancy quill", "pen"]:
                print("You pen a lovely letter. The words seem to flow spectacularly from your mind; it is a shame you have no one to send it to.")
                inv.append("flattering letter")
                print("You now have a 'flattering letter'!")

            elif inpt == "worker's tools":
                print("You find a chunk of wood on the ground and carve a small horse into it. What a charming little trinket.")
                inv.append("horse carving")
                print("You now have a 'horse carving'!")

            elif inpt == "love story":
                print("The stolen glances, mutual pining, breathless confessions... Oh my! This story is so beautifully written, it brings a tear to your eye.")

            else:
                print(rjct)

        elif inpt in goList:
            print("You close your pack and continue.")
            break

        else:
            print("You don't have that item...")
##adventure
def adventure():
    global opponentHealth
    global tempHealth
    global health
    global coin

    import time
    import random
    dungeonRooms = ["puzzle", "enemy", "journal", "loot", "pretty", "loop", "body", "nothing"]

    roomNum = random.randint(3,10)
    dungeon = True
    print("You enter the dungeon.\n")
    while dungeon:
        #- make this prettier
        time.sleep(2)
        currentRoom = random.choice(dungeonRooms)
        if roomNum <= 0:
            print("Dungeon end")
            break

        elif currentRoom == "nothing":
            roomNum -= 1
            print("There is nothing remarkable about this room.")
            inpt = input("Proceed to the next room?\n").lower()

            if inpt in yesList or inpt in contList:
                print("You press on.")
            elif inpt in goList or inpt in noList:
                print("You leave the dungeon.")
            #elif inpt in ["look", "look around", "stay"]:
                #- continues generating rooms
                #print("It's just a plain, empty room. The most interesting thing here is the spider crawling through a crack in the wall.")
            #else:
                #print(rjct)

##            progression()
        elif currentRoom == "enemy":
            roomNum -= 1
            opponentHealth = random.randint(3,15)
            print("You hear a dull thud of footsteps as you enter the next room. Barely illuminated by a nearby fire is a disturbingly tall creature, walking upright like a man but with antlers on its head, dripping with what appears to be a thick black... goo. \n Get ready for a fight!")
            fightMode()

        elif currentRoom == "journal":
            roomNum -= 1
            print("Scattered across the floor of the next room are pages from an adventurer's journal. Most of the pages are damaged beyond repair, but you can make out one of the accounts. It details a scandalous love affair! The participants are anonymous, but you pocket it anyway.")
            inv.append("love story")
            print("You now have a 'love story'!")

        elif currentRoom == "loot":
            roomNum -= 1
            print("Searching the next room, you catch something glinting in your torch light. Upon further inspection, it appears to be some loot! Score!\nYou gained 5 coin!")
            coin += 5

        elif currentRoom == "pretty":
            roomNum -= 1
            print("The next room is so strikingly beautiful. Moonlight barely graces the moss on the cracks of the stone walls, the cracked floor tracing a natural pattern. There's nothing else here, but you stop for a minute to take it all in.")

        elif currentRoom == "loop":
            roomNum += 1
            print("Wait a second - you've been here before! It appears that the dungeon has looped around and you've lost some progress.")

        elif currentRoom == "body":
            roomNum -= 1
            print("The next room you enter is quite dark. As you walk through, your foot hits something... odd. You shine your light on it, and discover a dead body! It's not fresh, but it's not old enough for you to be entirely comfortable with it either.")

        elif currentRoom == "puzzle":
            roomNum -= 1
            print("Three pillars stand before a locked door in this room, each with a switch held in place by a different object.\n1. On the left pillar, a pile of bones crumbles to dust atop a pedestal of rotting wood.\n2. The middle pillar is ceramic, with a candle and a feathered quill on top.\n3. The final pillar is solid gold, and on top is an assortment of fine jewels.\n")
            inpt = input("Which one do you take?\n").lower()
            if inpt in ["1"]:
                inv.append("old bones")
                tempHealth -= 4
                print("As you take the bones, the switch lifts and they cling to your hand! You manage to prize them off, but your heart is still racing from the initial shock. At least the door ahead has opened.\nYour health has decreased to " + str(tempHealth) + "!\n You now have 'old bones'!")
            elif inpt in ["2"]:
                inv.append("candle")
                inv.append("fancy quill")
                print("Gingerly taking the items, the switch lifts and the door ahead opens. It appears there were no repurcussions!\nYou now have 'candle' and 'fancy quill'!")
            elif inpt in ["3"]:
                inv.append("fake jewels")
                tempHealth -= 6
                print("You hastily grab the jewels, and as you do, a spike protrudes from the pillar and goes through your hand! You inspect the jewels, hoping to take solace in your new gains - only to find they're fake.\nYou now have 'fake jewels'!")


        ##print(roomNum, currentRoom)

##rest town
def tRest():
    global health
    global tempHealth
    global panache
    global force
    global coin

    townRest = True
    while townRest:

        inpt = input("Resting here will cost you 30 coin. Proceed? ").lower()
        if inpt in yesList:
            if coin >= 30:
                tempHealth += 7
                if tempHealth > health:
                    tempHealth = health

                import random

                eventList = ["loot", "break in", "friend", "nothing"]
                restEvent = random.choice(eventList)

                print("You find a place in town to rest.")

                if restEvent == "break in":
                    print("You hear someone attempt to force the door open. Leaping up and grabbing your weapon, you shout to alert the guards. The person on the other side stops, and with guards now on the lookout you decide it is safe to go back to sleep.")
                    force += 3
                    print("Your health has been restored to " + str(tempHealth))
                    print("Your Force has increased to " + str(force))
                    break

                elif restEvent == "friend":
                    print("You strike up a conversation with a charming patron. He imparts some wisdom before you head off to bed.")
                    panache += 3
                    if panache < 0:
                        panache = 0
                    print("Your health has been restored to " + str(tempHealth))
                    print("Your Panache has increased to " + str(panache))
                    break

                elif restEvent == "nothing":
                    print("Your rest is uneventful.")
                    print("Your health has been restored to " + str(tempHealth))
                    break

                elif restEvent == "loot":
                    print("As you enter your lodging, you notice it's previous occupier left some loose change. Finders Keepers!")
                    coin += 5 + (round(lvl / 3))
                    print("Your health has been restored to " + str(tempHealth))
                    print("You gained " + str(5 + (round(lvl / 3))) + " coin!")
                    break

            elif coin < 30:
                print("You don't have enough coin! Try resting in the wilderness.")
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

        print("You set up camp in the wilderness to rest.")

        if restEvent == "animal":
            print("Just as you're dozing off, a fox seems disturbingly interested in some of your provisions. You don't wish to aggravate it, so you head back to sleep.")
            print("Your health has been restored to " + str(tempHealth))
            force -= 3
            if force < 0:
                force = 0
            print("Your Force has decreased to " + str(force))
            break

        elif restEvent == "dream":
            print("You toss and turn all night. Your dreams are plagued by thoughts of your family turning to ash. You don't have a family. Needless to say, this rest wasn't very productive.")
            tempHealth = health - 3
            print("Your health has only been restored to " + str(tempHealth))
            break

        elif restEvent == "stranger":
            print("A haggard stranger happens upon your camp. She shares some of her harrowing tales before departing, leaving you feeling uneasy.")
            print("Your health has been restored to " + str(tempHealth))
            panache -= 3
            if panache < 0:
                panache = 0
            print("Your Panache has decreased to " + str(panache))
            break

        elif restEvent == "nothing":
            print("Your rest is uneventful.")
            print("Your health has been restored to " + str(tempHealth))
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
    print("The items in your pack are: " + (", ").join(inv) + ". You have " + str(coin) + " in coin.")
    #- prints keys not values
    print("Right now, you have " + str((", ").join(equipped.values())) + " equipped.")

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

        responseChoice = ["Aggressive", "Defensive", "Stealthy"]
        positionChoice = ["Defensive", "Stealthy", "Aggressive"]
        position = random.choice(positionChoice)
        print("Your opponent is taking a " + position + " stance.")
        p = positionChoice.index(position)

        response = int(input("How do you react? (1: Aggressive, 2: Defensive, 3: Stealthy) ")) -1
        print(responseChoice[response])

        if response == p:
            opponentHealth -= round(dmg)
            print("It worked!")
            if opponentHealth <= 0:
                print("You won the fight!")
                won == True
                tempHealth = health
                coin += loot
                break
            elif tempHealth <=0:
                print("You lost the fight!")
                won == False
                if coin >= (round(loot / 2)):
                    coin -= (round(loot / 2))
                    tempHealth = 3
                    print("You lost some coin!")
                else:
                    print("You don't even have enough coin to take!")
                break

#- response outside of defined parameters crashes (i.e. i accidentally typed "11" instead of "1"
        elif response != p:
            tempHealth -= 1 + (round(opponentHealth / 3))
            print("That didn't work...")
            if opponentHealth <= 0:
                print("You won the fight!")
                won == True
                tempHealth = health
                coin += loot
                break
            elif tempHealth <=0:
                print("You lost the fight!")
                won == False
                if coin >= (round(loot / 2)):
                    coin -= (round(loot / 2))
                    tempHealth = 3
                    print("You lost some coin!")
                    print("You lost some health! Rest or use a potion to regain some health.")
                else:
                    print("You don't even have enough coin to take!")
                break
            else:
                continue

##game
gameOn = True
fight = False

while gameOn == True:
    adventure()
    name = input("What is your name? ")

    print("In this land, there are many different regions, each providing its citizens with unique benefits.")
    print("1. The mountains are home to talented artisans; those from these rocky settlements tend to be more hardworking and robust.")
    print("2. The coast is the cultural gem of the land, and its citizens are often more taken to extravagance and charisma than fighting.")

    inpt = input("From where do you hail, " + name +"? ")
    if inpt == ("1"):

        inv.append("worker's tools")
        force += 2
        background = "mountain"

    elif inpt == ("2"):
        inv.append("fancy quill")
        panache += 2
        background = "coast"

    else:
        print("I've never heard of that place.")
        continue #- Continues from name, rather than background

    status()

    print("'" + name + ". Escape the Free Spirit. - J.B.'")
    print("Despite the vague nature of the note handed to you by the courier, something within you knew that it meant you had to leave. You hopped onto the first wagon out of your " + background + " town, beginning your search for answers.")
    print("However you've barely escaped the county when tragedy strikes! Your driver falls dead when an arrow is shot through his chest. Your eyes meet those of the attacker; a highwayman attempting to rob you!")

    opponentHealth = 8
    fightMode()

    print("It's a shame your driver didn't make it, but you like to look on the bright side: You now have a wagon with which you can do whatever you want.")
    inv.append("wagon")

    explore1 = True
    while explore1:

        print("You could probably sell this wagon off at a good price in the nearby 'Forest Town'. If you think your skills could do with some work, there's a 'Temple' that's likely to have trainers, but it's a bit of a ride. Or of course, you could always go on an 'Adventure' to look for treasure.")
        #print("Alternatively, you could: 'Rest', 'Use Item', or 'Look for Trouble', or 'Check Status'.")

        inpt = input("What would you like to do? ").lower()
        if inpt in ["forest town", "forest", "town"]:
            forestTown = True

            while forestTown:
                print("You are in the Forest Town.")
                print("The 'Market' here is renowned for its forgiving economy. You wonder if it has anything to do with the convenient location; surrounded by major cities and only a short ride to the docks.")
                print("Aside from the markets, there's plenty to do here. The 'Tavern' is rumoured to have all kinds of strange folks. 'The Governess' appears to be seeking strangers in an ambiguously vague task. You could always 'Go Back' or 'Travel Elsewhere'.")
                #print("Alternatively, you could: 'Rest', 'Use Item', 'Look for Trouble', or 'Check Status'.")

                inpt = input("What would you like to do? ").lower()
                if inpt in ["market"]:
                    marketItems = ["health potion", "lockpick"]
                    market()

                elif inpt in ["tavern"]:
                    print("tavern")

                elif inpt in ["governess", "the governess"]:
                    print("governess")

                elif inpt in ["rest"]:
                    tRest()

                elif inpt in ["travel", "travel elsewhere", "go elsewhere", "go somewhere else", "travel somewhere else"]:
                    print("travel")

                elif inpt in goList:
                    print("You leave the Forest Town.")
                    break

                else:
                    print(rjct)

        elif inpt in ["temple"]:
            temple = True

            while temple:
                print("You are at the Temple.")
                print("The air here is stiff with discipline. The local monks barely notice you as a kind lady takes you by the hand. She offers to show you around the Temple - she can take you directly to the 'Monks', who can help train you. Then again, she seems enthusiastic about showing you the priceless historical 'Artifacts'. There's also a small 'Market' here. You were hoping this place would be a little less tourist-y")

                inpt = input("Where would you like to go? ").lower()

                if inpt in ["market", "gift market", "shop", "store"]:
                    marketItems = ["sweet wine", "plain necklace"]
                    market()

                elif inpt in ["monks", "monk", "training", "train"]:
                    print("You visit the monks.")
                    print("The Monks are willing to train you, for a small price. 150 coin, to be exact. It's pricey, but you will level up.")
                    inpt = input("Do you wish to train for " + str(150 + (round(lvl / 2))) + " coin? ").lower()
                    if inpt in yesList:
                        if coin >= 150 + (round(lvl / 2)):
                            coin -= 150 + (round(lvl / 2))
                            levelUp()
                        elif coin < 150 + (round(lvl / 2)):
                            print("You don't have enough coin to level up! Come back when you have enough coin.")

                    elif inpt in noList:
                        print("You thank the monks for their time, and leave their presence.")

                    else:
                        print(rjct)

                elif inpt in goList:
                    print("You leave the Temple.")
                    break

                else:
                    print(rjct)

        elif inpt in ["adventure"]:
            print("Adventure")

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
                opponentHealth = 8
            elif opponent == "guardsman":
                opponentHealth = 12
            elif opponent == "ruffian":
                opponentHealth = 4

            print("You're itching for a fight, and you come across a rough-looking " + opponent + ". Get ready for a fight!")
            fightMode()

        else:
            print(rjct)

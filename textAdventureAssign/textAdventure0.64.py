##General Responses
rjct = ("You can't do that here.")

yesList = ["yes", "yeah", "y"]
noList = ["no", "nah", "nevermind", "n"]

goList = ["go back", "go", "leave", "go away"]

##Player's Stats
price = {"health potion": 35, "shortsword": 75, "handaxe": 65, "worker's tools": 15, "fancy quill": 15, "lockpick": 25}
marketItems = ["sword", "axe"]

inv = ["shortsword", "handaxe", "mysterious note"]
coin = 20
lvl = 0
health = 10
tempHealth = 10
force = 5
panache = 5
won = False

##Player Functions

##market
def market():
    global coin
    
    market = True
    while market:

        inpt = input("The items on sale are: " + (", ").join(marketItems) + ". What do you want to buy?").lower()
        if inpt in price:
            cost = price.get(inpt)
            item = inpt
            inpt = input("This will cost " + str(cost) + " coin. Proceed?").lower()
            
            if inpt in yesList:
                if coin >= cost:
                    coin -= cost
                    inv.append(item)
                    print("You are now the proud owner of a {0}. You have {1} coin.".format(item, coin))
                    continue
                else:
                    print("You don't have enough coin for that!")
                    continue
                
            elif inpt in noList:
                continue

            elif inpt in goList:
                print("You leave the market.")
                break
                
        elif inpt in goList:
            print("You leave the market.")
            break
            
        else:
            print("I don't understand.")
        
##use item

##rest town

##rest wilderness
def wRest():
    global health
    global tempHealth
    global panache
    global force

    rest = True
    while rest:

        tempHealth = health

        import random

        eventList = ["animal", "dream", "friend", "nothing"]
        restEvent = random.choice(eventList)

        print("You set up camp in the wilderness to rest.")

        if restEvent == "animal":
            print("Just as you're dozing off, a fox seems disturbingly interested in some of your provisions. You scare it off before heading back to sleep.")
            print("Your health has been restored to " + str(tempHealth))
            force += 1
            print("Your Force has increased to " + str(force))
            break

        elif restEvent == "dream":
            print("You toss and turn all night. Your dreams are plagued by thoughts of your family turning to ash. You don't have a family. Needless to say, this rest wasn't very productive.")
            tempHealth = (health - 3)
            print("Your health has only been restored to " + str(tempHealth))
            break
            
        elif restEvent == "friend":
            print("A charming stranger happens upon your camp. She shares some of her wisdom before departing.")
            print("Your health has been restored to " + str(tempHealth))
            panache += 1
            print("Your Panache has increased to " + str(panache))
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
    #inv - print join
    print("The items in your pack are: " + str(inv) + ". You have " + str(coin) + " in coin.")

##fight code
def fightMode():
    fight = True
    global health
    global opponentHealth
    global tempHealth
    global won
    global coin

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
            opponentHealth -= 1
            print("It worked!")
            if opponentHealth <= 0:
                print("You won the fight!")
                won == True
                tempHealth = health
                coin += 50
                break
            elif tempHealth <=0:
                print("You lost the fight!")
                won == False
                if coin >= 10:
                    coin -= 10
                    print("You lost some coin!")
                else:
                    print("You don't even have enough coin to take!")
                break

#- response outside of defined parameters crashes (i.e. i accidentally typed "11" instead of "1"
        elif response != p:
            tempHealth -= 1
            print("That didn't work...")
            if opponentHealth <= 0:
                print("You won the fight!")
                won == True
                tempHealth = health
                coin += 50
                break
            elif tempHealth <=0:
                print("You lost the fight!")
                won == False
                if coin >= 10:
                    coin -= 10
                    health += 3
                    print("You lost some coin!")
                    print("You lost some health! Rest or use a potion to regain some health.")
                else:
                    print("You don't even have enough coin to take!")
                break
            else:
                continue
            
##end of fight code

gameOn = True
fight = False

while gameOn == True:

    name = input("What is your name? ")

    print("In this land, there are many different regions, each providing its citizens with unique benefits.")
    print("1. The mountains are home to talented artisans; those from these rocky settlements tend to be more hardworking and robust.")
    print("2. The coast is the cultural gem of the land, and its citizens are often more taken to extravagance and charisma than fighting.")

    inpt = input("From where do you hail, " + name +"? ")
    if inpt == ("1"):

        inv.append("Worker's Tools")
        force += 2
        background = "mountain"

    elif inpt == ("2"):
        inv.append("Fancy Quill")
        panache += 2
        background = "coast"

    else:
        print("I've never heard of that place.")
        continue #- Continues from name, rather than background

    status()
    
    print("'" + name + ". Escape the Free Spirit. - J.B.'")
    print("Despite the vague nature of the note handed to you by the courier, something within you knew that it meant you had to leave. You hopped onto the first airship out of your " + background + " town, beginning your search for answers.")
    print("However you've barely escaped the county when tragedy strikes! Your driver falls dead when an arrow is shot through his chest. Your eyes meet those of the attacker; a highwayman attempting to rob you!")

    opponentHealth = 3
    #fightMode()

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
                ##print("Alternatively, you could: 'Rest', 'Use Item', 'Look for Trouble', or 'Check Status'.")
                
                inpt = input("What would you like to do? ").lower()
                if inpt in ["market"]:
                    fMarket = True
                    while fMarket:
                        print("You are in the Market.")
                        print("There is so much for sale, yet a few items in particular catch your eye. Health potions and lock picks are a particularly good price today. Some merchants eye you up; you could probably get a good deal for some items in your bag. Or you could go back.")
                        marketItems = ["health potion", "lockpick"]
                        market()

                elif inpt in ["tavern"]:
                    print("tavern")

                elif inpt in ["governess", "the governess"]:
                    print("governess")

                elif inpt in ["travel", "travel elsewhere", "go elsewhere", "go somewhere else", "travel somewhere else"]:
                    print("travel")

                elif inpt in ["go back", "go", "leave", "go away"]:
                    print("You leave the Forest Town.")
                    break
                else:
                    print(rjct)
                
        elif inpt in ["temple"]:
            print("temple")
        elif inpt in ["adventure"]:
            print("Adventure")
        elif inpt in ["check status", "status", "check", "checkstatus"]:
            status()
        #- Probably gonna break loop/bring back to name - add while loop?
        elif inpt in ["rest"]:
            wRest()
        else:
            print(rjct)

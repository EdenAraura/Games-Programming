##General responses
rjct = ("I don't understand.")

##Player's stats
inv = ["shortsword", "handaxe", "mysterious note"]
coin = 200
lvl = 0
health = 10
tempHealth = 10
force = 5
panache = 5
won = False

##Player functions

##rest town

##rest wilderness

##check status
def status():
    global inv
    global coin
    global lvl
    global health
    global force
    global panache

    print("You are level " + str(lvl) + ". Your health is currently at " + str(health) + ". Your Force is at " + str(force) + ", and your Panache is at " + str(panache) + ".")
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
        print(position)
        p = positionChoice.index(position)

        response = int(input("What is your response? (1: Aggressive, 2: Defensive, 3: Stealthy)")) -1
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
            else:
                continue

## response outside of defined parameters crashes (i.e. i accidentally typed "11" instead of "1"
        else:
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

    name = input("What is your name?")

    print("In this land, there are many different regions, each providing its citizens with unique benefits.")
    print("1. The mountains are home to talented artisans; those from these rocky settlements tend to be more hardworking and robust.")
    print("2. The coast is the cultural gem of the land, and its citizens are often more taken to extravagance and charisma than fighting.")

    inpt = input("From where do you hail, " + name +"?")
    if inpt == ("1"):

        inv.append("worker's tools")
        force += 2
        background = "mountain"

    elif inpt == ("2"):
        inv.append("fancy quill")
        panache += 2
        background = "coast"

    else:
        print(rjct)
        continue #- Continues from name, rather than background

    status()
    
    print(name + ". Escape the Free Spirit. - J.B.")
    print("Despite the vague nature of the note handed to you by the courier, something within you knew that it meant you had to leave. You hopped onto the first airship out of your " + background + " town, beginning your search for answers.")
    print("However you've barely escaped the county when tragedy strikes! Your driver falls dead when an arrow is shot through his chest. Your eyes meet those of the attacker; a highwayman attempting to rob you!")

    opponentHealth = 3
    fightMode()

    #- "won" not defined? Defined within function
    #if won == True:
        #print("winner")
    print("It's a shame your driver didn't make it, but you like to look on the bright side: You now have a wagon with which you can do whatever you want.")

    explore1 = True
    while explore1:
        
        print("You could probably sell this wagon off at a good price in the nearby 'Forest Town'. If you think your skills could do with some work, there's a 'Temple' that's likely to have trainers, but it's a bit of a ride. Or of course, you could always go on an 'Adventure' to look for treasure.")
        #print("Alternatively, you could: 'Rest', 'Use Item', or 'Look for Trouble', or 'Check Status'.")
        
        inpt = input("What would you like to do?").lower()
        if inpt in ["forest town", "forest", "town"]:
            forestTown = True
            
            while forestTown:
                print("You are in the Forest Town.")
                print("The 'Market' here is renowned for its forgiving economy. You wonder if it has anything to do with the convenient location; surrounded by major cities and only a short ride to the docks.")
                print("Aside from the markets, there's plenty to do here. The 'Tavern' is rumoured to have all kinds of strange folks. 'The Governess' appears to be seeking strangers in an ambiguously vague task. Of course, you could always 'Go Back' or 'Travel Elsewhere'.")
                ##print("Alternatively, you could: 'Rest', 'Use Item', 'Look for Trouble', or 'Check Status'.")
                
                inpt = input("What would you like to do?").lower()
                if inpt in ["market"]:
                    fMarket = True
                    while fMarket:
                        print("There is so much for sale; a few items in particular catch your eye. Potions, worker's tools, fancy quill, sell item, go back")

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
                    print("You can't do that here.")
                
        elif inpt in ["temple"]:
            print("temple")
        elif inpt in ["adventure"]:
            print("Adventure")
        elif inpt in ["check status", "status", "check", "checkstatus"]:
            status()
        ##Probably gonna break loop/bring back to name - add while loop?
        else:
            print("You can't do that here.")

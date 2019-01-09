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
#- When printing status, it prints as the status is orginially declared in the "player's stats" section
#status = ("You are level " + str(lvl) + ". Your health is currently at " + str(health) + ". Your force is at " + str(force) + ", and your panache is at " + str(panache) + ".")
#inventory = ("The items in your pack are: " + str(inv) + ". You have " + str(coin) + " in coin.")

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

    
    print("You are level " + str(lvl) + ". Your health is currently at " + str(health) + ". Your force is at " + str(force) + ", and your panache is at " + str(panache) + ".")
    print("The items in your pack are: " + str(inv) + ". You have " + str(coin) + " in coin.")
    
    print(name + ". Escape the Free Spirit. - J.B.")
    print("Despite the vague nature of the note handed to you by the courier, something within you knew that it meant you had to leave. You hopped onto the first airship out of your " + background + " town, beginning your search for answers.")
    print("However you've barely escaped the county when tragedy strikes! Your driver falls dead when an arrow is shot through his chest. Your eyes meet those of the attacker; a highwayman attempting to rob you!")

    opponentHealth = 3
    fightMode()

    #- "won" not defined? Defined within function
    ##if won == True:
        ##print("winner")
    
    print("It's a shame your driver didn't make it, but you like to look on the bright side: You now have a wagon with which you can do whatever you want.")
    print("You could probably sell this thing off easily in the 'Forest Town', but it's a bit of a drive. If you think your skills could do with some work, there's a nearby 'Temple' that's likely to have trainers. Or of course, you could always go on an 'Adventure' to look for treasure.")
    ##Add "check status"
    print("Alternatively, you could: 'Rest', 'Use Item', or 'Look for Trouble'.")
    
    inpt = input("What would you like to do?").lower()
    if inpt in ["forest town", "forest", "town"]:
        print("foresT")
    elif inpt in ["temple"]:
        print("temple")
    elif inpt in ["adventure"]:
        print("Adventure")
    else:
        print("You can't do that here.")

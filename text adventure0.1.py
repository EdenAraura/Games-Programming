game = True

inv = ["dagger", "axe"]
northList = ["north", "n"]
yesList = ["y", "yes", "yeah"]

while game == True:

    inp = input("which direction would you like to go?").lower()

    ##north
    if inp in northList:

        print("You encounter an enemy! It hasn't seen you yet...")
        inp = input("Will you fight?").lower()

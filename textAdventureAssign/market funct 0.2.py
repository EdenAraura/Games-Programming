price = {"Health Potion": 35, "Shortsword": 75, "Hand-Axe": 65, "Worker's Tools": 15, "Fancy Quill": 15, "lockpick": 25}
marketItems = ["health", "pick"]
coin = 200

inpt = input("The items on sale are: " + (", ").join(marketItems) + "What do you want to buy?").lower()
#print(price.getinpt)
#print(inpt)
cost = price.get(inpt)
item = inpt
inpt = input("This will cost " + str(cost) + " coin. Proceed?").lower()
    
if inpt in yesList:
    coin -= cost
    inv.append(item)
    print("You now have {0} in your inventory. You have {1} coin.".format(item, coin))
        

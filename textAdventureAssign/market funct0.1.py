price = {"Health Potion": 35, "Shortsword": 75, "Hand-Axe": 65, "Worker's Tools": 15, "Fancy Quill": 15, "Lockpick": 25}

def market():
    market = True
    while market:

        import random
        random.shuffle(price)
        print(price[2])

market()

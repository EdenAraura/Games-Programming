x=input ("say something!")

if len(x) >=3 and x[-3:] == "ing":
    print(x+"ly")
elif len(x) >= 3:
    print(x+"ing")
else:
    print(x)


## List comprehension: [expression for value in collection]

##youtube tutorial
    #squares = [x**2 for x in range(1,101)]
        #squares = []
        #for x in range(1,101):
            #squares.append(x**2)


shows = ["curious", "farewell", "medea", "boots", "beth"]

##prints "True, True, False, False
#longTitles = [len(x) >= 6 for x in shows]

#longTitles = []
    #for x in shows:
        #if len(x) >=6:
            #longTitles.append(x)

longTitles = [x for x in shows if len(x) >= 6]

print(longTitles)


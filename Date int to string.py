dateNum = input("What is the date? (dd/mm/yyyy)")

spaces = dateNum.replace("/", " ")

dateList = spaces.split()

day = int(dateList[0])
month = int(dateList[1])
year = int(dateList[2])

wrong = "That's not a real date..."

if day < 1 & day > 31:
    for x in dateList:
        if x[1] == "01":
            print("It is the ", day, "of January, ", year)

        elif x[1] == "02":
            print("It is the ", day, "of February, ", year)
            
        elif x[1] == "03":
            print("It is the ", day, "of March, ", year)
            
        elif x[1] == "04":
            print("It is the ", day, "of April, ", year)
            
        elif x[1] == "05":
            print("It is the ", day, "of May, ", year)
            
        elif x[1] == "06":
            print("It is the ", day, "of June, ", year)
            
        elif x[1] == "07":
            print("It is the ", day, "of July, ", year)
            
        elif x[1] == "08":
            print("It is the ", day, "of August, ", year)
            
        elif x[1] == "09":
            print("It is the ", day, "of September, ", year)
            
        elif x[1] == "10":
            print("It is the ", day, "of October, ", year)
            
        elif x[1] == "11":
            print("It is the ", day, "of November, ", year)
            
        elif x[1] == "12":
            print("It is the ", day, "of December, ", year)

        else:
            print(wrong)
else:
    print(wrong)

## Always prints wrong

#skips the for conditions
datenum = input("What is the date today? (dd/mm/yyyy)")

spaces = datenum.replace("/"," ")

dateList = spaces.split()

day = int(dateList[0])

month = dateList[1]

year = int(dateList[2])

wrong = "That's not a real date..."

if day < 1 or day > 31:
    print(wrong)
    
for x in dateList:

    if x[1] == "01":
        print("January the",day,",",year)
            
    elif x[1] == "02":
        if day <= 29:
            print("February the",day,",",year)
        else:
            print(wrong)
           
    elif x[1] == "03":
        print("March the",day,",",year)
   
    elif x[1] == "04":
        if day <= 30:
            print("April the",day,",",year)
        else:
            print(wrong)
   
    elif x[1] == "05":
        print("May the",day,",",year)
   
    elif x[1] == "06":
        if day <= 30:
            print("June the",day,",",year)
        else:
            print(wrong)
   
    elif x[1] == "07":
        print("July the",day,",",year)
   
    elif x[1] == "08":
        print("August the",day,",",year)
   
    elif x[1] == "09":
        print("September the",day,",",year)

    elif x[1] == "10":
        print("October the",day,",",year)

    elif x[1] == "11":
        if day <=30:
            print("November the",day,",",year)
        else:
            print(wrong)

    elif x[1] == "12":
        print("December the",day,",",year)

    else:
        break

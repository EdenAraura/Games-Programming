datenum = input("What is the date today? (dd/mm/yyyy)")

spaces = datenum.replace("/"," ")

dateList = spaces.split()

day = int(dateList[0])

month = dateList[1]

year = int(dateList[2])

wrong = False

wrongStr = "That's not a real date..."

if day < 1:
    wrong == True
    
if day > 31:
    wrong == True

for x in dateList:

    if x[1] == "01":
        month == "January"
            
    elif x[1] == "02":
        if day <= 29:
            month == "February"
        else:
            wrong == True
           
    elif x[1] == "03":
        month == "March"
   
    elif x[1] == "04":
        if day <= 30:
            month == "April"
        else:
            wrong == True
   
    elif x[1] == "05":
        month == "May"
   
    elif x[1] == "06":
        if day <= 30:
            month == "June"
        else:
            wrong == True
   
    elif x[1] == "07":
        month == "July"
   
    elif x[1] == "08":
        month == "August"
   
    elif x[1] == "09":
        month == "September"

    elif x[1] == "10":
        month == "October"

    elif x[1] == "11":
        if day <=30:
            month = "November"
        else:
            wrong == True

    elif x[1] == "12":
        month == "December"

    else:
        wrong == True

if wrong == False:
    print("It is the",day,"of",month,",",year)
else:
    print("okay")


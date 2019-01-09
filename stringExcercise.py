str = "hi chi a"

sepList = str.split(" ")
hiList = []

for x in sepList(len(str)-1):
    if x == "h":
        hiList.append(x)

print(hiList)

print(len(hiList))

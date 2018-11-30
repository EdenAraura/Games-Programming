list = ["mix", "xyz", "apple", "xanadu", "rovio"]
a = []
b = []
for y in list:
    if y[0] == "x":
        a.append(y)
    else:
        b.append(y)
print(sorted(a)+sorted(b))

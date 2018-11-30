inv = ["axe", "dagger", "oranges"]

for x in inv:
    if len(x) >= 1:
        inv.append("*")

print(inv)

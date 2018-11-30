tuple = [(), (), ('',), ("a", "b", "c"), ("d")]
return_tuple = []

for x in tuple:
    if x:
        return_tuple.append(x)

print(return_tuple)

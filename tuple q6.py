tuple = (1, 2, 3, 4)
newtuple = ()


for i in range(len(tuple)):
    if i == 1:  # When index is 1, modify the value
        newtuple += (20,)
    else:
        tuple += (tuple[i],)

print("Modified tuple:", tuple)

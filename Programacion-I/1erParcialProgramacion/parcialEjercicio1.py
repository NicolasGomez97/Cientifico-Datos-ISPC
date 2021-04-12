d1 = [1, 2, 3]
d2 = [3, 2, 4]
d3 = []

for i in d1:
    for j in d2:
        if i == j:
            d3.append(i*i*i)

print(d3)
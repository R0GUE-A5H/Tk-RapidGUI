x = {"Button 1": [48, 34], "Button 2": [54, 120], "Button 3": [52, 212], "Button 4": [482, 121], "Button 5": [464, 32]}
count = 0

for i, j in x.items():
    y = i[:i.index(' ')]
    if y == "Button":
        count += 1
for i in range(count):
        print(i)

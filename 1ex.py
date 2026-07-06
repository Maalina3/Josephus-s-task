n = int(input())
circle = []

for i in range(1, n + 1):
    circle.append(i)

start_delete = True
while len(circle) != 1:    
    if start_delete: 
        new_circle = circle[::2]
    else:
        new_circle = circle[1::2]

    if new_circle[-1] == circle[-1]:
        start_delete = False
    else:
        start_delete = True
    
    circle = new_circle

print(*circle)
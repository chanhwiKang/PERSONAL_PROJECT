emergency = []
result = [len(emergency)]
emergency = [1, 2, 3, 4, 5, 6, 7]
point = 0
i = 1

for _ in range(len(emergency)-1):
    result.append(1)
    
while True:
    point = emergency.index(max(emergency))
    emergency[point] = 0
    result[point] = i
    i += 1
    if max(emergency) == 0:
        break

print(result)
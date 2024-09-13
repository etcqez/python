list01 = [3, 7, 5, 7, 9, 35, 20, 10, 8]
for outer in range(len(list01) - 1):
    for inner in range(outer + 1, len(list01)):
        if list01[outer] > list01[inner]:
            list01[outer], list01[inner] = list01[inner], list01[outer]

print(list01)
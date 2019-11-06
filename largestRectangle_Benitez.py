def largestRectangle(h):
    buildingStack = [-1]
    greatestArea = 0

    for a in range(len(h)):
        while(buildingStack[-1] != -1 and h[buildingStack[-1]] >= h[a]):
            lastElement = buildingStack.pop()
            greatestArea = max(greatestArea, h[lastElement] * (a - buildingStack[-1] - 1))
        buildingStack.append(a)

    
    while buildingStack[-1] != -1:
        lastElement = buildingStack.pop()
        greatestArea = max(greatestArea, h[lastElement] * (len(h) - buildingStack[-1] - 1))
    return greatestArea


n = int(input())
h = list(map(int, input().rstrip().split()))
result = largestRectangle(h)
print(str(result) + '\n')


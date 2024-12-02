#leftList = [3, 4, 2, 1, 3, 3]
#rightList = [4, 3, 5, 3, 9, 3]

with open('Day1/leftList.txt', 'r') as leftListFile:
    leftList = [int(num) for num in leftListFile.read().split()]

with open("Day1/rightList.txt", 'r') as rightListFile:
    rightList = [int(num) for num in rightListFile.read().split()]

# ascending order
leftList.sort()
rightList.sort()

# absolute distance using sorted lists
totalDistance = sum(abs(left - right) for left, right in zip(leftList, rightList))

print("Total Distance:", totalDistance)


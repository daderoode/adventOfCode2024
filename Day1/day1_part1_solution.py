#leftList = [3, 4, 2, 1, 3, 3]
#rightList = [4, 3, 5, 3, 9, 3]

with open('Day1/leftList.txt', 'r') as leftListFile, open('Day1/rightList.txt', 'r') as rightListFile:
    totalDistance = sum(abs(left - right) for left, right in zip(sorted(map(int, leftFile)), sorted(map(int, rightFile))))
print("Total Distance:", totalDistance)

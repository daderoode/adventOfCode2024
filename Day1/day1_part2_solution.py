# leftList = [3, 4, 2, 1, 3, 3]
# rightList = [4, 3, 5, 3, 9, 3]

with open('Day1/leftList.txt', 'r') as leftListFile:
    leftList = [int(num) for num in leftListFile.read().split()]

with open("Day1/rightList.txt", 'r') as rightListFile:
    rightList = [int(num) for num in rightListFile.read().split()]

similarityScore = 0

for num in leftList:
    count_right = rightList.count(num)
    similarityScore += num * count_right


print("Similarity:", similarityScore)
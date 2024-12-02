with open('Day2/input.txt', 'r') as f:
    data = [list(map(int, line.split())) for line in f.read().splitlines()]
    print("Data: ",data)

def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))

    return increasing or decreasing

safe = 0
for report in data:
    if is_safe(report):
        print("Safe Report: ",report)
        safe += 1
    elif ()

# Output the result
print("Number of safe report:", safe)

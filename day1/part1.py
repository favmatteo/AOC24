list1 = []
list2 = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        num1, num2 = line.strip().split()
        list1.append(int(num1))
        list2.append(int(num2))


res = 0
while len(list1) > 0 and len(list2) > 0:
    min1 = min(list1)
    min2 = min(list2)
    list1.remove(min1)
    list2.remove(min2)
    res += abs(min1 - min2)

print(res)

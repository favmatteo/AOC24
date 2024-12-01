list1 = []
list2 = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        num1, num2 = line.strip().split()
        list1.append(int(num1))
        list2.append(int(num2))


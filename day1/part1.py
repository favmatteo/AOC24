list1 = []
dict2 = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        num1, num2 = line.strip().split()
        num2 = int(num2)
        list1.append(int(num1))
        if num2 in dict2:
            dict2[int(num2)] += 1
        else:
            dict2[num2] = 1

print(dict2)

res = 0
for el in list1:
    if el in dict2:
        print(el, dict2[el])
        res += el * dict2[el]

print(res)

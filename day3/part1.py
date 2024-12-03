import re
file = "input.txt"
with open(file, "r") as f:
    output = f.readlines()

tot = 0
for line in output:
    x = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)
    for mul in x:
        param1 = mul[4:mul.index(',')]
        param2 = mul[mul.index(',')+1:-1]
        tot += int(param1) * int(param2)

print(tot)
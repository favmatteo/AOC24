import re

file = "input.txt"
with open(file, "r") as f:
    output = f.readlines()

tot = 0
activate = True
regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)"
for line in output:
    x = re.findall(regex, line)
    for ins in x:
        if ins == 'do()':
            activate = True
        elif ins == "don't()":
            activate = False
        elif activate:
            param1 = ins[4:ins.index(',')]
            param2 = ins[ins.index(',')+1:-1]
            tot += int(param1) * int(param2)

    pass

print(tot)

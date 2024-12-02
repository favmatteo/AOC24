reports = []


def is_increasing(list):
    return list == sorted([el for el in set(list)])


def is_decreasing(list):
    return list == sorted([el for el in set(list)])[::-1]


def check_max_difference_level(list):
    el = list[0]
    for curr in list[1:]:
        if abs(el - curr) > 3:
            return False
        el = curr
    return True


with open("input.txt", "r") as f:
    for line in f.readlines():
        reports.append([int(el) for el in line.strip().split()])

cnt = 0
for report in reports:
    if (is_increasing(report) or is_decreasing(report)) and check_max_difference_level(
        report
    ):
        cnt += 1

print(cnt)

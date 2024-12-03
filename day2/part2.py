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
    else:
        # prova rimuovendo 
        # prova a rimuovere ogni elemento e vedere se è ok
        temp_report: list = report.copy()
        for i in range(len(report)):
            temp_report.pop(i)
            if (is_increasing(temp_report) or is_decreasing(temp_report)) and check_max_difference_level(temp_report):
                cnt+=1
                break
            temp_report = report.copy()

print(cnt)


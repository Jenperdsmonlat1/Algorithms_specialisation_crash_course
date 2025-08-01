with open("jobs.txt", "r") as file:

    lines = file.readlines()

jobs = []
number_tasks = int(lines[0])
print(number_tasks)

for line in lines[1:]:
    job = line.split()
    jobs.append((int(job[0]), int(job[1])))


def greedy_sort(tasks):
    
    sorted_tasks = sorted(tasks, key=lambda job: job[0] / job[1], reverse=True)
    current = 0
    sum = 0

    for weight, length in sorted_tasks:
        current += length
        sum += weight * current

    return sum

print(greedy_sort(jobs))
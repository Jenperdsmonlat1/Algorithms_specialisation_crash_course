
with open("2_sum.txt", "r") as file:
    data = set(int(line.strip()) for line in file)


def two_sum(array, minimum, maximum):

    set_numbers = array
    valid_target = []

    for t in range(minimum, maximum + 1):
        for x in set_numbers:
            y = t - x

            if y != x and y in set_numbers:
                valid_target.append(t)
                print(t)
                break
    
    return len(valid_target)

number = two_sum(data, -10000, 10000)
print(number)
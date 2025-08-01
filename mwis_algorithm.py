
with open("mwis.txt", "r") as file:
    lines = file.readlines()

n = int(lines[0])
weights = [int(line) for line in lines[1:]]
print(n)

A = [0] * (n + 1)
A[0] = 0
A[1] = weights[0]

for i in range(2, n + 1):
    A[i] = max(A[i - 1], A[i - 2] + weights[i - 1])


selected = set()
i = n

while i >= 1:
    if A[i - 1] >= A[i - 2] + weights[i - 1]:
        i -= 1
    else:
        selected.add(i)
        i -= 2

check_vertices = [1, 2, 3, 4, 17, 117, 517, 997]
bits = ['1' if v in selected else '0' for v in check_vertices]
answer = ''.join(bits)
print(answer)
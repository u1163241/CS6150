import random
import math

tList = [40000, 90000, 160000]
answer = []
for i in tList:
    temp = []
    for r in range(50):
        current = 0
        prev = 0
        count = 0
        for t in range(i):
            rand = random.randint(0, 1)
            if rand == 0:
                current -= math.sqrt(t)
            else:
                current += math.sqrt(t)
            if prev * current < 0:
                count += 1
            prev = current
        temp.append(count)
    answer.append(sum(temp) / len(temp))
print(answer)

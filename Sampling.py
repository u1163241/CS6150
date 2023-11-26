import random

sList = [20, 100, 400, 1000]
answer = []
for i in sList:
    temp = []
    for r in range(100):
        count = 0
        for t in range(i):
            rand = random.randint(0, 1000000)
            if rand <= 520000:
                count += 1
        if count > (i / 2):
            temp.append(1)
        else:
            temp.append(0)
    answer.append(sum(temp) / len(temp))
print(answer)

#랜덤 뽑기

import random

count = 0

while True:
    r = random.randint(1,100)
    print(r)
    count += 1

    if r == 77:
        break

print(str(count) + "번만에 뽑기 성공!")
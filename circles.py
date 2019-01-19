import math


c1 = [int(el) for el in input().split()]
c2 = [int(el) for el in input().split()]
distance = math.sqrt(math.fabs(c1[0] - c2[0]) ** 2 + math.fabs(c1[1] - c2[1]) ** 2)
if distance > c1[2] + c2[2]:
    print('NO')
else:
    print('YES')

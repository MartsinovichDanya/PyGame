r1 = [int(el) for el in input().split()]
r2 = [int(el) for el in input().split()]

xlt1, ylt1, xrb1, yrb1 = r1[0], r1[1], r1[0] + r1[2], r1[1] + r1[3]
xlt2, ylt2, xrb2, yrb2 = r2[0], r2[1], r2[0] + r2[2], r2[1] + r2[3]

if xlt1 > xrb2 or xrb1 < xlt2 or ylt1 > yrb2 or yrb1 < ylt2:
    print('NO')
else:
    print('YES')

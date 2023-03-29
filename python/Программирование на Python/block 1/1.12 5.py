a, b, c = int(input()), int(input()), int(input())
if a <= b <= c:
    print(c)
    print(a)
    print(b)
elif a >= b <= c and c >= a:
    print(c)
    print(b)
    print(a)
elif a >= b <= c and c <= a:
    print(a)
    print(b)
    print(c)
elif a <= b >= c and a >= c:
    print(b)
    print(c)
    print(a)
elif a <= b >= c and a <= c:
    print(b)
    print(a)
    print(c)
else:
    print(a)
    print(c)
    print(b)
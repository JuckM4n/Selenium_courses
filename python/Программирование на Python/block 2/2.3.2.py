a, b = int(input()), int(input())
#a, b = (int(i) for i in input().split())
s = 0
n = 0
for i in range (a, b +1):
    if i % 3 == 0:
        s += i
        n += 1
print(s / n)

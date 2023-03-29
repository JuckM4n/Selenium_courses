import math
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = p * (p - a) * (p - b) * (p - c)
sqrt = math.sqrt(S)
print(sqrt)
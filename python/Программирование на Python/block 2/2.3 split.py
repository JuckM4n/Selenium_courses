#Решение 1
a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range (a, b + 1):
    if i % 2 == 1:
        s += i
print(s)



#Решение 2
a, b = input().split()
a = int(a)
b = int(b)
s = 0
if a % 2 == 0:
    a += 1
for i in range (a, b +1,2):
    s += i
print(s)

#Решение 3
a, b = (int(i) for i in input().split()) #выводит все числа в одной строке
s = 0
if a % 2 == 0:
    a += 1
for i in range (a, b +1,2):
    s += i
print(s)
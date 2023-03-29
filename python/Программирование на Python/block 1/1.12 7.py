# put your python code here
i = int(input())
a = i % 10
b = i % 100 // 10
c = i % 1000 // 100
d = i % 10000 // 1000
e = i % 100000 // 10000
f = i % 1000000 // 100000
if a + b + c == d + e + f:
    print ("Счастливый")
else:
    print("Обычный")

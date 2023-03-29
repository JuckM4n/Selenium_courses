#мой длинный вариант
genome = input()
cnt = 0
count = 0
p = 0
percent = 100
for nucl in genome.upper():
    p += 1
    if nucl == "C":
        cnt += 1
    elif nucl == "G":
        count += 1
s = cnt + count
out = s / p * percent
print(out)

#сокращенный вариант
s = input().upper()
print((s.count('G')+s.count('C')) / len(s) * 100)

st = input()
cnt = 0

j = len(st)
i = 0

while i < j:
    if i == 0 or st[i] == st[i - 1]:
        cnt += 1
    else:
        print(st[i - 1] + str(cnt), end="")
        cnt = 1
    i += 1
print(st[i - 1] + str(cnt))
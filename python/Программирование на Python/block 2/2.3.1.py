a,b,c,d = int(input()),int(input()),int(input()),int(input())
for j in range(c, d + 1):
    print('\t', j, end = '', sep = '')
for i in range(a, b + 1):
    print()
    print(i, end = '\t')
    for g in range (c, d + 1):
        print(i * g, end = '\t')
print()


a,b,c,d = int(input()),int(input()),int(input()),int(input())
print('', *range(c, d+1), sep='\t')
for i in range(a,b+1):
    print(i, *range(i*c,(i*d)+1, i), sep='\t')
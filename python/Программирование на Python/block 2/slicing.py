from re import I


dna = 'ATTCGGAGCT'
dna[1] -> 'T'
dna[1:4] -> 'TTC'
dna[:4] -> 'ATTC'
dna[4:] -> 'GGAGCT'
dna[-4:] -> 'AGCT'
dna[1:-1] -> 'TTCGGAGC'
dna[1:-1:2] -> 'TCGG'
dna[::-1] -> 'TCGAGGCTTA' (символы в обратном порядке)

#Задача с палиндромом
s = input()
i = 0
j = len(s) - 1
is_palindrom = True
while i < j:
    if s[i] != s[j]:
        is_palindrom = False
    i += 1
    j -= 1
if is_palindrom:
    print('YES')
else:
    print('NO')
    
#Задача с палиндромом в которой процесс обрывается если False => немного оптимизирован    
s = input()
i = 0
j = len(s) - 1
is_palindrom = True
while i < j:
    if s[i] != s[j]:
        is_palindrom = False
        break
    i += 1
    j -= 1
if is_palindrom:
    print('YES')
else:
    print('NO')
    
#Короткий вариант, но сильно загружает память, если большие строки    
s = input()
r = s[::-1]
if s == r:
    print('YES')
else:
    print('NO')
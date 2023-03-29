genome = "ATGG"
for i in range (4):
    print(genome[i], end=' ')
    
genome = "ATGG"
for c in genome:
    print(c, end=' ')
    
    
genome = input()
cnt = 0
for nucl in genome:
    if nucl == "C":
        cnt += 1
print(cnt)

genome = input()
print(genome.count("C"))
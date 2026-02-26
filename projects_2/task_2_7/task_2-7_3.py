seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]

for nucleotides in seq:
    if nucleotides.endswith(('A')):
     print(nucleotides, end='')
else:
    print()

for nucleotides in seq:
    for letter in nucleotides:
     print(letter)
          
print('Цикл выполнен')         


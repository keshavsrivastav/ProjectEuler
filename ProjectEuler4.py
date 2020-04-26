prod=0
counter=0
palindromes=[]
for i in range(100,999):
    for j in range(100,999):
        prod = 0
        prod = i * j
        prod=str(prod).split()[0]
        if len(prod) == 6:
            if prod[0] == prod[-1] and prod[1] == prod[-2] and prod[2] == prod[-3]:
                palindromes.append(prod)

print(max(palindromes))
    

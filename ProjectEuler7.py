def primeNonPrime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
            break        
    return True

    

counter=-1
for i in range(1,10000000000):
    if primeNonPrime(i)==True:
        counter+=1
        if counter==10001:
            print(i)
            break
    


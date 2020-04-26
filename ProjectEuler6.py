numsqu=0
sumofnumsqu=0
for i in range(1,101):
    numsqu = i * i
    sumofnumsqu+=numsqu
    # print(sumofnumsqu)

sumofnum=0
for j in range(1,101):
    sumofnum+=j
    # print(sumofnum)

sumofnum=sumofnum*sumofnum

print(sumofnum-sumofnumsqu)
    
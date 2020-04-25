# print(sum([i for i in range(3999999) if i%2==0]))
def fibb():
    num1=0
    num2=1
    num3=0
    result=0
    while num3<4000000:
        num3=num1+num2
        num1=num2
        num2=num3
        if num3%2==0:
            result+=num3
    
    print(result)

fibb()
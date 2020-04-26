
def devisbleFind(num):
    for i in range(11,21):
        if num % i != 0:
            return False
    return True

number=1
while True:
    if devisbleFind(number):
        break
    else:
        number+=1

print(number)



# check_list = [11, 13, 14, 16, 17, 18, 19, 20]

# def find_solution(step):
#     for num in xrange(step, 999999999, step):
#         if all(num % n == 0 for n in check_list):
#             return num
#     return None

# if __name__ == '__main__':
#     solution = find_solution(20)
#     if solution is None:
#         print "No answer found"
#     else:
#         print "found an answer:", solution
def isMultipleOf(number):
    if number % 3 == 0:
        return True
    if number % 5 == 0:
        return True
    return False

numbers = filter(isMultipleOf,range(1000))
print(sum(numbers))
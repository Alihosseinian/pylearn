def is_factorial(num):
    i = 1
    factorial = 1

    while factorial < num:
        i += 1
        factorial *= i

    if factorial == num:
        return "yes"
    else:
        return "no"

user_input = int(input("plesae enter your numner : "))

result = is_factorial(user_input)
print(result)

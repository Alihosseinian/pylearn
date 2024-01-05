def print_diamond(n):
    if n % 2 == 0:
        n += 1  

    for i in range(n):
        spaces = abs(n // 2 - i)
        stars = n - 2 * spaces
        print(" " * spaces, end="")
        print("*" * stars)

n = int(input("please enter the Number: "))

print_diamond(n)

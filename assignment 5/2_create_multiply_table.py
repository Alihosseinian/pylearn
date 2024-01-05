def print_multiplication_table(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result = i * j
            print(f"{i} * {j} = {result}\t", end="")
        print()

n = 10
m = 10
print_multiplication_table(n, m)

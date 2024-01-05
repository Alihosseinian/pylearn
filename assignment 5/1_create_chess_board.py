def print_chessboard(n, m):
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                print("*", end="")
            else:
                print("#", end="")
        print()

n = 4
m = 9
print_chessboard(n, m)

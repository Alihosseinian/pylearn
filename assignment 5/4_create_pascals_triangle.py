def generate_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

n = int(input("please enter the number: "))

pascals_triangle_result = generate_pascals_triangle(n)

print_pascals_triangle(pascals_triangle_result)

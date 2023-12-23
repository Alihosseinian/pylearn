def draw_snake(n):
    snake = ""
    for i in range(n):
        if i % 2 == 0:
            snake += "*"
        else:
            snake += "#"
    return snake

n = int(input("please enter size of the snake : "))

snake_pattern = draw_snake(n)
print(snake_pattern)

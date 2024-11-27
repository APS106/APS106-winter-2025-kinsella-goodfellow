import math

def quadratic(a, b, c):
    d = b ** 2 - 4 * a
    disc = sqrt(d)
    root1 = (-b + disc) / (2 * a)
    root2 = (-b - disc) / (2 * a)
    return root1, root2

continue_string = 'y'  # initial input

while continue_string != 'n':
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    result = quadratic(a, b, c)
    print(result)
    continue_string = input("Do you want to calculate again? (y/n)")

# test cases
# a = 1, b = -14, c = 45
# a = 1, b = 6, c = 9
# a = 1, b = 4, c = 5
def triangle(n):

    for i in range(1, n + 1):

        spaces = ' ' * (n - i)
        hashes = '#' * (2 * i - 1)

        print(spaces + hashes + spaces)

if __name__ == "__main__":
    n = int(input("Enter the size of the triangle: "))
    triangle(n)
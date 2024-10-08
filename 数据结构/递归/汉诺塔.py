def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, b, c)
        print("moving from %s to %s" % (a, b))
        hanoi(n - 1, a, b, c)

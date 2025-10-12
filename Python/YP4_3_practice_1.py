def countdown(n):
    if n <= 0:
        print("Старт!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
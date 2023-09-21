def multiplication_table():
    for i in range(1, n+1):
        print(1, "*", i, "=", i)


n = int(input("Введите число N: "))
result = multiplication_table()
print(result)

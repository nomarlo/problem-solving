t = int(input())

while t:
    result = True
    n = int(input())

    numbers = []
    while n:
        n1 = input()
        numbers.append(n1)

        n = n - 1

    numbers.sort()

    for i in range(len(numbers) - 1):
        if numbers[i + 1].startswith(numbers[i]):
            result = False
            break

    if result:
        print("YES")
    else:
        print("NO")

    t = t - 1

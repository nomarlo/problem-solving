t = int(input())

for _ in range(t):

    n = int(input())    
    letters = {}
    for _ in range(n):
        letter, price = input().split()
        letters[letter] = int(price)

    payment = 0
    l = int(input())
    for _ in range(l):
        line = input()
        payment += sum(map(lambda letter: letters[letter] if letter in letters else 0, line))

    print("{:.2f}$".format(payment/100))

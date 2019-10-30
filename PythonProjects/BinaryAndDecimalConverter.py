number, system = map(int, input().split())
if system == 10:
    a = []
    b = ""
    while (number // 2) != 0:
        a.append(number % 2)
        number = number // 2
    a.append(1)
    b = "".join(str(i) for i in a[::-1])
    print(b, 2)
elif system == 2:
    c = str(number)
    j = 1
    n = 0
    while j <= len(c):
        for i in c:
            n = n + int(i)*(2**(len(c)-j))
            j+=1
    print(n, 10)
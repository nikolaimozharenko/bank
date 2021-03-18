while True:
    a = int(input("Число: "))
    p = float(input("Процент в десятичной дроби: "))
    d = input("Сложные или простые проценты(+ для простых, - для сложных): ")
    n = int(input("Сколько раз выполнять операцию: "))
    result = int
    if d == "+":
        c1 = n * p
        c2 = 1 + c1
        c3 = a * c2
        result = c3
    elif d == "-":
        c1 = 1 + p
        c2 = c1 ** n
        c3 = a * c2
        result = c3
    print(result)
    
        
        

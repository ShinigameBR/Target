def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n:
        return True
    else:
        return False

num = int(input("Digite um número: "))
if fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
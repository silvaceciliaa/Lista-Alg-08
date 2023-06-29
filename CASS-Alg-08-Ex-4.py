def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        resultado = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = resultado
        return resultado

def main():
    n = int(input("Digite um valor inteiro: "))
    
    resultado = fibonacci(n)

    print(resultado)

main()

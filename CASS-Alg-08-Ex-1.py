def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
def main():
    n = int(input("Digite um número inteiro: "))
    resultado = fatorial(n)
    print(f"O fatorial de {n} é: {resultado}")

main()

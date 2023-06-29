def compactar(dados, contador=1):
    if not dados:
        return []

    primeiro = dados[0]

    if len(dados) > 1 and dados[1] == primeiro:
        return compactar(dados[1:], contador + 1)
    else:
        result = [str(contador), primeiro]

        return result + compactar(dados[1:])


def main():
    dados = input("Digite a string a ser compactada: ")

    compactdo = compactar(dados)

    print("Resultado codificado em run-length:", "".join(compactdo))

main()

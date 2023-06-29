def descompactarLista(lista):
    listaDescompactada = []
    i = 0

    while i < len(lista):
        valor = lista[i]
        if isinstance(valor, int):
            if i + 1 < len(lista):  
                elemento = lista[i+1]
                listaDescompactada.extend([elemento] * valor)
                i += 2
            else:
                break
        else:
            listaDescompactada.append(valor)
            i += 1

    return listaDescompactada


def main():
    lista_codificada = ["A", 12, "B", 4, "A", 6, "B", 1]
    listaDescompactada = descompactarLista(lista_codificada)

    print("Lista Codificada:", lista_codificada)
    print("Lista Descompactada:", listaDescompactada)


main()

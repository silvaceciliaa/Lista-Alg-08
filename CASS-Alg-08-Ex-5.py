def main():
    def somar():
        valores = input("Digite um valor e tecle ENTER para parar: ")
        
        if valores == "":
            return 0.0
        
        valor = int(valores)
        somarResto = somar()
        
        return valor + somarResto
    
    total = somar()
    print(total)

main()

from unidecode import unidecode
import re

def ePalindromo(caracteres):
    def limparCaracteres(caracteres):
        caracteresSemAcento = unidecode(caracteres)
        caracteresSemPontuação = re.sub(r'[^a-zA-Z0-9]', '', caracteresSemAcento)
        caracteresLimpos = caracteresSemPontuação.lower().replace(" ", "")
        return caracteresLimpos
    

    def checagem(caracteres):
        if len(caracteres) <= 1:
            return "É palíndromo"

        if caracteres[0] == caracteres[-1]:
            return checagem(caracteres[1:-1])
        else:
            return "Não é palíndromo"

    caracteresLimpos = limparCaracteres(caracteres)
    return checagem(caracteresLimpos)

def main():
    caracteres = input("Digite uma palavra ou frase: ")
    print(ePalindromo(caracteres))
main()
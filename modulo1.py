#Função para ler somente números inteiros
def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO: Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("\nUsuário não digitou nenhum número.")
            return 0
        else:
            return n

#Funções para realização do MENU
def linha(tam=42):
    return "-" * tam

def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(c, "-", item)
        c += 1
    print(linha())
    opção = leiaInt("Escolha uma opção: ")
    return opção


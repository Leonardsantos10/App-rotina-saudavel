import modulo1
import json

pessoa = dict()

#Função para saber se existe um arquivo já criado
def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
#Função para criar um arquivo
def criarArquivo(nome):
    try:
        a = open(nome, "w")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print("Arquivo", nome,"criado com sucesso!")
#Função para ler o arquivo criado
def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        modulo1.cabeçalho("CADASTRO DE INFORMAÇÕES")
        print(a.read())
    finally:
        a.close()


#Funções para criar uma lista formato json
def Salvar_json(lista):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(lista, f)


def carregar_json(arquivo):
    with open(arquivo, 'r+') as f:
        return json.load(f)


def cadastrar(arq, nome, peso, altura, idade, sexo, objetivo):
    f = open('texto.json', 'r+')
    f.truncate(0)
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO durante a abertura do programa!")
    else:
        try:
            minha_lista = {'nome':nome, 'peso':peso, 'altura':altura, 'idade':idade, 'sexo':sexo, 'objetivo':objetivo}
            Salvar_json(minha_lista)
        except:
            print("Houve um ERRO na hora de escrever os dados")
        else:
            print("Novo registro de", nome," adicionado")
            a.close()
            

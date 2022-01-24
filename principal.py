import modulo1
import arquivo1
import math
from time import sleep
agua_ingerida = 0
kcal_total = 0
kcal_gasta = 0

arq = "meu_arquivo.json"

if not arquivo1.arquivoExiste(arq):
    arquivo1.criarArquivo(arq)

while True:
    resposta = modulo1.menu(["Mostrar Cadastro","Atualizar Cadastro", "Registro de alimentação", "Registro de Hidratação", "Registro de atividade física", "Sair do programa"])
    #Mostrar Cadastro caso exista um feito
    if resposta == 1:
        retorno = arquivo1.carregar_json(arq)
        print(retorno)
    #Entrar com opções para cadastro   
    elif resposta == 2:
        modulo1.cabeçalho("Opção 2")
        nome = str(input("Digite seu nome: "))
        peso = float(input("Digite seu peso atual(Kg): "))
        altura = int(input("Digite sua altura(Cm): "))
        idade = int(input("Digite sua idade: "))
        sexo = str(input("Digite seu sexo(M/F): "))
        objetivo = int(input("Qual o seu objetivo:\n1. Emagrecer\n2. Manter o peso\n3. Ganhar massa\nSelecione uma opção: "))
        arquivo1.cadastrar(arq, nome, peso, altura, idade, sexo, objetivo)
    #Registro de alimentação
    elif resposta == 3:
        modulo1.cabeçalho("Opção 3")
        retorno = arquivo1.carregar_json(arq)

        if retorno["sexo"] in 'Ff':
            metabolismo_basal = 655 + (9.6 * retorno["peso"]) + (1.8 * retorno["altura"]) - (4.7 * retorno["idade"])
        elif retorno["sexo"] in 'Mm':
            metabolismo_basal = 66 + (13.8 * retorno["peso"]) + (5 * retorno["altura"]) - (6.8 * retorno["idade"])
                    
        if retorno["objetivo"] == 1:
                  if kcal_gasta != 0:
                            meta = metabolismo_basal + kcal_gasta - 500
                  else:
                            meta = metabolismo_basal - 500
        elif retorno["objetivo"] == 2:
                  if kcal_gasta != 0:
                            meta = metabolismo_basal + kcal_gasta
                  else:
                            meta = metabolismo_basal
        elif retorno["objetivo"] == 3:
                  if kcal_gasta != 0:
                            meta = metabolismo_basal + kcal_gasta + 500
                  else:
                            meta = metabolismo_basal + 500
        adicionar_alimento = 1

        while adicionar_alimento == 1:
                  str(input("\nNome do alimento: "))
                  kcal_ingerida = float(input("Digite a quantidade de calorias do alimento ingerido: "))
                  kcal_total = kcal_total + kcal_ingerida

                  adicionar_alimento = int(input("\nDeseja adicionar outro alimento(Digite 1 ou 2)\n1. Sim\n2. Não\n: "))

        print("\nVocê consumiu {} Kcal de {} Kcal para atingir sua meta diária".format('%.2f' % kcal_total,'%.2f' % meta))
    #Registro de Hidratação    
    elif resposta == 4:
        modulo1.cabeçalho("Opção 4")
        retorno = arquivo1.carregar_json(arq)
        meta_diaria = 35 * retorno["peso"]

        adicionar_agua = int(input("Digite a quantidade de água ingerida(ml): "))
        agua_ingerida = agua_ingerida + adicionar_agua
        restante = meta_diaria - agua_ingerida
        excesso = agua_ingerida - meta_diaria

        if meta_diaria >= agua_ingerida:
                  print("Você ingeriu {} ml de agua hoje, faltam {} ml para atingir a sua meta diária".format(agua_ingerida, restante))
        elif meta_diaria < agua_ingerida:
                  print("Meus parabés, você atingiu sua meta diária de hidrtação. Bebeu {} ml além da meta".format(excesso))
        else:
                  print("ERRO! Tente novamente")
    #Registro de Atividade física               
    elif resposta == 5:
        modulo1.cabeçalho("Opção 5")
        retorno = arquivo1.carregar_json(arq)
        atividade = int(input("\nOpções de exercícios\n1. Corrida\n2. Caminhada\n3. Pular corda\n4. Futebol\n5. Natação\n6. Tae kwon do\n7. Aeróbico de Alto impacto\n8. Basquete\n9. Hidroginastica\n10. Yoga\n11. Outros\nSelecione seu exercício: "))
        tempo_atividade = int(input("Qual o tempo, em minutos, de duração da atividade: "))

        if atividade == 1:
                  kcal_gasta = tempo_atividade * 16.11
        elif atividade == 2:
                  kcal_gasta = tempo_atividade * 8.2
        elif atividade == 3:
                  kcal_gasta = tempo_atividade * 16.11
        elif atividade == 4:
                  kcal_gasta = tempo_atividade * 14.07
        elif atividade == 5:
                  kcal_gasta = tempo_atividade * 13.39
        elif atividade == 6:
                  kcal_gasta = tempo_atividade * 14.07
        elif atividade == 7:
                  kcal_gasta = tempo_atividade * 9.97
        elif atividade == 8:
                  kcal_gasta = tempo_atividade * 10.93
        elif atividade == 9:
                  kcal_gasta = tempo_atividade * 7.52
        elif atividade == 10:
                  kcal_gasta = tempo_atividade * 5.46
        elif atividade == 11:
                  nome_atividade = str(input("\nNome do exercício: "))
                  kcal_gasta = int(input("Digite a quantidade de calorias gastas no exercício: "))
        else:
                  print("Opção inválida!")

        print("\nVocê gastou {} Kcal em exercícios físicos\n".format(kcal_gasta))
    #Opção para sair do programa   
    elif resposta == 6:
        modulo1.cabeçalho("Saindo do sistema.. Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida.")
    sleep(1.5)

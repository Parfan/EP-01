# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Felipe Lacombe,  felipeml4@al.insper.edu.br
# - aluno B: Willian Asanuma, williankal@al.insper.edu.br
# - aluno C: Gabriel Parfan,  gabrielpg1@al.insper.edu.br

import json
from random import randint

def carregar_cenarios():
    with open('arquivo_cenarios.py','r') as arquivo_cenarios:
        arquivo1 = arquivo_cenarios.read()
    cenarios = json.loads(arquivo1)
    nome_cenario_atual = "saguao"
    return cenarios, nome_cenario_atual

def randomize():
    random1a3 = randint(1,3)
    random1a6 = randint(1,6)
    return random1a3, random1a6

def carregar_monstros():
    lista_habilidades = [1,2]
    lista_monstros = [1,2,3,4]
    monstros = {
        lista_monstros[0]: {
            "Nome": "Seguranca",
            "Pontos de vida": 12,
            "Habilidades": {
                lista_habilidades[0] : 1,
                lista_habilidades[1] : 2
            }
        },
        lista_monstros[1]: {
            "Nome": "Faxineira ninja",
            "Pontos de vida": 8,
            "Habilidades": {
                lista_habilidades[0] : 2,
                lista_habilidades[1] : 3
            }
        },
        lista_monstros[2]: {
            "Nome": "Professor",
            "Pontos de vida": 10,
            "Habilidades": {
                lista_habilidades[0] : 1,
                lista_habilidades[1] : 2
            }
        },
        lista_monstros[3]: {
            "Nome": "Coordenador",
            "Pontos de vida": 10,
            "Habilidades": {
                lista_habilidades[0] : 1,
                lista_habilidades[1] : 2
            }
        }
        
    }
    enfrentando_monstro = lista_monstros[1]
    return monstros, enfrentando_monstro

def itens():
    item = {
        "carteirinha": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "catraca": "Passar pela catraca",
                "biblioteca": "Ir para a biblioteca",
                "desistir": "Desistir e ir embora"
            }
        },
        "atestado": {
            "titulo": "O portao giratorio",
            "descricao": "Voce esta nas catracas do Saguao do perigo",
            "opcoes": {
                "saguao": "Voltar ao Saguao do perigo",
                "elevador": "Ir para o transportador magico",
                "escada": "Ir para a escadaria do infinito"
            }
        },
        "faca": {
            "titulo": "Apoio",
            "descricao": "Voce subiu a Escadaria do infinito e agora está no 2o andar",
            "opcoes": {
                "catraca": "Voltar para o portao giratorio",
                "corredor andar 2": "Ir para o corredor do segundo andar"
            }
        }    
    }
    return item

def funcao_inventario(item):
    mochila=[]
    mochila.append(item)
    return mochila

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa ideia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print("------------------------------------------------------------")
    print("Digite 'opcao' ou 'opcoes' para ver os comandos disponíveis.")
    print("------------------------------------------------------------")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    monstros, enfrentando_monstro = carregar_monstros()
    random1a3, random1a6 = randomize()
    
    game_over = False
    i = 0
    
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        
        opcoes = cenario_atual['opcoes']

        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            for k, v in opcoes.items():
                print(f"* '{k}' ({v})")
            escolha = input("Escolha a sua opção: ")
            print()
            if escolha == 'desistir':
                game_over = True
            else:
                while escolha not in opcoes:
                    if escolha == 'opcao' or escolha == 'opcoes':
                        for k, v in opcoes.items():
                            print(f"* '{k}' ({v})")
                        escolha = input("Escolha a sua opção: ")
                        print()
                    elif escolha == '':
                        escolha = input("Oops, acho que você se esqueceu de digitar um comando: ")
                        if escolha == 'desistir':
                            game_over = True
                        print()
                    else:
                        print("Não conheço esta opção... :/")
                        escolha = input("Escolha a sua opção: ")
                        if escolha == 'desistir':
                            game_over = True
                        print()
                if escolha in opcoes:
                    nome_cenario_atual = escolha
                    #game_over = True
                if nome_cenario_atual == "biblioteca":
                    print(random1a3)
                    print(i)
                    if random1a3 == 1:
                        while i < 3:
                            cenarios["biblioteca"]["descricao"] = "Você entra Santuario da sabedoria e derrepente se depara com um objeto cúbico peculiar..."
                            cenarios["biblioteca"]["opcoes"] = {"dado misterioso": "Pegar dado misterioso no chao"}
                            i+=1

    if escolha == 'desistir':
        print("Você desistiu de tentar o adiamento, foi embora e pegou DP!")
    else:
        print("Você morreu!")
  
# Programa principal.
if __name__ == "__main__":
    main()

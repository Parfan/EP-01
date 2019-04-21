# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Felipe Lacombe,  felipeml4@al.insper.edu.br
# - aluno B: Willian Asanuma, williankal@al.insper.edu.br
# - aluno C: Gabriel Parfan,  gabrielpg1@al.insper.edu.br

import json
from colorama import *

def carregar_cenarios():
    with open('arquivo_cenarios.py','r') as arquivo_cenarios:
        arquivo1 = arquivo_cenarios.read()
    cenarios = json.loads(arquivo1)
    nome_cenario_atual = "saguao"
    return cenarios, nome_cenario_atual

def carregar_monstros():
    lista_habilidades = [1,2]
    lista_monstros = [1,2,3,4]
    monstros = {
        lista_monstros[0]: {
            "Nome": "Seguranca",
            "Vida": 12,
            "Dano": [2,3]
        },
        lista_monstros[1]: {
            "Nome": "Faxineira ninja",
            "Vida": 8,
            "Dano": {
                lista_habilidades[0] : 2,
                lista_habilidades[1] : 3
            }
        },
        lista_monstros[2]: {
            "Nome": "Professor",
            "Vida": 10,
            "Dano": {
                lista_habilidades[0] : 1,
                lista_habilidades[1] : 2
            }
        },
        lista_monstros[3]: {
            "Nome": "Veterano",
            "Vida": 10,
            "Dano": {
                lista_habilidades[0] : 1,
                lista_habilidades[1] : 2
            }
        }
    }
    return monstros

'''def combate(enfrentando_monstro):
    vida_inimigo = enfrentando_monstro["Vida"]
    ataque_inimigo = enfrentando_monstro["Dano"]
    return vida_inimigo, ataque_inimigo'''

def combate(i,vida,item):
    vida_inimigo = monstros[lista_monstros[i]]["Vida"]
    ataque_inimigo = monstros[lista_monstros[i]]["Dano"]
    print("Você entrou em combate com {0}!".format(monstros[lista_monstros[i]]["Nome"]))
    print("Sua vida: {0}".format(vida))
    print(f"Vida do inimigo: {vida_inimigo}")
    while vida > 0 or vida_inimigo > 0:
        dano_inimigo = monstros[lista_monstros[i]]["Dano"][randint(0,1)]
        vida_inimigo-=item["punhos"]["dano"]
        print("Você bate no inimigo com {0} e deixa o inimigo com {1} de vida!".format(item["punhos"]["titulo"],vida_inimigo))
        if vida_inimigo <= 0:
            break
        vida-=dano_inimigo
        print("{0} te bate e te deixa com {1} de vida".format(monstros[lista_monstros[i]]["Nome"],vida))
    if vida_inimigo <= 0 and vida > 0:
        print("Você venceu a luta!")
    elif vida <= 0:
        print("Você perdeu a luta!")
    return vida, vida_inimigo

def inventario():
    mochila = []
    return mochila

def itens():
    item = {
    "carteirinha": {
        "titulo": "Carteirinha de estudante",
        "dano": 0
        },
    "atestado": {
        "titulo": "Atestado medico",
        "dano": 5
        },
    "punhos": {
        "titulo": "Próprias mãos",
        "dano": 3
        }
    }
    return item

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

    game_over = False
    seguranca_allow = 1
    vida = 20
    i = 0
    escolha = "saguao"
    nome = input("Antes de começar a sua jornada em busca do adiamento do EP...\nDigite seu nome: ")
    while len(nome) == 0:
        nome = input("Não seja tímido, diga seu nome: ")
    print()
    
    cenarios, nome_cenario_atual = carregar_cenarios()
    monstros = carregar_monstros()
    item = itens()
    #vida, vida_inimigo = combate(i,vida,item)
    mochila = inventario()
    
    while not game_over and escolha != "desistir":
        
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print("--- OPÇÕES ---")
        
        opcoes = cenario_atual['opcoes']

        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            for k, v in opcoes.items():
                print(f"* '{k}' ({v})")
            escolha = input("Escolha a sua opção: ")
            print()
            while escolha not in opcoes:
                if escolha == 'opcao' or escolha == 'opcoes':
                    for k, v in opcoes.items():
                        print(f"* '{k}' ({v})")
                    escolha = input("Escolha a sua opção: ")
                    print()
                else:
                    escolha = input("Não conheço esta opção... :/\n\nEscolha a sua opção: ")
            if escolha in opcoes:
                nome_cenario_atual = escolha
                if nome_cenario_atual == "catraca" and "carteirinha" not in mochila:
                    print(Fore.RED + "Você não está com sua carteirinha, portanto não pode passar pela catraca!")
                    print(Fore.RESET)
                    nome_cenario_atual = "saguao"
                elif escolha == "achados e perdidos":
                    if "carteirinha" not in mochila:    
                        print(Fore.GREEN + "Olá {0}, o segurança encontrou a sua carteirinha ontem no chão! Iremos devolvê-la para você, mas tome cuidado com o porteiro, ele parece estar meio irritado...".format(nome))
                        print(Fore.RESET)
                        mochila.append("carteirinha")
                        nome_cenario_atual = "saguao"
                    else:
                        print(Fore.GREEN + "Desculpe, não temos nada perdido em seu nome, {0}".format(nome))
                        print(Fore.RESET)
                        nome_cenario_atual = "saguao"
                elif nome_cenario_atual == 'catraca' and seguranca_allow != 0:
                    print(Fore.RED + "Segurança: HAA! FINALMENTE ENCONTREI VOCÊ MOLEQUE, AGORA VOU TE DAR UMA LIÇÃO PARA NUNCA MAIS ME FAZER DE TROUXA CATANDO CARTEIRINHA DE GENTE DESCUIDADA!")
                    print(Fore.RESET)
                    while seguranca_allow == 1:
                        luta = True
                        i = 0
                        vida, vida_inimigo = combate(i,vida,item)
                        if vida <= 0 or vida_inimigo <= 0:
                            if vida <= 0:
                                seguranca_allow = 0
                                game_over = True
                            elif vida_inimigo <= 0:
                                seguranca_allow = 0
                            
                        

                        
    if escolha == 'desistir':
        print("Você desistiu de tentar o adiamento, foi embora e pegou DP!")
    else:
        print("Você morreu!")
  
# Programa principal.
if __name__ == "__main__":
    main()

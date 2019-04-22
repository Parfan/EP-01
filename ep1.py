# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Felipe Lacombe,  felipeml4@al.insper.edu.br
# - aluno B: Willian Asanuma, williankal@al.insper.edu.br
# - aluno C: Gabriel Parfan,  gabrielpg1@al.insper.edu.br

import json
from random import randint
from colorama import *
from time import sleep

def carregar_cenarios():
    with open('arquivo_cenarios.py','r') as arquivo_cenarios:
        arquivo1 = arquivo_cenarios.read()
    cenarios = json.loads(arquivo1)
    nome_cenario_atual = "saguao"
    return cenarios, nome_cenario_atual

def combate(nome_inimigo, vida_inimigo, ataque_inimigo, vida, item, game_over, mochila):
    print("Você entrou em combate com {0}!".format(nome_inimigo))
    arma = input(Fore.CYAN + "Para abrir a mochila digite: 'mochila'\n" + Fore.RESET + "Informe a sua arma: ")
    while arma not in mochila:
        if arma == "mochila":
            print(mochila)
            arma = input("Informe a sua arma: ")
        else:
            arma = input("Você não possui este item na sua mochila, digite outro: ")
    arma_usada = item[arma]
    print("Sua vida: {0}".format(vida))
    print(f"Vida do inimigo: {vida_inimigo}")
    while vida > 0 and vida_inimigo > 0:
        dano_inimigo = ataque_inimigo[randint(0,1)]
        vida_inimigo-=arma_usada["dano"]
        print("Você bate no inimigo com {0} e deixa o inimigo com {1} de vida!".format(arma_usada["titulo"],vida_inimigo))
        sleep(1)
        if vida_inimigo <= 0:
            break
        vida-=dano_inimigo
        print("{0} te bate e te deixa com {1} de vida".format(nome_inimigo,vida))
    if vida_inimigo <= 0 and vida > 0:
        print()
        print(Fore.GREEN + "Você venceu a luta!")
        print(Fore.RESET)
    elif vida <= 0:
        game_over = True
    return vida, vida_inimigo, game_over

def inventario():
    mochila = []
    return mochila

def carregar_monstros(i):
    lista_monstros = [1,2,3,4]
    monstros = {
        lista_monstros[0]: {
            "Nome": "Seguranca",
            "Vida": 12,
            "Dano": [3,2]
        },
        lista_monstros[1]: {
            "Nome": "Faxineira ninja",
            "Vida": 8,
            "Dano": [4,1]
        },
        lista_monstros[2]: {
            "Nome": "Professor",
            "Vida": 10,
            "Dano": [2,0]
        },
        lista_monstros[3]: {
            "Nome": "Veterano",
            "Vida": 10,
            "Dano": [2,2]
        }
    }
    nome_inimigo = monstros[lista_monstros[i]]["Nome"]
    vida_inimigo = monstros[lista_monstros[i]]["Vida"]
    ataque_inimigo = monstros[lista_monstros[i]]["Dano"]
    return monstros, nome_inimigo, vida_inimigo, ataque_inimigo

def itens():
    item = {
    "carteirinha": {
        "titulo": "carteirinha",
        "dano": 0
        },
    "atestado": {
        "titulo": "atestado",
        "dano": 5
        },
    "punhos": {
        "titulo": "punhos",
        "dano": 3
        },
    "chave": {
        "titulo": "chave",
        "dano": 0
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

    cenario_anterior = "saguao"
    pocao_de_HP = 0
    game_over = False
    estacionamento_deny = 0
    seguranca_deny = 1
    vida = 20
    i = 0
    escolha = "saguao"
    nome = input("Antes de começar a sua jornada em busca do adiamento do EP...\nDigite seu nome: ")
    
    while len(nome) == 0:
        nome = input("Não seja tímido, diga seu nome: ")
    print()
    
    cenarios, nome_cenario_atual = carregar_cenarios()
    monstros, nome_inimigo, vida_inimigo, ataque_inimigo = carregar_monstros(i)
    item = itens()
    mochila = inventario()
    
    mochila.append("punhos")
    
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
                    print(Fore.RED + "Você não está com sua carteirinha, portanto não pode passar pela catraca!\n" + Fore.RESET)
                    nome_cenario_atual = "saguao"
                elif escolha == "achados e perdidos":
                    if "carteirinha" not in mochila:    
                        print(Fore.CYAN + "Olá {0}, o segurança encontrou a sua carteirinha ontem no chão! Iremos devolvê-la para você, mas tome cuidado com o segurança, ele parece estar meio irritado...\n".format(nome) + Fore.RESET)
                        mochila.append("carteirinha")
                        nome_cenario_atual = "saguao"
                    else:
                        print(Fore.CYAN + "Desculpe, não temos nada perdido em seu nome, {0}\n".format(nome) + Fore.RESET)
                        nome_cenario_atual = "saguao"
                elif nome_cenario_atual == "catraca" and seguranca_deny == 1:
                    print(Fore.RED + "Segurança: HAA! FINALMENTE ENCONTREI VOCÊ MOLEQUE, AGORA VOU TE DAR UMA LIÇÃO PARA NUNCA MAIS ME FAZER DE TROUXA CATANDO CARTEIRINHA DE GENTE DESCUIDADA!\n" + Fore.RESET)
                    i = 0
                    sleep(5)
                    vida, vida_inimigo, game_over = combate(nome_inimigo, vida_inimigo, ataque_inimigo, vida, item, game_over, mochila)
                    if vida > 0:
                        pocao_de_HP += 1
                        print(Fore.CYAN + "+1 pocao de HP\nPara utilizar abra a sua mochila\n" + Fore.RESET)
                        sleep(3)
                    seguranca_deny = 0
                elif nome_cenario_atual == "estacionamento":
                    if cenario_anterior == "saguao":
                        if randint(1,6) < 2:
                            vida-=5
                            print(Fore.CYAN + "Cuidado por onde anda!\nVocê estava atravessando a rua no estacionamento sem olhar para os dois lados e foi atropelado por uma bicicleta!\n")
                            print(Fore.RED + "-5 vida\n" + Fore.RESET + f"Vida = {vida}\n")
                            if vida <= 0:
                                game_over = True
                            else:
                                print(Fore.CYAN + "Por sorte você passa bem e conseguiu voltar ao saguao!\n" + Fore.RESET)
                                nome_cenario_atual = "saguao"
                elif nome_cenario_atual == "tech lab":
                    cenario_anterior = "tech lab"
                    if item["chave"]["titulo"] in mochila:
                        print(Fore.CYAN + "Você entrou no tech lab e encontrou o SMASH testando um teletransportador revolucionário, porém, ainda é uma tecnologia nova e eles não tem nenhuma cobaia para testar...\n")
                        print("Sendo uma pessoa gentil, você se oferece a ser a cobaia que será teletransportada pela primeira vez na história!" + Fore.RESET)
                    else:
                        print(Fore.CYAN + "O tech lab está trancado, parece que para entrar você precisará de uma chave!\n" + Fore.RESET)
                        nome_cenario_atual = "estacionamento"
                elif nome_cenario_atual == "saguao":
                    cenario_anterior = "saguao"
                elif nome_cenario_atual == "roubar carro":
                    cenario_anterior = "roubar carro"
                    if randint(1,5) < 5:
                        print(Fore.WHITE + "\nVocê vê um carro com o vidro aberto e resolve destrancá-lo...\nUsa seus conhecimentos de engenharia para fazer uma ligação direta no carro e, na hora que ia acelerar não percebe que estava na marcha ré!\nPAAAAH!!!\n" + Fore.RESET)
                        game_over = True
                    else:
                        if estacionamento_deny == 0:
                            pocao_de_HP+=3
                            print(Fore.WHITE + "Você vê o carro com o vidro aberto e resolve destrancá-lo...\nPor sorte ninguém te vê e você consegue voltar para o estacionamento com mais 50 dinheiros\n" + Fore.CYAN)                        
                            print("+ pocao de HP\nPara utilizar a sua pocao abra a sua mochila\n" + Fore.RESET)
                            estacionamento_deny += 1
                        else:
                            if dinheiro >= 75:
                                print(Fore.WHITE + "\nVocê tenta roubar o mesmo carro, só que desta vez você é flagrado por um veterano que diz que irá chamar a polícia a menos que você dê 2 pocoes de HP para ele!\n" + Fore.RESET)
                                escolha = input("O que você vai fazer?\n--- OPÇÕES ---\n* 'sim' (Aceitar extosão)\n* 'nao' (Recusar extorsão)\n\nEscolha a sua opção: ")
                                if escolha != "sim":
                                    if escolha != "nao":
                                        print(Fore.WHITE + "O veterano percebe que você está tentando enrolar ele e ele liga pra polícia...\nVocê vai preso com prisão perpétua e apodrece na cadeia!\n" + Fore.RESET)
                                    else:
                                        print(Fore.WHITE + "O veterano liga pra polícia...\nVocê vai preso com prisão perpétua e apodrece na cadeia!\n" + Fore.RESET)
                                        escolha = "saguao"
                                    game_over = True
                                else:
                                    dinheiro -= 75
                                    print(Fore.WHITE + "Você aceita a extorsão do veterano e perde 2 pocoes!\n\n" + Fore.RED)
                                    print("-2 pocoes\n" + Fore.RESET)
                                    nome_cenario_atual = "estacionamento"
                            else:
                                print(Fore.WHITE + "\nVocê tenta roubar o mesmo carro, só que desta vez você é flagrado por um veterano que diz que irá chamar a polícia a menos que você dê 4 pocoes de HP para ele!\n")
                                print("E como você não possui 4 pocoes de HP, ele chama a polícia e você vai preso com prisão perpétua e apodrece na cadeia!\n" + Fore.RESET)
                                escolha = "saguao"
                                game_over = True
                elif nome_cenario_atual == "hall":
                    i = 0
                    monstros, nome_inimigo, vida_inimigo, ataque_inimigo = carregar_monstros(i)
                    vida, vida_inimigo, game_over = combate(nome_inimigo, vida_inimigo, ataque_inimigo, vida, item, game_over, mochila)
                    if vida > 0:
                        dinheiro += 50
                        print(Fore.CYAN + "+1 pocao de HP\nPara utilizar a sua pocao abra a mochila\n" + Fore.RESET)
                        sleep(3)
                #elif:
    if escolha == 'desistir':
        print(Fore.RED + "Você desistiu de tentar o adiamento, foi embora e pegou DP!")
        print(Fore.RESET)
    else:
        print(Fore.RED + "Você morreu!")
        print(Fore.RESET)
  
# Programa principal.
if __name__ == "__main__":
    main()
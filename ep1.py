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
import pygame

def carregar_cenarios():
    with open('arquivo_cenarios.py','r') as arquivo_cenarios:
        arquivo1 = arquivo_cenarios.read()
    cenarios = json.loads(arquivo1)
    nome_cenario_atual = "saguao"
    return cenarios, nome_cenario_atual

def itens():
    with open('arquivo_itens.py','r') as arquivo_itens:
        arquivo2 = arquivo_itens.read()
    item = json.loads(arquivo2)
    return item

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

def maquina_de_snack(dinheiro):
    snacks={
    "snickers": {
        "titulo": "Snickers, mata sua fome",
        "atributos": {
            'preço': 30,
            'vida': 5
        }
    },
    "twix": {
        "titulo": "O portao giratorio",
        "atributos": {
            'preço':40,
            'vida':10
            
        }
    }
    

def main():
        
    pygame.init()
    pygame.display.set_mode((200,100))
    pygame.mixer.music.load("MusicaEP.mp3")
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)
    
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

    dinheiro = 0
    game_over = False
    estacionamento_deny = 0
    seguranca_deny = 1
    vida = 20
    i = 0
    escolha = "saguao"
    nome = input("Antes de começar a sua jornada em busca do adiamento do EP...\nDigite seu nome: ")
    
    while nome.lower() == "andrew":
        nome = input("Desculpe, mas apenas humanos podem jogar este jogo...\nDigite seu nome: ")
    print()
    
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
                elif escolha == 'mochila' or escolha == 'inventario':
                    print(mochila)
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
                        dinheiro += 50
                        print(Fore.CYAN + "+50 dinheiro\n" + Fore.RESET)
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
                            dinheiro += 50
                            print(Fore.WHITE + "Você vê um carro com o vidro aberto e resolve destrancá-lo...\nPor sorte ninguém te vê e você consegue voltar para o estacionamento com mais 50 dinheiros\n" + Fore.CYAN)                        
                            print("+50 dinheiros\n" + Fore.RESET)
                            estacionamento_deny += 1
                        else:
                            if dinheiro >= 75:
                                print(Fore.WHITE + "\nVocê tenta roubar o mesmo carro, só que desta vez você é flagrado por um veterano que diz que irá chamar a polícia a menos que você dê 75 dinheiros para ele!\n" + Fore.RESET)
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
                                    print(Fore.WHITE + "Você aceita a extorsão do veterano e perde 75 dinheiros!\n\n" + Fore.RED)
                                    print("-75 dinheiros\n" + Fore.RESET)
                                    nome_cenario_atual = "estacionamento"
                            else:
                                print(Fore.WHITE + "\nVocê tenta roubar o mesmo carro, só que desta vez você é flagrado por um veterano que diz que irá chamar a polícia a menos que você dê 75 dinheiros para ele!\n")
                                print("E como você não possui 50 dinheiros, ele chama a polícia e você vai preso com prisão perpétua e apodrece na cadeia!\n" + Fore.RESET)
                                escolha = "saguao"
                                game_over = True
                elif nome_cenario_atual == "corredor 1 andar":
                    cenario_anterior = "corredor 1 andar"
                elif nome_cenario_atual == "corredor 2 andar":
                    cenario_anterior = "corredor 2 andar"
                elif nome_cenario_atual == "elevador":
                    usar_elevador = input(Fore.CYAN + "O elevador está em manutenção, mas como não tem ninguém olhando você pode tentar usá-lo...\n" + Fore.RESET + "--- OPÇÕES ---\n* 'sim' (Usar elevador)\n* 'nao' (Melhor não né...)\n\nEscolha a sua opção: ")
                    print()
                    if usar_elevador == "sim":
                        if randint (1,10) < 10:
                            print("Você entra no elevador mesmo sabendo que o mesmo está em manutenção...\nQuando o botão do andar é acionado você escuta um barulho de metal se rompendo...\n")
                            game_over = True
                        else:
                            cenario_anterior = "elevador"
                            nome_cenario_atual = "easter egg"
                    elif usar_elevador == "1337":
                        cenario_anterior = "elevador"
                        nome_cenario_atual = "easter egg"
                    else:
                        nome_cenario_atual = cenario_anterior
                elif nome_cenario_atual == "easter egg":
                   if escolha == "sala secreta":
                       nome_cenario_atual = "sala do teleport"
                       input("Você gostaria de rodar o dado magico?: ")
                       
    if escolha == 'desistir':
        print(Fore.RED + "Você desistiu de tentar o adiamento, foi embora e pegou DP!")
        print(Fore.RESET)
    else:
        print(Fore.RED + "Você morreu!")
        print(Fore.RESET)
    pygame.mixer.music.stop()

# Programa principal.
if __name__ == "__main__":
    main()
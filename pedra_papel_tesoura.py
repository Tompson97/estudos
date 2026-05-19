# .\venv\Scripts\Activate.ps1
import os
import sys


def exibir_logo():
    print("=" * 60)
    # Usamos aspas triplas para strings com múltiplas linhas
    print("""
  _____  ______ _____  _____            
 |  __ \|  ____|  __ \|  __ \     /\\    
 | |__) | |__  | |  | | |__) |   /  \\   
 |  ___/|  __| | |  | |  _  /   / /\ \\  
 | |    | |____| |__| | | \ \  / ____ \\ 
 |_|    |______|_____/|_|  \_\/_/    \\_\\
                                         
  _____             _____  ______ _      
 |  __ \\     /\\    |  __ \|  ____| |     
 | |__) |   /  \\   | |__) | |__  | |     
 |  ___/   / /\ \\  |  ___/|  __| | |     
 | |      / ____ \\ | |    | |____| |____ 
 |_|     /_/    \\_\\|_|    |______|______|
                                         
  _______ ______  _____  ____  _    _ _____            
 |__   __|  ____|/ ____|/ __ \| |  | |  __ \\     /\\    
    | |  | |__  | (___ | |  | | |  | | |__) |   /  \\   
    | |  |  __|  \\___ \| |  | | |  | |  _  /   / /\ \\  
    | |  | |____ ____) | |__| | |__| | | \ \  / ____ \\ 
    |_|  |______|_____/ \\____/ \\____/|_|  \_\/_/    \\_\\
""")
    print("=" * 60)
    print("      BEM-VINDO AO JOGO DE PEDRA, PAPEL E TESOURA!")
    print("=" * 60)

def encerrar_jogo():
    # Usando o prefixo 'r' antes das aspas para garantir que as barras \ 
    # sejam lidas corretamente como desenho, e não como comandos do Python.
    print(r"""
  ___  _     _                 _        
 / _ \| |__ _ __(_)__ _ __  __| | ___   
| (_) | '_ \ '_ \ / _` / _` / _` |/ _ \  
 \___/|_.__/_| |_|_\__, \__,_\__,_\___/  
                   |___/                 
  ___  ___  _ _    _  ___  __ _ __ _ _ _ 
 | _ \/ _ \| '_|  | |/ _ \/ _` / _` | '_|
 |  _/ (_) | |   _| | (_) \__, \__,_|_|  
 |_|  \___/|_|  \__/ \___/|___/|___/|_|  
                                         
""")
    print("=" * 41)
    print("      Até a próxima partida! 👋")
    print("=" * 41)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def gamer_over():
        game_over = input("Deseja jogar novamente? (y/n)").upper().strip()
        if game_over == "Y":
            next
        else:
            clear_terminal()
            encerrar_jogo()
            input("Pressione qualquer tecla para sair.")
            sys.exit()

while(True):
    clear_terminal() # Limpa a saída do terminal antes de executar o jogo
    exibir_logo()


    while(True):
        jogador_1= input("Jogador 1. (pedra/papel/tesoura?) ")
        resposta1 = jogador_1.upper().strip()

        if resposta1 == "PEDRA" or resposta1 == "PAPEL" or resposta1 == "TESOURA":
            break
        else:
            print("Escreva uma opção válida: (pedra, papel ou tesoura) ")


    while(True):
        jogador_2= input("Jogador 2. (pedra/papel/tesoura?) ")
        resposta2 = jogador_2.upper().strip()

        if resposta2 == "PEDRA" or resposta2 == "PAPEL" or resposta2 == "TESOURA":
            break
        else:
            print("Escreva uma opção válida: (pedra, papel ou tesoura)")


    if resposta1 == resposta2:
        print("Empate!")
        gamer_over()
        
    if resposta1 == "PEDRA":
        if resposta2 == "PAPEL":
            print("Vitória do jogador 2!")
            print("Papel vence pedra.")
            gamer_over()         
            
        else:
            print("Vitória do jogador 1!")
            print("Pedra vence tesoura.")
            gamer_over() 
            
    elif resposta1 == "TESOURA":
        if resposta2 == "PAPEL":
            print("Vitória do jogador 1!")
            print("Tesoura vence papel.")
            gamer_over()
            
        else:
            print("Vitória do jogador 2!")
            print("Pedra vence tesoura.")
            gamer_over()
            
    else:
        if resposta2 == "TESOURA":
            print("Vitória do jogador 2!")
            print("Tesoura vence papel.")
            gamer_over()
            
        else:
            print("Vitória do jogador 1!")
            print("Papel vence pedra.")
            gamer_over()
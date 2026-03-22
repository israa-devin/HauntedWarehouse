
dragao_dormindo = r"""
                           |`--,___,--'|       
                           |           |       
                           |           |       
                    ,--,   |           |     
                 ,/'`;`;'\ |           |       
       \\ ' /   /';`;`;`;`;|           |-,_ ,-`~~`-,  ,
       - O - ,/'';';';`;`;`|           |_,-';`;`;`;`\\/|_,
     / \\\\ /`;`;`;';`;`;`;|           |`;`;`;`;`;`;`  o|_,
        \\\\`;';';';';';';';\\         /`;`;`;`;`;`;`;`;  /
       /`\\\\`;`;';';';';';`;`\\,___,/'`;`;`;`;`;`;`;`;`;`\\
         ,/`;`;';`;`;';';';';';';`;`;`;`;__,--~~~-,`;`;_,----,_
      __/;`;`;`; _,;`;`;`;`;`;`;`;`;`;`;``~-~~--,  `~~`        `-,_
  ,--' /;`;`;`;/'/;`;`;';';';';';';';';';';';';`;~~-,__,--~~-,_    `,
,'   ,/;`;`;`;/ (___`;`;`;';';';';';';';';';';';';`;`;`;`;`;`;\`\,   `,
     `-,_`;`;/   ,__\\,;`;`;`;`;`;';';';';';';';';`;`;`;`;`;`;``\\ }    ,
         `-~~         ~~~~~~\\;`;`;`;`;`;`;`;`;`;`;`;`;`;`;`;`;`;`\\    '
   -,                  ____ o| ';';';';';';';';';';';';';';';';';';\\,'
     `-,___,--;~~~;,--------\\|,--,_,-,_,--,_,---,__,--,_,-,_,---,___\\
`-,_    `-'  /`VVV`
    `-,    ,'
"""

dragao_fala = r"""
                 /           /                                               
                /' .,,,,  ./                                                 
               /';'     ,/                                                   
              / /   ,,//,`'`                                                 
             ( ,, '_,  ,,,' ``                                               
             |    /@  ,,, ;" `                                               
            /    .   ,''/' `,``                                              
           /   .     ./, `,, ` ;                                             
        ,./  .   ,-,',` ,,/''\\,'                                             
       |   /; ./,,'`,,'' |   |                                               
       |     /   ','    /    |                                               
        \\___/'   '     |     |                                               
          `,,'  |      /     `\\                                              
               /      |        ~\\                                            
               '       (                                                      
             :                                                               
            ; .         \\--                                                  
          :   \\         ;
"""

dragao_morte = r"""
                                             ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\\
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\\
               -,-..\\  _  \\  `  /  ,  / `._) _,-\\`       \\
                \_,,.) /\\    ` /  / ) (-,, ``    ,        |
               ,` )  | \\_\\       '-`  |  `(               \\
              /  /```(   , --, ,' \\   |`<`    ,            |
             /  /_,--`\\   <\\  V /> ,` )<_/)  | \\      _____)
       ,-, ,`   `   (_,\\ \\    |   /) / __/  /   `----`
      (-, \\           ) \\ ('_.-._)/ /,`    /
      | /  `          `/ \\\\ V   V, /`     /
   ,--\\(        ,     <_/`\\\\     ||      /
  (   ,``-     \\/|         \\-A.A-`|     /
 ,>,_ )_,..(    )\\          -,,_-`  _--`
(_ \\|`   _,/_  /  \\_            ,--`
 \\( `   <.,../`     `-.._   _,-`
""" 

item_pergaminho = r"""
     _______________
()==(              (@==()
     '______________'|
       | ~~~~~~~~~~  |
       | ~~~~~~~~~~  |
     __)_____________|
()==(               (@==()
     '--------------'
"""

finaL_ruim = r"""             +             
            |           
            |         
           / \      
         /_____\  
         |__|__|  
       |;|     |;|  
       \\.    .  /    
        ||:  .  |       
        ||:     |         
        ||:.    |           
        ||:    .|
        ||:   , |         /`\
        ||:     |                                          /`\
        ||: _ . |                             /`\
       _||_| |__|                      ____
  ____~    |_|  |___           __-----~    ~`---,__             ___
-~                  ~---___,--~'                  ~~----_____-~'
`~----,____                       
"""

# Dicionário com charadas e respostas
charadas = {
    "1": ("O que Sobe, sobe, sobe e jamais desce?".upper(), "idade"),
    "2": ("Quanto mais você tira, maior fica?".upper(), "buraco"),
    "3": ("Tem 6 faces, mas em nenhuma delas usa maquiagem. Tem 21 olhos, mas nenhum delez é capaz de ver?".upper(), "dado"),
    "4": ("Não tem carne, escamas, penas ou ossos, mas tem dedos próprios, o que é?".upper(),"luva"),
    "5": ("O que é que atravessa o rio mas nunca se molha?".upper(), "ponte"),
    "6": ("Ele nunca passa, mas sempre está na frente. Quem é?".upper(),"futuro")
}

# ======= MENSAGEM DE INÍCIO =======
print("Depois de horas na masmorra, finalmente você chega à sala principal...\n")
print(dragao_dormindo)

resposta_inicio = input("Pretende continuar sua busca? (s/n) ").strip().lower()

if resposta_inicio != "s":
    print("\nParece que por hoje já vivemos aventuras demais.\nVocê volta pra casa e pede um iFood.\n" + finaL_ruim)
    input("\nPressione Enter para sair...")
    exit()

# ======= LOOP PRINCIPAL =======
vida = 3  # número inicial de vidas
fim_jogo = False  # controla quando o jogo termina

print("\nVocê move furtivamente pela grande sala até esbarrar em um busto mal posicionado...\n" + dragao_fala +
      "\n'ORA, ORA, SE NÃO É MAIS UM AVENTUREIRO EM BUSCA DE MEUS TESOUROS'"
      "\n'RESPONDA CORRETAMENTE UMA DAS MINHAS CHARADAS E DEIXAREI ESCOLHER QUALQUER ITEM DA MINHA COLEÇÃO'"
      "\n'CUIDADO! VOCÊ SÓ TEM TRÊS CHANCES HAHAHAHA!'")

while not fim_jogo:
    print("\nEscolha uma charada ou digite 'fugir' para tentar escapar:\n")
    for key in charadas.keys():
        print(f"Charada número {key}")
    print("Fugir")

    escolha = input("\nDigite o número da charada: ").strip().lower()

    if escolha == "fugir":
        print("\n'NINGUÉM FOGE DE AERIONAR'" + dragao_morte + "\nVocê morreu...\n")
        fim_jogo = True
        break

    elif escolha in charadas:
        pergunta, resposta_certa = charadas[escolha]

        while True:  # loop da charada
            resposta = input(f"{pergunta} ").strip().lower().split()

            if resposta_certa in resposta:
                print(dragao_fala +
                      "\nACERTOU!! ESCOLHA SEU ITEM LOGO ANTES QUE MUDE DE IDEIA.\n".upper()
                      + item_pergaminho
                      + "\nVocê pega o Pergaminho da Sabedoria e some dali."
                      + "\nAgora com o Pergaminho da Sabedoria você vai conseguir sonegar qualquer imposto."
                      + "\nQuem diria que torres mágicas eram tão caras?"
                      + finaL_ruim)
                fim_jogo = True
                break  # sai do loop da charada
            else:
                vida -= 1
                if vida <= 0:
                    print("\n'HAHAHAHA! PATÉTICO!!'" + dragao_morte + "\nVocê morreu...")
                    fim_jogo = True
                    break  # termina o jogo
                print(f"\n'ERRADO!! VOCÊ TEM MAIS {vida} CHANCES'".upper())
                mudar = input("\nQuer escolher outra charada? (s/n) ").strip().lower()
                if mudar == "s":
                    break  # volta ao menu para escolher outra charada
                # Se mudar != "s", continua perguntando a mesma charada
    else:
        print("\nOpção inválida, tente novamente.")

# ======= FINALIZAÇÃO DO JOGO =======
input("\nPressione Enter para sair...")
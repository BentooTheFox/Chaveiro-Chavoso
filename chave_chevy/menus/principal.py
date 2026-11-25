from os import name, system
from time import sleep
from tela import Tela
from logging import warning, info, error, critical

clear = lambda: system("cls" if name == "nt" else "clear")

OPCOES = [
    ("Bentoo", "Goat"),
    ("Criar novo perfil", Tela.PRINCIPAL),
    ("Editar perfil existente", Tela.DE_EDICAO),
    ("Visualizar perfis", Tela.DE_VISUALIZAR),
    ("Excluir perfil", Tela.DE_EXCLUIR),
    ()
]

info("Menu principal: Telas mapeadas")

MENU = r"""
                                                            
 ,-----.,--.                             ,--.               
'  .--./|  ,---.  ,--,--.,--.  ,--.,---. `--',--.--. ,---.  
|  |    |  .-.  |' ,-.  | \  `'  /| .-. :,--.|  .--'| .-. | 
'  '--'\|  | |  |\ '-'  |  \    / \   --.|  ||  |   ' '-' ' 
 `-----'`--' `--' `--`--'   `--'   `----'`--'`--'    `---'  

 ,-----.,--.                 
'  .--./|  ,---.  ,--,--.,--.  ,--.,---.  ,---.  ,---.      
|  |    |  .-.  |' ,-.  | \  `'  /| .-. |(  .-' | .-. |     
'  '--'\|  | |  |\ '-'  |  \    / ' '-' '.-'  `)' '-' '     
 `-----'`--' `--' `--`--'   `--'   `---' `----'  `---'      
Bentoo 🐾

Bem-Vind@ ao CHAVEIRO CHAVOSO!

Com ele você pode criar nicks, senhas e logins inteiros!

Escolha uma opção para começar!

{}

99 - Sair
____________________________________
O que vai ser, campeã(o)?"""


def _formatar_menu_(menu=MENU):
    decoracao = "[{}] - {}\n"
    __formatacao__ = []

    for num, opt in enumerate(OPCOES):
        try:
            linha = decoracao.format(num, opt[0])

        except IndexError:
            warning(
                "Ocorreu um erro ao adicionar um item na formatação."
                    + f"Segue o item:\n\t{OPCOES[num]}"
                    + "\nPortanto este será ignorado." 
                )
            linha = decoracao.format(num, "BLOQUEADO - Erro ao processar este item")

        __formatacao__.append(linha)
    
    return menu.format( "".join(__formatacao__) )



def iniciar_loop(menu=_formatar_menu_()):
    while True:
        print(menu)
        usr = input(">> ")

        if usr.isnumeric():
            usr = int(usr)

            if 0 < usr < len(OPCOES):
                print("O usuário optou por", OPCOES[usr])
                try:
                    proximo_estado = OPCOES[usr][1]
                    info(f"Seleção realizada com sucesso, indo para {proximo_estado}")
                    return proximo_estado


                except IndexError as ie:
                    warning(f"Não foi possível realizar a mudança de estado\n\tRazão:\n\t\t{ie};\n\tNota: Opção inválida ou mapeamento quebrado.")
                    critical("Mapeamento possivelmente quebrado.")
                    print("Houve um erro, mas não se assuste! Veja o arquivo LOG.txt para ver o que aconteceu.")
                    input("< Pressione Enter para reiniciar >")
                    clear()

                except Exception as e:
                    error(f"Não foi possível avançar para o próximo estado.\n\tRazão:\n\t\t{e}")
                    raise e

            elif usr == 99:
                return Tela.SAIR

        print("Resposta inválida, bro.")
        sleep(1.9)
        clear()


if __name__ == "__main__":
    iniciar_loop()

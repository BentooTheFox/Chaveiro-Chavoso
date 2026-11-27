from time import sleep

try:
    from database import gerenciamento_de_dados
    from ferramentas import artista_artoso, imprimir_tabela
    from seguridad import log_logoso
    from objetos.tela import Tela
except:
    from .database import gerenciamento_de_dados
    from .ferramentas import artista_artoso, imprimir_tabela
    from .seguridad import log_logoso
    from objetos.tela import Tela

PETER = artista_artoso.construir_coloracao_rgb(r=233, g=138, b=158) + r"""
⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠤⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢴⠋⠙⠳⣤⡀⣠⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠓⠤⡀⣠⡴⠟⠛⣷⠀⠀
⠀⠀⠈⠳⢤⣀⢈⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢏⣀⣠⡴⠋⠀⠀
⢀⣠⣤⣄⣄⣉⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⣡⣤⡴⣦⣀
⢹⣅⡀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠁⠀⢀⣠⠏
⠀⠈⠙⠉⢋⣉⣇⠀⠀⣾⣷⠄⠀⠀⠀⠀⠀⠀⠀⢴⣿⡆⠀⢀⣿⡙⠋⠋⠀⠀
⠀⠀⢤⠶⠋⠉⢈⣦⡀⠈⠉⠀⠀⠀⠉⠉⠉⠀⠀⠀⠉⠀⣠⣎⠈⠉⠛⢷⡀⠀
⠀⠀⠻⣤⣤⠶⠋⠀⠈⠑⠠⠄⣀⣀⣀⣀⣀⣀⡀⠤⠐⠉⠀⠈⠻⠶⠖⠶⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠤⡀⠀⡠⠤⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠉⠁⠀⠉⠉⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢀⠤⡀⠀⡠⢄⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠢⣀⣀⣀⣈⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⡇⠀⣎⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⡇⣸⠜
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + artista_artoso.RESET

MENU = f"""
Este é o menu de {artista_artoso.filtro_arco_iris("EDIÇÃO")}.

Funciona assim:
- Escolha um nick/perfil existente
- O programa guiará você para que edite respectivamente: nick/perfil, senha.

🦊< Você consegue!
"""
# [0] - Pesquisar um nick # TODO -> Sisteminha de pesquisa para encontrar nicks mais rápido


@log_logoso.run_function
def escolher_perfil():
    logins = gerenciamento_de_dados.consultar_logins()
    imprimir_tabela.clear()
    while True:
        try:
            print(
                artista_artoso.aviso(
                    "Quando encontrar o ID do login desejado, pressione Ctrl + C para poder acessar."
                )
            )
            sleep(2)
            imprimir_tabela.imprimir_tabela(logins, itens_por_pagina=30)
            raise KeyboardInterrupt

        except KeyboardInterrupt:
            print()
            usr = input(
                "Digite o id do login a ser editado ou '/lista' para rever a lista do começo - para cancelar digite '/cancelar' >> "
            )
            if usr.isnumeric() and int(usr) >= 0:
                login_consultado = gerenciamento_de_dados.consultar_login_por(
                    credencial=int(usr), metodo=gerenciamento_de_dados.ID
                )
                return login_consultado

            elif usr.lower().strip() == "/back":
                continue
            
            elif usr.lower().strip() == "/cancelar":
                return
            





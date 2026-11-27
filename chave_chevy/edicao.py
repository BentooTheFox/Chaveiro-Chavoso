# TODO -> Sisteminha de pesquisa para encontrar nicks mais rápido

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
    from .objetos.tela import Tela


#region Banner & Deco

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

🦊 < Você consegue!

[0] - Iniciar edição
[1] - Voltar

(Dê enter para começar ou 1 ou '/back' para voltar) >>> """

#endregion


#region Func

@log_logoso.run_function
def escolher_perfil():
    print()
    usr = input(
        "Digite o id do login a ser editado ou '/lista' para rever a lista do começo - para cancelar digite '/cancelar' >> "
    )
    if usr.isnumeric() and int(usr) >= 0:
        login_consultado = gerenciamento_de_dados.consultar_login_por(
            credencial=int(usr), metodo=gerenciamento_de_dados.ID
        )
        return login_consultado

    return usr.lower().strip()


@log_logoso.run_function
def iniciar_edicao_de_perfil(perfil: tuple[str, str]) -> tuple:
    print("Maravilha, parceir@! Vamos editar esse treco e deixar com a sua cara!")
    nome = perfil[0]
    senha = perfil[1]

    # Nome
    print("Vamos começar pelo NOME/NICK.")
    print("Atual:", nome)
    novo_nome = input(
        "Que nome deseja pôr? (Deixe em branco para pular e manter como está) >> "
    )
    if novo_nome and novo_nome != nome:
        nome = novo_nome

    # Senha
    print("Perfeito. Quase acabando, companheir@! Vamos ver sua senha.")
    print("Atual:", senha)
    nova_senha = input(
        "Como deve ser a senha nova? (Deixe em branco para pular e manter como está) >> "
    )
    if nova_senha and nova_senha != senha:
        senha = nova_senha

    return (novo_nome, nova_senha)


@log_logoso.run_function
def iniciar_loop():
    # Intro
    print(PETER)
    sleep(.75)
    if input(MENU) in ["1", "voltar", "/back", "/voltar"]:
        return Tela.PRINCIPAL
    print(artista_artoso.sucesso("Muito bem!"))

    # Preparação de dados:
    logins = gerenciamento_de_dados.consultar_logins()
    imprimir_tabela.clear()

    # Loop principal
    while True:
        print(
            artista_artoso.aviso(
                "Quando encontrar o ID do login desejado,"
                +
                " pressione Ctrl + C para poder acessar."
            )
        )
        sleep(2)

        try:
            imprimir_tabela.imprimir_tabela(logins, itens_por_pagina=30)
            raise KeyboardInterrupt

        except KeyboardInterrupt:
            perfil_escolhido = escolher_perfil()

            match perfil_escolhido:
                case "/lista":
                    continue

                case "/cancelar":
                    return Tela.PRINCIPAL

                case _:
                    perfil_editado = iniciar_edicao_de_perfil(perfil_escolhido)
                    gerenciamento_de_dados.inserir_login(perfil_editado)
                    if input("Deseja editar ou perfil? [s/N] >> ") in ["", "n", "no", "nope", "nao", "não"]:
                        gerenciamento_de_dados.salvar()
                        return Tela.PRINCIPAL

                    else:
                        gerenciamento_de_dados.salvar()
                        continue

#endregion
from os import system, name

clear = lambda: system("cls" if name == "nt" else "clear")


def imprimir_tabela(lista_de_dicionarios_de_logins: list[dict], itens_por_pagina=25):
    """
    Exibe uma tabela formatada no console com informações de logins.

    A função recebe uma lista de dicionários, onde cada dicionário representa
    um login com as chaves "id", "nome" e "senha". A tabela é exibida com
    colunas alinhadas, ajustando dinamicamente o tamanho das colunas com base
    no conteúdo mais longo.

    Parâmetros:
    -----------
    lista_de_dicionarios_de_logins : list[dict]
        Uma lista de dicionários contendo os dados de login. Cada dicionário
        deve ter as chaves:
        - "id" (int): Identificador único do login.
        - "nome" (str): Nome de usuário.
        - "senha" (str): Senha do usuário.

    Retorno:
    --------
    None
        A função não retorna nada, apenas exibe a tabela formatada no console.

    Exemplo de uso:
    ---------------
    lista = [
        {"id": 1, "nome": "usuario1", "senha": "senha1"},
        {"id": 2, "nome": "usuario2", "senha": "senha2"}
    ]
    imprimir_tabela(lista)
    """

    LINHA = "[ID] {} -- [USR] -- {}  -- [SNH] -- {}"
    TAMANHO_DO_DICIONARIO = len(lista_de_dicionarios_de_logins)
    ITENS_POR_PAGINA = itens_por_pagina

    maior_numero_de_idd = max(
        len(str(dicionario["id"])) for dicionario in lista_de_dicionarios_de_logins
    )
    tamanho_da_coluna_central = max(
        len(dicionario["nome"]) for dicionario in lista_de_dicionarios_de_logins
    )

    def __imprimir__(bloco):
        for login in bloco:
            nome = login["nome"]
            idd = str(login["id"])

            diferenca = tamanho_da_coluna_central - len(nome)

            if not diferenca % 2 == 0:
                diferenca += 1

            espaço_restante = diferenca // 2 * " "

            nome = espaço_restante + nome + espaço_restante
            idd = idd + " " * (maior_numero_de_idd - len(idd))

            if tamanho_da_coluna_central - len(nome) == -1:
                nome = nome[1:]

            print(
                LINHA.format(
                    idd,
                    nome,
                    login["senha"],
                )
            )

    if TAMANHO_DO_DICIONARIO > ITENS_POR_PAGINA:
        for pagina in range(0, TAMANHO_DO_DICIONARIO, ITENS_POR_PAGINA):
            __imprimir__(
                lista_de_dicionarios_de_logins[pagina : pagina + ITENS_POR_PAGINA]
            )
            input(
                f"""
--- Próxima página [{pagina+ITENS_POR_PAGINA}/{TAMANHO_DO_DICIONARIO}] >> """
            ) # TODO: (para voltar, digite 99)
            
            if pagina+ITENS_POR_PAGINA < TAMANHO_DO_DICIONARIO: # Para pular o último clear
                clear()
    else:
        __imprimir__(lista_de_dicionarios_de_logins)

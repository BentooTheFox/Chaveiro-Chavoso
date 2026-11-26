try:
    from .objetos import tela
    from .seguridad import log_logoso
    from .ferramentas import geramento_chavoso
    from .database import gerenciamento_de_dados
    from .ferramentas.enfeites import artista_artoso

except:
    from objetos import tela
    from seguridad import log_logoso
    from ferramentas import geramento_chavoso
    from database import gerenciamento_de_dados
    from ferramentas.enfeites import artista_artoso

import random

loop_padrao_de_geracao = geramento_chavoso.loop_padrao_de_geracao
gerar_nickname = geramento_chavoso.gerar_nickname
gerar_senha = geramento_chavoso.gerar_senha

ASCII_RAPOSA = r"""
       :===:                :===:
      :*=--+=:            :=+--=*:
      -# -+=-+-          -+-=+- #-
      =*  :+=:=+========+=:=+:  *=
      += : :@: :#-::::-#: :@: : ++
      +=   :*:            :*:   =+
      +=                        =+
      -*                        *-
      :%-                      -%:
      +=    :==:        :==:    =+
     :%:    :*#+:      :+#*:    :%:
     :#:                        :#:
      +=       -:      :-       =+
      :#---:  :%:::  :::%:  :---#:
       :---=+:=* -+==+- *=:+=---:
            --:*=::*#::=*:--
                -+======:
                :======:
                   :::
"""

welCUM = (
    "Olá! Bem-vindo ao menu de "
    + artista_artoso.filtro_arco_iris("CRIAÇÃO", estilo=artista_artoso.Estilos.NEGRITO)
    + "!"
)


PROMPTS_PARA_INPUT_DE_CREDENCIAL = [
    "Qual {credencial} desse perfil?",
    "Me fala por favor que {credencial} você quer associar a esse perfil.",
]

MENSAGENS_COMEMORATIVAS = [
    ""
]

def iniciar_loop():
    print(welCUM)
    print("Vamos lá, parceir@!")

    nick = loop_padrao_de_geracao(
        mensagem_de_confirmacao = random.choice( PROMPTS_PARA_INPUT_DE_CREDENCIAL ) %"USUÁRIO/NICK/EMAIL",
        gatilho=gerar_nickname,
    )

    print(artista_artoso.filtro_arco_iris(str(nick) + "! Que maravilha!!"))

    senha = loop_padrao_de_geracao()


iniciar_loop()

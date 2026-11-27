import random
import time
from os import name, system

try:
    from .objetos import tela
    from .ferramentas import geramento_chavoso
    from .database import gerenciamento_de_dados
    from .ferramentas import artista_artoso
    from .seguridad import log_logoso

except:
    from objetos import tela
    from ferramentas import geramento_chavoso
    from database import gerenciamento_de_dados
    from ferramentas import artista_artoso
    from seguridad import log_logoso

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
                :======:   Bentoo
                   :::
"""








#region Strings & Deco

welCUM = (
    "Olá! Bem-vindo ao menu de "
    + artista_artoso.filtro_arco_iris("CRIAÇÃO", estilo=artista_artoso.Estilos.NEGRITO)
    + """!    
Nota: caso você utilize o EXATO mesmo nome de algum outro perfil existente, a senha será ATUALIZADA.
Para cancelar digite '/99' a qualquer momento.
Mesmo que escreva /99, a confirmação da etapa ainda será efetuada, é normal."""
)


PROMPTS_PARA_INPUT_DE_CREDENCIAL = [
    "Qual {} desse perfil?",
    "Me fale, por favorzinho, que {} você quer associar a esse perfil.",
    "Ok, que {} você deseja pôr?",
    "Agora, escolhe só {} legal, hein!",
]

#endregion



# Guigaz!




#region Func

clear = lambda: system("cls" if name == "nt" else "clear")

@log_logoso.run_function
def cancelar_operacao():
    print("Deseja mesmo cancelar a operação? Você irá retornar à tela PRINCIPAL")

    for i in range(3, 0, -1):
        print(artista_artoso.aviso(f"*Liberando confirmação em {i}... "), end="\r")
        time.sleep(1)

    print("\n", end="\r")

    usr = input("Cancelar e voltar ao início? [S/n] ").lower().strip()
    if usr in ["sim", "s", "y", "yes", ""]:
        return True
    return False

@log_logoso.run_function
def criar_em_massa(quantidade = 25):
    for _ in range(quantidade):
        gerenciamento_de_dados.inserir_login(
            ( gerar_nickname(), gerar_senha(True),)
            )
    gerenciamento_de_dados.salvar()

@log_logoso.run_function
def iniciar_loop():
    clear()
    print(
        artista_artoso.filtro_arco_iris(
            ASCII_RAPOSA, estilo=artista_artoso.Estilos.NORMAL
        )
    )
    time.sleep(1)
    print(welCUM, end="\n\n")

    while True:
        nik_prompt = random.choice(PROMPTS_PARA_INPUT_DE_CREDENCIAL).format(
            "USUÁRIO/NICK/EMAIL"
        )
        pwd_prompt = random.choice(PROMPTS_PARA_INPUT_DE_CREDENCIAL).format("SENHA")
        tip_prompt = " (Deixe em branco para gerar) >> "

        # Nick
        nick = loop_padrao_de_geracao(nik_prompt + tip_prompt, gerar_nickname)
        if nick == "/99" and cancelar_operacao():
            return tela.Tela.PRINCIPAL

        print(artista_artoso.filtro_arco_iris(str(nick)[:35] + "! Que maravilha!!"))

        # Senha
        senha = loop_padrao_de_geracao(pwd_prompt + tip_prompt, gerar_senha)
        if senha == "/99" and cancelar_operacao():
            return tela.Tela.PRINCIPAL

        print(artista_artoso.filtro_arco_iris(f"{senha}? É isso aí!!"))

        # Sequencia final
        print(artista_artoso.sucesso("Novo login gerado com sucesso!"))
        time.sleep(0.25)

        print(
            f"Aí, gente boa, as credenciais ficaram assim:\nLogin:\n-- Usuário: {nick}\n-- Senha: {senha}"
        )
        time.sleep(0.25)

        for i in range(5, 0, -1):
            print(
                artista_artoso.aviso(f"*Liberando confirmação em {i}... "),
                end="\r",
            )
            time.sleep(1)
        print("", end="\r")

        if not input("Está correto? [S/n]").lower().strip() in ["", "s", "y"]:
            msg = artista_artoso.aviso(
                f"Ok, mas antes de voltar, COPIE o que você quer salvar!!\nUsuário: {nick}\nSenha: {senha}\n"
            )
            print(msg)
            input("< Pressione ENTER para reiniciar a criação >")
            clear()
            print(
                artista_artoso.filtro_arco_iris(ASCII_RAPOSA)
                + artista_artoso.aviso(
                    "\nLembrando: '/99' cancela a operação e te leva de volta à tela principal.\n"
                )
            )
            continue

        break

    gerenciamento_de_dados.inserir_login((nick, senha))
    gerenciamento_de_dados.salvar()

    artista_artoso.reset()

    return tela.Tela.PRINCIPAL


#endregion
from string import digits
from string import punctuation
from string import ascii_letters


def loop_padrao_de_geracao(
    mensagem_inicial="Qual nome quer dar para este login? (Deixe em branco para nick aleatório) >> ",
    gatilho=print,
    mensagem_de_confirmacao='"%s" está ok? [S/n] >> ',
):

    while True:

        # 'nome' aqui não significa nada, apenas
        # se chama assim para exemplificar um uso real
        # e para facilitar a visualização do significado
        # de cada coisa.

        nome = input(mensagem_inicial)
        nome = gatilho() if not nome else nome

        match input(
            mensagem_de_confirmacao
            if not "%s" in mensagem_de_confirmacao
            else mensagem_de_confirmacao % nome
        ).lower().strip():

            case None | "":
                print(nome, "confirmado então!")
                return nome


# Gerar login completo com: identificador, nickname/login e senha
def gerar_nickname():
    return 'Bentoo the GOAT'

def gerar_senha():
    # logica para criar uma senha/pin
    return '1234abcd'


from string import digits
from string import punctuation
from string import ascii_letters
from string import ascii_lowercase
from random import choice
from random import randint
from random import shuffle

try:
    from .nick_list import words
except:
    from nick_list import words


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
    nick = ""

    for i in range(2):
        nick = nick + str(choice(words)).capitalize()

    for i in range(2):
        nick = nick + str(randint(0, 9))

    return nick


def gerar_senha(auto=False):
    usr = None if not auto else "cadeia"
    tamanho = "" if not auto else 12

    if not auto:

        while usr not in ("pin", "cadeia", ""):
            usr = (
                input(
                    "Perfeito! Agora, deseja um PIN (apenas números) ou cadeia de caracteres (senha forte).\nEscreva 'pin' para PIN ou deixe em branco para gerar uma cadeia >> "
                )
                .lower()
                .strip()
            )

        while not (tamanho.isnumeric() and 100 >= int(tamanho) >= 6):
            tamanho = input(
                "Você quer que a senha tenha quantos dígitos? (min.: 6, recomendado: 12, max: 100) >> "
            )
            if not tamanho:
                tamanho = "12"

        tamanho = int(tamanho)

    if usr == "pin":
        return "".join([str(randint(0, 9)) for _ in range(tamanho)])

    else:
        senha = [choice(digits + ascii_letters + punctuation) for _ in range(tamanho)]

        shuffle(senha)

        senha = "".join(senha)

        return senha


if __name__ == '__main__':
    print("Auto:",gerar_senha(True))
    print("SEM Auto:",gerar_senha(False))
    print(gerar_nickname())
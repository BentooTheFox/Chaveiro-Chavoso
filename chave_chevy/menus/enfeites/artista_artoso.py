import os
import ctypes
import logging
from random import randint
from itertools import cycle

RESET = "\033[0m"

if os.name == "nt":
    kernel32 = ctypes.windll.kernel32
    # 7 = ENABLE_PROCESSED_OUTPUT (1) | ENABLE_WRAP_AT_EOL_OUTPUT (2) | ENABLE_VIRTUAL_TERMINAL_PROCESSING (4)
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


class Estilos:
    NORMAL = 0
    NEGRITO = 1
    ITALICO = 3
    SUBLINHAR = 4


class Cores:
    PRETO = 30
    VERMELHO = 31
    VERDE = 32
    AMARELO = 33
    AZUL = 34
    MAGENTA = 35
    CIANO = 36
    BRANCO = 37
    NORMAL = BRANCO


def construir_coloracao(
    estilo=Estilos.NORMAL,
    cor_do_texto=Cores.NORMAL,
    fundo=Cores.PRETO
):
    try:
        sum([estilo, fundo, estilo])
        return f"\033[{estilo};{cor_do_texto};{fundo+10}m"

    except TypeError as e:
        logging.warning(f"""Construção de coloração impossível.
\t-- Razão: {e}.
\t-- Recebidos:
\t\t{estilo=}
\t\t{cor_do_texto=}
\t\t{fundo=}""")

        return ""
    


def construir_coloracao_rgb(r=None, g=None, b=None, colorir_fundo=False):
    r = r or randint(0, 255)
    g = g or randint(0, 255)
    b = b or randint(0, 255)

    if colorir_fundo:
        return f"\033[48;2;{r};{g};{b}m"

    return f"\033[38;2;{r};{g};{b}m"


def filtro_arco_iris(texto, estilo=Estilos.NEGRITO, auto_reset=True):
    cores = cycle(
        [
            Cores.VERMELHO,
            Cores.AMARELO,
            Cores.VERDE,
            Cores.CIANO,
            Cores.AZUL,
            Cores.MAGENTA,
        ]
    )

    atribuicoes = zip(cores, texto)

    stringo = "".join(
        [construir_coloracao(estilo, cor) + char for cor, char in atribuicoes]
    )

    if auto_reset:
        stringo = stringo + RESET
    return stringo


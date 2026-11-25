from chave_chevy import menus
from chave_chevy.menus.tela import Tela
from chave_chevy.tools import geramento_chavoso
from chave_chevy.database import gerenciamento_de_dados

# Mapeamento
while ESTADO != Tela.SAIR:
    funcao = MAQUINA[ESTADO]
    funcao()

from os import name, system
from time import sleep
from chave_chevy.seguridad.log_logoso import _setup_logger
from chave_chevy import principal
from chave_chevy import criacao
# TODO from chave_chevy import edicao
# TODO from chave_chevy import exclusao
from chave_chevy import visualizacao
from chave_chevy.objetos.tela import Tela

_setup_logger()

clear = lambda: system("cls" if name=='nt' else "clear")

mapa = {
    Tela.DE_CRIACAO: criacao.iniciar_loop,
    Tela.PRINCIPAL: principal.iniciar_loop,
    # TODO Tela.DE_EDICAO: edicao.iniciar_loop,
    # TODO Tela.DE_EXCLUIR: exclusao.iniciar_loop,
    Tela.DE_VISUALIZAR: visualizacao.iniciar_loop,
    Tela.SAIR: 99
}

ESTADO = Tela.PRINCIPAL

# Mapeamento
while ESTADO != Tela.SAIR:
    funcao = mapa[ESTADO]
    novo_estado = funcao()

    if mapa.get(novo_estado):
        ESTADO = novo_estado

    else:
        print("Opção inválida ou quebrada.")
        sleep(1)
        clear()
        ESTADO = Tela.PRINCIPAL

print("Bye!")
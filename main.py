# TODO from chave_chevy import exclusao

from os import name, system
from time import sleep
from chave_chevy.seguridad.log_logoso import _setup_logger
from chave_chevy import principal
from chave_chevy import criacao
from chave_chevy import edicao
from chave_chevy import visualizacao
from chave_chevy.objetos.tela import Tela

_setup_logger()


mapa = {
    Tela.PRINCIPAL: principal.iniciar_loop,
    Tela.DE_CRIACAO: criacao.iniciar_loop,
    Tela.DE_EDICAO: edicao.iniciar_loop,
    Tela.DE_VISUALIZAR: visualizacao.iniciar_loop,
    Tela.SAIR: 99
#TODO Tela.DE_EXCLUIR: exclusao.iniciar_loop,
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
        system("cls" if name=='nt' else "clear")
        ESTADO = Tela.PRINCIPAL

print("Bye!")
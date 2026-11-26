from logging import info, error, warning
from pathlib import Path


def consertar_recursivamente(caminho: Path):
    try:
        print("Tentando criar", caminho.name)
        caminho.mkdir()

        info("Pasta parente criada:", caminho.name)

        return caminho

    except FileNotFoundError:
        aviso = f"Ops! Erro ao alcançar: {caminho.name}, pegando parente..."
        warning(aviso)
        print(aviso)
        consertar_recursivamente(caminho.parent)
    
    except Exception as e:
        error(f"Não foi possível criar o caminho: {caminho.absolute()}. Razão: {e}")


def tocar(caminho: Path):
    '''Tenta Path.touch() no caminho fornecido.
    
    Caso falhe (FileNotFoundError), o caminho é construído
    recursivamente até o destino desejado e o arquivo é tocado.'''

    try:
        caminho.touch()
        info(caminho.name, "tocado com sucesso!")

    except FileNotFoundError:
        warning("Iniciando sequencia de vapo")

        while not consertar_recursivamente(caminho.parent):
            continue

        caminho.touch()
        info("Pastas recursivas criadas com sucesso. Arquivo tocado também.")

    except Exception as e:
        error(f"Não foi possível criar o caminho até {caminho.absolute()}. Um erro desconhecido ocorreu: {e}")
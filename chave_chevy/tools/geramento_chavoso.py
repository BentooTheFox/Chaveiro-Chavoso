if __name__ == '__main__':
    from loop_padrao_de_geracao import loop_padrao_de_geracao
else:
    from .loop_padrao_de_geracao import loop_padrao_de_geracao

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
especiais_basicos = '!@#$'
especiais_completao = '()[]}{_~;:,.><' + especiais_basicos
numericos = '1234567890'

cadeia_de_caracteres = alfabeto + alfabeto.upper()
cadeia_de_caracteres += especiais_completao + numericos

# Gerar login completo com: identificador, nickname/login e senha
def gerar_nickname():
    return 'Bentoo the GOAT'

def gerar_senha():
    # logica para criar uma senha/pin
    return '1234abcd'

def criar_login():
    nome = loop_padrao_de_geracao(
        gatilho = gerar_nickname
    )
    senha = loop_padrao_de_geracao(
        "Escreva a senha que deseja atribuir ao perfil. Deixe em branco para gerar uma senha nova >> ",
        gerar_senha
    )
    return (nome, senha)
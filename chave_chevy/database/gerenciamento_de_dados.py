import pathlib
import logging
import sqlite3

try:
    from . import sql_queries
    from . import verificador_de_integridade_de_caminho as vic
except:
    import sql_queries
    import verificador_de_integridade_de_caminho as vic


PASTA_CHAVE_CHEVY = pathlib.Path(__file__).parents[1]
CAMINHO_DO_BANCO = PASTA_CHAVE_CHEVY / "data" / "Clavium.db"

vic.tocar(CAMINHO_DO_BANCO)

try:
    banco = sqlite3.connect(CAMINHO_DO_BANCO)

except sqlite3.OperationalError as e:
    logging.error(f"Não foi possível se conectar ao banco de dados.\nRazão: {e}")
    raise e

cursor = banco.cursor()

# ------
banco.execute(sql_queries.CRIAR_TABELA)
logging.info("Banco conectado e ativo.")


def salvar():
    try:
        banco.commit()
        print("Banco atualizado!")
        logging.info("Alterações enviadas ao banco de dados")

    except Exception as e:
        logging.error(f"Erro ao enviar alterações ao banco de dados.\nRazão: {e}")


def inserir_login(tupla_de_credenciais: tuple):
    try:
        banco.execute(sql_queries.INSERIR_OU_ATUALIZAR_PERFIL, tupla_de_credenciais)
        logging.info("Credenciais atualizadas/adicionadas com sucesso.")
        print("Login novo!")

    except Exception as e:
        logging.error(
            f"Um erro ocorreu ao tentar inserir o login {tupla_de_credenciais} no banco de dados. Razão: {e}"
        )
        raise e


def consultar_logins():
    cursor.execute(sql_queries.SELECIONAR_TUDO)
    return [
        {"id": idd, "nome": nome, "senha": senha}
        for idd, nome, senha in cursor.fetchall()
    ]


def excluir_perfil(idd=None):
    try:
        banco.execute(sql_queries.EXCLUIR_LINHA_PELO_ID, idd)
        logging.info("Exclusão realizada.")

    except Exception as e:
        msg = f"Não foi possível excluir o perfil de id {idd} do banco de dados. Razão: {e}"
        # print(msg)
        logging.error(msg)

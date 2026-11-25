SELECIONAR_TUDO = "SELECT * FROM chavosaria"

EXCLUIR_LINHA_PELO_ID = "DELETE FROM chavosaria WHERE id = ?"

INSERIR_OU_ATUALIZAR_PERFIL = '''
INSERT INTO chavosaria (perfil, senha) VALUES (?, ?)
ON CONFLICT(perfil) DO UPDATE SET
    senha = excluded.senha'''

CRIAR_TABELA = '''
CREATE TABLE IF NOT EXISTS chavosaria(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    perfil TEXT UNIQUE NOT NULL,
    senha TEXT DEFAULT "Sem senha"
)'''
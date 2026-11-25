from enum import Enum, auto

# 1. Cada tela do seu CLI é um Estado
class Tela(Enum):
    MENU_PRINCIPAL = auto()
    GERAR_SENHA = auto()
    GERAR_APELIDO = auto()
    SAIR = auto()


#region 2. Funções isoladas para cada tela (retornam qual deve ser a próxima tela)
def tela_menu_principal() -> Tela:
    print("\n=== MENU PRINCIPAL ===")
    print("[1] Gerar Senha")
    print("[2] Gerar Apelido")
    print("[0] Sair")

    opcao = input("Escolha: ").strip()
    rotas = {
        "1": Tela.GERAR_SENHA,
        "2": Tela.GERAR_APELIDO,
        "0": Tela.SAIR,
    }
    return rotas.get(opcao, Tela.MENU_PRINCIPAL) # Se digitar errado, fica no menu

def tela_gerar_senha() -> Tela:
    print("\n--- GERADOR DE SENHA ---")
    # Sua lógica de gerar senha aqui...
    print("Senha gerada: X9#kL2!pQ")
    input("Pressione Enter para voltar...")
    return Tela.MENU_PRINCIPAL # Volta limpo, sem 'break' maluco

def tela_gerar_apelido() -> Tela:
    print("\n--- GERADOR DE APELIDO ---")
    # Sua lógica de apelido aqui...
    print("Apelido gerado: CyberTupiniquim")
    input("Pressione Enter para voltar...")
    return Tela.MENU_PRINCIPAL

#endregion

# 3. O Loop Principal (Único e plano!)
def iniciar_cli():
    estado_atual = Tela.MENU_PRINCIPAL

    telas = {
        Tela.MENU_PRINCIPAL: tela_menu_principal,
        Tela.GERAR_SENHA: tela_gerar_senha,
        Tela.GERAR_APELIDO: tela_gerar_apelido,
    }

    while estado_atual != Tela.SAIR:
        funcao_tela = telas[estado_atual]
        estado_atual = funcao_tela()

    print("Até mais!")

if __name__ == "__main__":
    iniciar_cli()

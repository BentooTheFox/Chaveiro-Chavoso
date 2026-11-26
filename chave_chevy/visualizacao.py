try:
    from database import gerenciamento_de_dados as db
    from principal import clear
    from ferramentas.enfeites.artista_artoso import construir_coloracao, Cores, reset
    from objetos.tela import Tela

except:
    from .database import gerenciamento_de_dados as db
    from .principal import clear
    from .ferramentas.enfeites.artista_artoso import construir_coloracao, Cores, reset
    from .objetos.tela import Tela


TSU_ASCII = """
                                                               
                                 AAAAA                         
                                 AAAAAAA                       
                                     AAA                       
                                   AAAAA                       
                                   AAA                         
                                   AAA                         
       AAAA                        AAA               AAA       
       AAAA                                         AAAA       
       AAAA          AAAAAAAAAAAAAAAAAAAAA          AAAA       
       AAAAAA      AAAAAAAAAAAAAAAAAAAAAAAAA       AAAAA       
       AAAAAA    AAAAAAAAAAAAAAAAAAAAAAAAAAAAA    AAAAAA       
       AAAAAA  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  AAAAAA       
      AAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA      
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
         AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA         
           AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA           
           AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA           
             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA             
               AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA               
                         AAAAAAAAAAAAA                         
                                                               

"""


def imprimir_tabela(lista_de_dicionarios_de_logins: list[dict]):
    LINHA = "[ID] {} -- [USR] -- {}  -- [SNH] -- {}"
    TAMANHO_DO_DICIONARIO = len(lista_de_dicionarios_de_logins)

    maior_numero_de_idd = max(
        len(str(dicionario["id"])) for dicionario in lista_de_dicionarios_de_logins
    )
    tamanho_da_coluna_central = max(
        len(dicionario["nome"]) for dicionario in lista_de_dicionarios_de_logins
    )

    def __imprimir__(bloco):
        for login in bloco:
            nome = login["nome"]
            idd = str(login["id"])
            
            diferenca = tamanho_da_coluna_central - len(nome)
            
            if not diferenca % 2 == 0:
                diferenca += 1

            espaço_restante = diferenca // 2 * " "

            nome = espaço_restante + nome + espaço_restante
            idd = idd + " " * (maior_numero_de_idd - len(idd))

            if tamanho_da_coluna_central - len(nome) == -1:
                nome = nome[1:]

            print(
                LINHA.format(
                    idd,
                    nome,
                    login["senha"],
                )
            )

    if TAMANHO_DO_DICIONARIO > 10:
        for pagina in range(0, TAMANHO_DO_DICIONARIO, 10):
            __imprimir__(lista_de_dicionarios_de_logins[pagina : pagina + 10])
            input(
                f"""
--- Próxima página (para voltar, digite 99) [{pagina+10}/{TAMANHO_DO_DICIONARIO}] >> """
            )
            clear()
    else:
        __imprimir__(lista_de_dicionarios_de_logins)


def iniciar_loop():
    clear()
    print(construir_coloracao(cor_do_texto=Cores.AZUL), TSU_ASCII)
    reset()

    # Imprimir tabela

    dados = db.consultar_logins()
    print("hell yeah" if dados else 9090)

    if not dados:
        print("Ops! Você ainda não criou nenhum perfil!")
    else:
        imprimir_tabela(dados)

    # input("[ Pressione Enter para voltar ]")

    return Tela.PRINCIPAL


if __name__ == "__main__":
    from criacao import criar_em_massa

    criar_em_massa(30)
    iniciar_loop()

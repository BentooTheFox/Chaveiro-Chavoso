try:
    from database import gerenciamento_de_dados as db
    from principal import clear
    from ferramentas.artista_artoso import construir_coloracao, Cores, reset
    from objetos.tela import Tela
    from ferramentas.imprimir_tabela import imprimir_tabela
except:
    from .database import gerenciamento_de_dados as db
    from .principal import clear
    from .objetos.tela import Tela
    from .ferramentas.artista_artoso import construir_coloracao, Cores, reset
    from .ferramentas.imprimir_tabela import imprimir_tabela


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

def iniciar_loop():
    clear()
    print(construir_coloracao(cor_do_texto=Cores.AZUL), TSU_ASCII)
    reset()

    # Imprimir tabela

    dados = db.consultar_logins()

    if not dados:
        print("Ops! Você ainda não criou nenhum perfil!")
    else:
        imprimir_tabela(dados)

    input("[ Pressione Enter para voltar à tela principal]")

    return Tela.PRINCIPAL

if __name__ == "__main__":
    from criacao import criar_em_massa

    criar_em_massa(30)
    iniciar_loop()

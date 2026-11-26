### ESTRUTURA DO PROJETO
CHAVEIRO CHAVOSO.git:
│   .gitignore
│   main.py -> Reunião e orquestramento do fluxo dos estados do programa
│   readme.txt -> :3 readme
|
├───chave_chevy
│   │   criacao.py        -> Arquivo responsável APENAS pela CRIAÇÃO de novos perfis
│   │   edicao.py         -> || APENAS pela EDIÇÃO de perfis existentes
│   │   exclusao.py       -> || APENAS pela EXCLUSÃO de perfis existentes
│   │   principal.py      -> || APENAS pela INTRODUÇÃO ao programa
│   │   visualizacao.py   -> || APENAS pela VISUALIZACAO e checagem de perfis existentes
│   │   
│   ├───database
│   │       gerenciamento_de_dados.py -> Manipulação do banco de dados
│   │       sql_queries.py -> Strings grandes de queries SQL (para não poluir o código do ´gerenciamento_de_dados.py´)
│   │       verificador_de_integridade_de_caminho.py -> Pequena ferramenta que garante que o caminho até o banco de dados seja 100% garantido
│   │       
│   ├───ferramentas
│   │   │   geramento_chavoso.py -> Geração de nicks e senhas + customização
│   │   │   
│   │   └───enfeites
│   │           artista_artoso.py -> Programinha extra para automatizar enfeites e efeitos artísticos sem o colorama
│   │           
│   └───objetos
│           tela.py -> Objeto 'Tela'
│           
└───data # (Gerado automaticamente pelo programa)
        Clavium.db -> Banco de dados onde os perfis são guardados
        












### ESTRUTURA DE MENUS/TELAS

Todo menu contém 3 partes:
- Texto/Painel - Mostra ao usuário onde ele está e o que está acontecendo no momento, um ESTADO.
- Instrução - Diz ao usuário o que o PROGRAMA espera que o usuário faça/diga
- Retorno - RETORNA a resposta do usuário para o programa principal e (É AQUI que ocorre a MUDANÇA de ESTADO)


# Parte 1 - Texto/Painel
Geralmente, os painéis terão uma estrutura como essa abaixo:

ARTE ASCII
BANNER/Instrução

[opções disponíveis/orientação]

99 - Voltar/Sair
------

>> prompt de input e aguardar movimento do usuário


# Parte 2 - Instrução
    Nessa parte, dedico-me a impedir o usuário de avançar
    e TAMBÉM o programa de quebrar caso haja alguma resposta inválida.
    Em outras palavras, o usuário ficará "preso" aqui até que
    responda de forma válida OU que feche o programa.
    Exemplo (meramente explicativo):
    
    while True:
        # ... Kool Kode
        if INVALID:
            print("Ops! Try again brah")
            continue

        return usr # <--- Esse retorno é a própria Parte 3

# Parte 3
    Retornar resposta ao programa principal,
    onde ele processará o retorno do usuário


MANTRA: "MENU NÃO É PAINEL DE CONTROLE, É ORIENTADOR."




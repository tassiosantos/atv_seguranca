from conect_db import *



def create_senha_pura(login, senha):
    iniciar_conexao()
    create_register(login, senha, "")


def read_senha_pura(login, senha):
    iniciar_conexao()
    registro = read_register(login, senha, "")
#    print(registro)
    return registro


# create_senha_pura("maria", "mariabonita")    
    
# read_senha_pura("maria", "mariabonita")

# create_senha_pura("joao", "123asd")


# read_senha_pura("joao", "123asd")
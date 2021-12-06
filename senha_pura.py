from conect_db import *



def create_senha_pura(__self__, nome, senha):
    iniciar_conexao()
    create_register(nome, senha, "")


def read_senha_pura(__self, nome, senha):
    iniciar_conexao()
    read_register(nome, senha, "")



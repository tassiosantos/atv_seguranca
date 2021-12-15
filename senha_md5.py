import os
import hashlib

from conect_db import *
from salt import *
   

def generate_hash(senha):
    result = hashlib.md5(senha.encode()).hexdigest()
    return result


def create_senha_md5(login, senha):
    iniciar_conexao()
    hash = generate_hash(senha)
    create_register(login, hash,"null")
    

def read_senha_md5(login, senha):
    iniciar_conexao()
    hash = generate_hash(senha)
    registro = read_register(login, hash, "null")
#    print(registro)
    return registro


# create_senha_md5("maria", "mariabonita")    
    
# read_senha_md5("maria", "mariabonita")

# create_senha_md5("joao", "123asd")


# read_senha_md5("joao", "123asd")

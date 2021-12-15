import os
import hashlib

from conect_db import *
from salt import *
   

def generate_hash(senha):
    result = hashlib.md5(senha.encode()).hexdigest()
    return result


def create_senha_md5_salt(login, senha):
    iniciar_conexao()
    salt = generate_salt();
    hash = generate_hash(senha + salt)
    create_register(login, hash, salt)
    

def read_senha_md5_salt(login, senha):
    iniciar_conexao()
    salt = get_salt(login)
    #print(salt[0][0])
    hash = generate_hash(senha + salt[0][0])
    #print(hash)
    
    registro = read_register(login, hash, salt[0][0])
    #print(registro)
    return registro
    
    
#create_senha_md5_salt("maria", "mariabonita")    
    
#read_senha_md5_salt("maria", "mariabonita")

#create_senha_md5_salt("joao", "123asd")


#read_senha_md5_salt("joao", "123asd")

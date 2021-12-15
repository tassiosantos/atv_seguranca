from logging import exception
from os import *
from datetime import date
from senha_pura import *
from senha_md5 import *
from senha_md5_salt import *


def iniciar():
    print("Programa para exibir a autenticação")

def novo_cadastro(num):
    try:
        print("Digite o login:")
        login = input()
        
        print("Digite a senha:")
        senha = input()
        
        if(num == "0"):
            create_senha_pura(login, senha)
        
        elif(num == "1"):
            create_senha_md5(login, senha)
        
        elif(num == "2"):
            create_senha_md5_salt(login, senha)
        
        print("Cadastro realizado com sucesso!")
    except:
        print("Erro no cadastro")
    
    
def buscar_cadastro(num):
    try:
        print("Digite o login para acessar:")
        login = input()
        
        print("Digite a senha de acesso:")
        senha = input()
        
        
        
        if(num == "0"):
            cadastro = read_senha_pura(login, senha)
        
        elif(num == "1"):
            cadastro = read_senha_md5(login, senha)
        
        elif(num == "2"):
            cadastro = read_senha_md5_salt(login, senha)
        
        if(cadastro == []):
            print("Login ou senha incorreto. Falha na autenticação")    
        else:
            print("Autenticado com sucesso:")
            print(cadastro)
        
        
    except:
        print("login ou senha inválido")
    
    

if __name__ == '__main__':
    
    iniciar()
    
    continuar = True
    
    while(continuar):
        print("Qual altenticação deseja realizar\n")
        print("0 - Login e senha aberta\n")
        print("1 - Login e senha criptografada\n")
        print("2 - Login e senha criptografada (salt)\n")
        
        num = input()
        
        print("Qual operação deseja fazer:\n")
        print("0 - Criar novo cadastro\n")
        print("1 - Buscar um cadastro\n")
        
        op = input();
        
        if (op == "0"):
            novo_cadastro(num)
        elif (op == "1"):
            buscar_cadastro(num)
        
        print("Deseja realizar uma nova operação? S/N")
        
        escolha = input().capitalize()
        
        if(escolha == "N"):
            continuar = False
        else:
            continuar = True
            
        
        
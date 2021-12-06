import MySQLdb # para o MySQL

global con
global cursor



def iniciar_conexao():
    global con
    global cursor

    con = MySQLdb.connect('localhost', 'root', 'root')
    con.select_db('atv_seguranca')
    cursor = con.cursor()

def create_register(nome, senha, hash):
    global cursor
    return cursor.execute(f'INSERT INTO LOGIN (nome, senha, hash) VALUES (?,?.?)', ({nome}, {senha},{hash}))

def read_register(nome, senha, hash):
    global cursor
    return cursor.execute(f'SELECT nome, senha FROM LOGIN WHERE nome = {nome} AND senha = {senha} AND hash = {hash}')
    

def update_register(nome, senha):
    return True

def delete_register(nome, senha):
    global cursor
    cursor.execute(f'DELETE FROM LOGIN WHERE nome = {nome} AND senha = {senha}')
    return True



import mysql.connector


global con
global cursor



def iniciar_conexao():
    global con
    global cursor

    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root",
        database = "atv_seguranca"
    )
    cursor = con.cursor()

def create_register(login, senha, hash):
    global cursor
    if(hash == "null"):
        stmt = f'INSERT INTO login (login, senha, hash) VALUES (\'{login}\',\'{senha}\',null)'
    else:
        stmt = f'INSERT INTO login (login, senha, hash) VALUES (\'{login}\',\'{senha}\',\'{hash}\')'
    cursor.execute(stmt)
    con.commit();

def read_register(login, senha, hash):
    global cursor
    if(hash == "null"):
        stmt = f'SELECT * FROM login WHERE login = \'{login}\' AND senha = \'{senha}\' AND hash is {hash};'
    else:
        stmt = f'SELECT * FROM login WHERE login = \'{login}\' AND senha = \'{senha}\' AND hash = \'{hash}\';'

    cursor.execute(stmt)

    return cursor.fetchall()
    

def update_register(login, senha):
    return True

def delete_register(login, senha):
    global cursor
    cursor.execute(f'DELETE FROM LOGIN WHERE login = {login} AND senha = {senha}')
    return True

def get_salt(login):
    global cursor
    cursor.execute(f'SELECT hash FROM login WHERE login = \'{login}\'')
    salt = cursor.fetchall()
    return salt

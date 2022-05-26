import pyodbc 
import enviroment


server = enviroment.server 
database = enviroment.database
username = enviroment.username
password = enviroment.password

def conecta():
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        return cursor
    except Exception:
        print('ErroConexao')
def desconecta(cursor):
    try:
        cursor.close()
        print('DesconexaoEfetuadaComSucesso')
    except Exception:
        print('Erro')
    



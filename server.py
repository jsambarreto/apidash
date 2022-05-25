from base64 import encode
import collections

import pyodbc 
import json
import enviroment
from models.matriculas import welcome_from_dict
from models.vagas import Escola

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = enviroment.server 
database = enviroment.database
username = enviroment.username
password = enviroment.password

data=[]
#Sample select query
#query = 'select pes_id_pessoa, pes_nm_pessoa, pes_nu_cpf_cgc from pes_pessoa'
def select_query(query):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d["id"] = int(row[0])
        d["nome"] = row[1]
        d["cpf"] = row[2]
        objects_list.append(d)

    j = json.dumps(objects_list)
    cursor.close()
    return j
#print(select_query('select top 10 pes_id_pessoa, pes_nm_pessoa, pes_nu_cpf_cgc from pes_pessoa'))
def matriculas(query):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d["Id_escola"] = int(row[0])
        d["Escola"] = row[1]
        d["Zona"] = row[2]
        d["Ano"] = row[3]
        d["G1"] = row[4]
        d["G2"] = row[5]
        d["G3"] = row[6]
        d["G4"] = row[7]
        d["G5"] = row[8]
        d["A1"] = row[9]
        d["A2"] = row[11]
        d["A3"] = row[11]
        d["A4"] = row[12]
        d["A5"] = row[13]
        d["A6"] = row[14]
        d["A7"] = row[15]
        d["A8"] = row[16]
        d["A9"] = row[17]
        d["EJAI"] = row[18]
        d["EJAII"] = row[19]
        d["EJAIII"] = row[20]
        d["EJAIV"] = row[21]
        d["EJAV"] = row[22]
        d["MEI"] = row[23]
        d["MF9"] = row[24]
        d["MEJ"] = row[25]
        d["CF"] = row[26]
        d["Total"] = row[27]
        objects_list.append(d)
    j = json.dumps(objects_list)
    cursor.close()
    return j

def vagas(query):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d["ID_ESCOLA"] = int(row[0])
        d["SERIE"] = row[1]
        d["CURSANDO"] = row[2]
        d["CAPACIDADE"] = row[3]
        d["VAGAS"] = row[4]
        d["ID_ESCOLA"] = int(row[5])
        d["ESCOLA_RESUMIDO"] = row[6]
        d["ESCOLA_COMPLETO"] = row[7]
        d["DIRETOR"] = row[8]
        d["TELEFONE"] = row[9]
        d["LATITUDE"] = row[10]
        d["LONGITUDE"] = row[11]
        d["ENDERECO"] = row[12]
        d["EMAIL"] = row[13]
        objects_list.append(d)
    j = json.dumps(objects_list)
    cursor.close()
    return j

def lista_escolas(query):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d["ID_ESCOLA"] = int(row[0])
        d["ESCOLA_COMPLETO"] = row[1]
        objects_list.append(d)
    j = json.dumps(objects_list)
    cursor.close()
    return j

#Em teste#
def escola_encoder(escola):
    if isinstance(escola, Escola):
        return{'ID_ESCOLA':escola.email, 'ESCOLA_COMPLETO':escola.escola_completo }
    raise TypeError(f'Object {escola} is not of type Escola')


def vagas_teste(query):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    object_list=[]
    for row in rows:
        json_escola = json.dumps(row, default=escola_encoder, indent=4)
        object_list.append(json_escola)
    cursor.close()
    return object_list
#####
from flask import Flask

from server import matriculas, select_query

app = Flask(__name__)

#Rora padrão
@app.route('/')
def home():
  return select_query('select top 10 pes_id_pessoa, pes_nm_pessoa, pes_nu_cpf_cgc from pes_pessoa')

@app.route('/matriculas')
def matricula():
  return matriculas('select * from SGR2_Totais_Matricula_Escola_todos_anos where ano = 2022')


if __name__ == "__main__":
  debug = True # com essa opção como True, ao salvar, o "site" recarrega automaticamente.
  app.run(host='0.0.0.0', port=5000, debug=debug)

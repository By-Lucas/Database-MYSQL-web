from psycopg2 import connect
import mysql.connector
from mysql.connector import errorcode

# CONEXÃO DE BANCO DE DADOS WEB
# COMPATIVEL COM MYSQL : AWS, AZURE, CLOUD CLOUTERS, UOL, dentre outros.


config = {
  'user': 'usuario do database',
  'password': 'senha do database',
  'host': 'hoste de coexão com database',
  'database': 'banco de dados criado',
  'port': 'porta do database',
  'raise_on_warnings': True
}


# Construir conexão  de string e verificar possiveis erros
try:
   conn = mysql.connector.connect(**config)
   print("Conexão estabelecida com banco de dados")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Nome ou senha do banco de dados incorreto!")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Banco de dados não existe")
  else:
    print(err)
else:
  cursor = conn.cursor()

  
  # Apagar tabela existente 

  cursor.execute("DROP TABLE IF EXISTS usuarios;")
  cursor.execute("DROP TABLE IF EXISTS clientes;")
  print("Tabela apagada, tabela existente!") 
  

  # Criar tabelas que ainda não existe, se existir nao vai ser criado
  
  cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
  codigo int(4) AUTO_INCREMENT,
  nome varchar(30) NOT NULL,
  email varchar(50) NOT NULL,
  senha varchar(50) NOT NULL,
  data_cliente varchar(50) NOT NULL,
  PRIMARY KEY (codigo)
  );""")
  print('Tabela criada tabela usuarios no Clouters!')
  
    # Inserir informacoes dentro da tabela
  inserir_usuarios = cursor.execute("""INSERT INTO usuarios(codigo, nome, email, senha, data_cliente) 
  VALUES (null, 'carlos', 'carlos@gmail.com', '123', '25/05/2022');
  """)
  print("Inserido",cursor.rowcount,"usuario(s) no Banco de dados")
  


  cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
  id INT(5) NOT NULL AUTOINCREMENT,
  nome varchar(70) NOT NULL,
  email varchar(70) NOT NULL,
  cidade varchar(70) NOT NULL,
  produto varchar(70) NOT NULL,
  telefone varchar(70) NOT NULL,
  observacoes varchar(400),
  data_1 varchar(70) NOT NULL,
  data_2 varchar(70) NOT NULL
  PRIMARY KEY (id)
  );
  """)
  print('Tabela criada tabela clientes no Clouters!')

  
  # Inserir informacoes dentro da tabela
  inserir_clientes = cursor.execute("""INSERT INTO usuarios(id, nome, email, cidade, produto, telefone, observacoes, data_compra, data_1, data_2) 
  VALUES (null, 'lucas', 'lucas@gmail.com', 'CG', 'Iphone', '74981199190', 'Enviar produto e N. Fiscal','25/05/2021', '25/05/2022');
  """)
  print("Inserido",cursor.rowcount,"cliente(s) no Banco de dados")
  


  # Ler banco de dados SELECIONADO
  cursor.execute("SELECT * FROM usuarios;")
  rows = cursor.fetchall()
  print("Voce tem",cursor.rowcount,"usuarios cadastrados.")


  mostrar = cursor.execute("SELECT * FROM usuarios;")
  olhar = cursor.fetchall()

  # Mostrar tabela de usuarios cadastrados
  for i in rows:
  	print(i)

  # Fechar banco de dados
  conn.commit()
  cursor.close()
  conn.close()



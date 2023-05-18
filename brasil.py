from teste import conectar

def listar(conn, cursor):
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tribo")

    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)
        
    cursor.close()
    conn.close()


def inserir(id, nome, nhabitantes, rendaMensal, escolaridade, assalariado):
    conn = conectar()

    cursor = conn.cursor()

    sql = "INSERT INTO tribo(id, nome, nhabitantes, rendaMensal, escolaridade, assalariado) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id, nome, nhabitantes, rendaMensal, escolaridade, assalariado)
    cursor.execute(sql, val)

    conn.commit()

    print("Registro inserido com sucesso.")

    cursor.close()
    conn.close()

def atualizar(id, nome, nhabitantes, rendaMensal, escolaridade, assalariado):
    conn = conectar()

    cursor = conn.cursor()

    sql = "UPDATE tribo SET nome = %s WHERE id = %s"
    val = (id, nome, nhabitantes, rendaMensal, escolaridade, assalariado)
    cursor.execute(sql, val)

    conn.commit()

    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")

    cursor.close()
    conn.close()

def deletar(id):
    conn = conectar()

    cursor = conn.cursor()

    sql = "DELETE FROM tribo WHERE codigo = %s"
    val = (id)
    cursor.execute(sql, val)

    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    cursor.close()
    conn.close()


conn = conectar()
cursor = conn.cursor()
while True:
  print("O que você deseja fazer?")
  print("1 - Listar tribos")
  print("2 - Inserir nova tribo")
  print("3 - Atualizar uma tribo")
  print("4 - Deletar tribo")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    listar(conn, cursor)
  
  elif opcao == 2:
    id = int(input("Digite o código da nova tribo: "))
    nome_tribo = input("Digite o nome da nova tribo: ")
    habitantes = int(input("Digite o número de habitantes da tribo: "))
    renda_media = float(input("Digite a renda mensal média da tribo: "))
    escolaridade = input("Digite a escolaridade média da tribo (fundamental, médio ou superior): ")
    trabalha = bool(input("Diga possuem trabalho assalariado ou não (0 = não e 1= sim): "))
    inserir(id, nome_tribo, habitantes, renda_media, escolaridade, trabalha)

  elif opcao == 3:
    
    id = int(input("Digite o código da nova tribo: "))
    nome_tribo = input("Digite o nome da nova tribo: ")
    habitantes = int(input("Digite o número de habitantes da tribo: "))
    renda_media = float(input("Digite a renda mensal média da tribo: "))
    escolaridade = input("Digite a escolaridade média da tribo (fundamental, médio ou superior): ")
    trabalha = bool(input("Diga possuem trabalho assalariado ou não (0 = não e 1= sim): "))
    atualizar(id, nome_tribo, habitantes, renda_media, escolaridade, trabalha)

  elif opcao == 4:
    # Deletar um estado
    id = int(input("Digite o código do estado que deseja deletar: "))
    deletar(id)

  elif opcao == 0:
    break

  else:
    print("Opção inválida. Digite novamente.")
    
cursor.close()
conn.close()
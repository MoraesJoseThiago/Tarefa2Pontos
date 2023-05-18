from codigoAfrica import conectar

def listar(conn, cursor):
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM animal_nativo")

    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)
        
    cursor.close()
    conn.close()


def inserir(id, raca, quantidade, risco, area):
    conn = conectar()

    cursor = conn.cursor()

    sql = "INSERT INTO animal_nativo (id, raca, quantidade, risco, area) VALUES (%s, %s, %s, %s, %s)"
    val = (id, raca, quantidade, risco, area)
    cursor.execute(sql, val)

    conn.commit()

    print("Registro inserido com sucesso.")

    cursor.close()
    conn.close()

def atualizar(id, raca, quantidade, risco, area):
    conn = conectar()

    cursor = conn.cursor()

    sql = "UPDATE animal_nativo SET nome = %s WHERE id = %s"
    val = (id, raca, quantidade, risco, area)
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

    sql = "DELETE FROM animal_nativo WHERE codigo = %s"
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
  print("1 - Listar animais")
  print("2 - Inserir nova animal")
  print("3 - Atualizar um animal")
  print("4 - Deletar animal")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    listar(conn, cursor)
  
  elif opcao == 2:
    id = int(input("Digite o código do novo animal: "))
    raca = int(input("Digite a raça do animal: "))
    quantidade = float(input("Digite a quantidade: "))
    risco = input("Digite se possui risco de instinção ou não (0 = não e 1 = sim): ")
    area = bool(input("Diga a área que o animal vive(norte, sul, leste ou oeste)"))
    inserir(id, raca, quantidade, risco, area)

  elif opcao == 3:
    
    id = int(input("Digite o código do novo animal: "))
    raca = int(input("Digite a raça do animal: "))
    quantidade = float(input("Digite a quantidade: "))
    risco = input("Digite se possui risco de instinção ou não (0 = não e 1 = sim): ")
    area = bool(input("Diga a área que o animal vive(norte, sul, leste ou oeste)"))
    inserir(id, raca, quantidade, risco, area)

  elif opcao == 4:
    id = int(input("Digite o código do estado que deseja deletar: "))
    deletar(id)

  elif opcao == 0:
    break

  else:
    print("Opção inválida. Digite novamente.")
    
cursor.close()
conn.close()
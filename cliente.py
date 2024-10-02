from socket import *

# Configuração Conexão
HOST = '127.0.0.1'  # Endereço IP local
PORTA = 65432        # Porta escolhida

# Estabelece a conexão
conexao = socket(AF_INET, SOCK_STREAM)
conexao.connect((HOST, PORTA))

# Loop principal do cliente
while True:
    matricula = input("Informe sua matrícula: ")
    senha = input("Informe sua senha: ")
    conexao.send(f"LOGIN {matricula} {senha}".encode())
    resposta = conexao.recv(1024).decode()
    print(resposta)

    if "realizado com sucesso" in resposta:
        while True:
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Visualizar Saldo")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = input("Informe o valor a ser depositado: ")
                conexao.send(f"DEPOSITO {valor}".encode())
                print(conexao.recv(1024).decode())

            elif opcao == "2":
                valor = input("Informe o valor a ser sacado: ")
                conexao.send(f"SACAR {valor}".encode())
                print(conexao.recv(1024).decode())

            elif opcao == "3":
                conexao.send("SALDO".encode())
                print(conexao.recv(1024).decode())

            elif opcao == "4":
                conexao.send("SAIR".encode())
                print(conexao.recv(1024).decode())
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        continue

conexao.close()

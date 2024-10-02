from socket import *

# Configura a Conexão
HOST = '127.0.0.1'  # Endereço IP local
PORTA = 65432        # Porta escolhida

# Estabelece a conexão
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((HOST, PORTA))
sockobj.listen(1)

saldo = 0  # Saldo inicial

while True:
    # Aceita conexão do cliente 
    conexao, endereco = sockobj.accept()
    print('Conectado:', endereco)

    while True:
        # Recebe informação e decodifica para string
        data = conexao.recv(1024)
        if not data:
            break
        mensagem = data.decode()
        print("Cliente:", mensagem)

        # Lógica do servidor
        if mensagem.startswith("LOGIN"):
            _, matricula, senha = mensagem.split()
            if matricula == "matricula" and senha == "123456":
                conexao.send("Login realizado com sucesso.".encode())
            else:
                conexao.send("Falha no login. Tente novamente.".encode())

        elif mensagem.startswith("DEPOSITO"):
            _, valor = mensagem.split()
            saldo += float(valor)
            conexao.send(f"Depósito realizado. Saldo atual: {saldo:.2f}".encode())

        elif mensagem.startswith("SACAR"):
            _, valor = mensagem.split()
            valor = float(valor)
            if valor > saldo:
                conexao.send("Saldo insuficiente.".encode())
            else:
                saldo -= valor
                conexao.send(f"Saque realizado. Saldo atual: {saldo:.2f}".encode())

        elif mensagem == "SALDO":
            conexao.send(f"Saldo atual: {saldo:.2f}".encode())

        elif mensagem == "SAIR":
            conexao.send("Desconectando...".encode())
            break

    print('Desconectado', endereco)
    conexao.close()

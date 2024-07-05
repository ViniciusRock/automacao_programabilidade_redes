import socket
import os

class Cliente:
    def __init__(self, nome, cpf, email, telefone, loja):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.loja = loja

    def __str__(self):
        return f"{self.nome},{self.cpf},{self.email},{self.telefone},{self.loja}"

def verificar_arquivo(nome_arquivo):
    return os.path.exists(nome_arquivo)

def incluir_dados(cliente, nome_arquivo='clientes.txt'):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"{cliente}\n")

def listar_dados(nome_arquivo='clientes.txt'):
    if not verificar_arquivo(nome_arquivo):
        return "Arquivo não encontrado."
    
    if os.path.getsize(nome_arquivo) == 0:
        return "Não há clientes cadastrados."

    with open(nome_arquivo, 'r') as arquivo:
        clientes = arquivo.readlines()
        resposta = "Nome       | CPF        | E-mail         | Telefone   | Loja\n"
        resposta += "-------------------------------------------------------------\n"
        for cliente in clientes:
            nome, cpf, email, telefone, loja = cliente.strip().split(',')
            resposta += f"{nome.ljust(10)} | {cpf.ljust(10)} | {email.ljust(14)} | {telefone.ljust(10)} | {loja}\n"
        return resposta

def pesquisar_dados(cpf, nome_arquivo='clientes.txt'):
    if not verificar_arquivo(nome_arquivo):
        return "Arquivo não encontrado."

    with open(nome_arquivo, 'r') as arquivo:
        clientes = arquivo.readlines()
        for cliente in clientes:
            dados_cliente = cliente.strip().split(',')
            if dados_cliente[1] == cpf:
                return f"Cliente encontrado: {cliente.strip()}"
        return "Cliente não encontrado."

def excluir_dados(cpf, loja, nome_arquivo='clientes.txt'):
    if not verificar_arquivo(nome_arquivo):
        return "Arquivo não encontrado."

    with open(nome_arquivo, 'r') as arquivo:
        clientes = arquivo.readlines()

    clientes_remanescentes = []
    excluido = False
    for cliente in clientes:
        dados_cliente = cliente.strip().split(',')
        if dados_cliente[1] == cpf and dados_cliente[4] == loja:
            excluido = True
        else:
            clientes_remanescentes.append(cliente)
    
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(clientes_remanescentes)

    return "Cliente excluído." if excluido else "Cliente não encontrado ou loja não autorizada para excluir."

def handle_client(connection, address):
    print(f"Conexão estabelecida com {address}")
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        parts = data.split('|')
        command = parts[0]

        if command == "1":
            nome, cpf, email, telefone, loja = parts[1], parts[2], parts[3], parts[4], parts[5]
            cliente = Cliente(nome, cpf, email, telefone, loja)
            incluir_dados(cliente)
            connection.sendall("Cliente incluído com sucesso.".encode())
        elif command == "2":
            resposta = listar_dados()
            connection.sendall(resposta.encode())
        elif command == "3":
            cpf = parts[1]
            resposta = pesquisar_dados(cpf)
            connection.sendall(resposta.encode())
        elif command == "4":
            cpf, loja = parts[1], parts[2]
            resposta = excluir_dados(cpf, loja)
            connection.sendall(resposta.encode())
        elif command == "5":
            connection.sendall("Finalizando conexão.".encode())
            break
        else:
            connection.sendall("Comando inválido.".encode())
    connection.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        connection, address = server.accept()
        handle_client(connection, address)

if __name__ == "__main__":
    main()

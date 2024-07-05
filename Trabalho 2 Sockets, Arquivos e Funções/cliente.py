import socket

def menu():
    print("Selecione uma opção:")
    print("1. Incluir Dados")
    print("2. Listar Dados")
    print("3. Pesquisar Dados")
    print("4. Excluir Dados")
    print("5. Finalizar")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    while True:
        menu()
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            loja = input("Loja: ")
            data = f"1|{nome}|{cpf}|{email}|{telefone}|{loja}"
            client.sendall(data.encode())
            resposta = client.recv(1024).decode()
            print(resposta)
        elif opcao == "2":
            client.sendall("2|".encode())
            resposta = client.recv(1024).decode()
            print(resposta)
        elif opcao == "3":
            cpf = input("CPF: ")
            data = f"3|{cpf}"
            client.sendall(data.encode())
            resposta = client.recv(1024).decode()
            print(resposta)
        elif opcao == "4":
            cpf = input("CPF: ")
            loja = input("Loja: ")
            data = f"4|{cpf}|{loja}"
            client.sendall(data.encode())
            resposta = client.recv(1024).decode()
            print(resposta)
        elif opcao == "5":
            client.sendall("5|".encode())
            resposta = client.recv(1024).decode()
            print(resposta)
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    client.close()

if __name__ == "__main__":
    main()

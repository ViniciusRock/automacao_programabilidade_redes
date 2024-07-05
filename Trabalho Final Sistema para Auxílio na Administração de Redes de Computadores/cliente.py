import socket
import os

def menu():
    print("Selecione uma opção:")
    print("1. Registrar Ocorrência")
    print("2. Enviar Imagem")
    print("3. Finalizar")

def registrar_ocorrencia(client):
    ocorrencia = input("Digite a ocorrência: ")
    data = f"1|{ocorrencia}"
    client.sendall(data.encode())
    resposta = client.recv(1024).decode()
    print(resposta)

def enviar_imagem(client):
    file_path = input("Caminho da imagem: ")
    if not os.path.exists(file_path):
        print("Arquivo não encontrado.")
        return

    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)

    data = f"2|{file_size}|{file_name}"
    client.sendall(data.encode())

    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            client.sendall(chunk)

    resposta = client.recv(1024).decode()
    print(resposta)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    while True:
        menu()
        opcao = input("Opção: ")

        if opcao == "1":
            registrar_ocorrencia(client)
        elif opcao == "2":
            enviar_imagem(client)
        elif opcao == "3":
            client.sendall("3|".encode())
            resposta = client.recv(1024).decode()
            print(resposta)
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    client.close()

if __name__ == "__main__":
    main()

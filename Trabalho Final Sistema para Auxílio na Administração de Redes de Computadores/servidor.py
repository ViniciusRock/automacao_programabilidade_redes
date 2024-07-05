import socket
import os
import threading

def verificar_arquivo(nome_arquivo):
    return os.path.exists(nome_arquivo)

def registrar_ocorrencia(ocorrencia, nome_arquivo='ocorrencias.txt'):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"{ocorrencia}\n")

def handle_client(connection, address):
    print(f"Conexão estabelecida com {address}")
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        parts = data.split('|')
        command = parts[0]

        if command == "1":  # Registrar ocorrência
            ocorrencia = parts[1]
            registrar_ocorrencia(ocorrencia)
            connection.sendall("Ocorrência registrada com sucesso.".encode())
        elif command == "2":  # Enviar imagem
            file_size = int(parts[1])
            file_name = parts[2]
            with open(f"imagens/{file_name}", 'wb') as f:
                bytes_received = 0
                while bytes_received < file_size:
                    chunk = connection.recv(4096)
                    f.write(chunk)
                    bytes_received += len(chunk)
            connection.sendall("Imagem recebida com sucesso.".encode())
        elif command == "3":  # Finalizar
            connection.sendall("Finalizando conexão.".encode())
            break
        else:
            connection.sendall("Comando inválido.".encode())
    connection.close()

def main():
    if not os.path.exists('imagens'):
        os.makedirs('imagens')
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        connection, address = server.accept()
        threading.Thread(target=handle_client, args=(connection, address)).start()

if __name__ == "__main__":
    main()

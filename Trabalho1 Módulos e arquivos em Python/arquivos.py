import os

class Vinho:
    def __init__(self, marca, tipo, teor_alcoolico, preco):
        self.marca = marca
        self.tipo = tipo
        self.teor_alcoolico = teor_alcoolico
        self.preco = preco

def verificar_arquivo(nome_arquivo):
    return os.path.exists(nome_arquivo)

def cadastrar_vinho(marca, tipo, teor_alcoolico, preco, nome_arquivo='vinhos.txt'):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"{marca},{tipo},{teor_alcoolico},{preco}\n")

def listar_vinhos(nome_arquivo='vinhos.txt'):
    if not verificar_arquivo(nome_arquivo):
        print("Arquivo não encontrado.")
        return False
    
    if os.path.getsize(nome_arquivo) == 0:
        print("Não há vinhos cadastrados.")
        return False

    with open(nome_arquivo, 'r') as arquivo:
        vinhos = arquivo.readlines()
        total_precos = 0
        total_vinhos = len(vinhos)
        print("Marca       | Tipo       | Teor Alc. | Preço")
        print("---------------------------------------------")
        for vinho in vinhos:
            marca, tipo, teor_alcoolico, preco = vinho.strip().split(',')
            print(f"{marca.ljust(12)} | {tipo.ljust(10)} | {teor_alcoolico.rjust(9)} | R${preco}")
            total_precos += float(preco)
        print("---------------------------------------------")
        print(f"Total de vinhos cadastrados: {total_vinhos}")
        print(f"Preço médio: R${total_precos / total_vinhos:.2f}")
        return True

def excluir_vinhos(indices_para_excluir, nome_arquivo='vinhos.txt'):
    if not verificar_arquivo(nome_arquivo):
        print("Arquivo não encontrado.")
        return False

    with open(nome_arquivo, 'r') as arquivo:
        vinhos = arquivo.readlines()

    indices = [int(idx.strip()) for idx in indices_para_excluir.split(',')]

    vinhos_remanescentes = [vinho for i, vinho in enumerate(vinhos, 1) if i not in indices]

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(vinhos_remanescentes)
    
    return True

def menu():
    print("Selecione uma opção:")
    print("1. Cadastrar vinho")
    print("2. Listar vinhos")
    print("3. Excluir vinho")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Opção: ")

        if opcao == "1":
            marca = input("Marca: ")
            tipo = input("Tipo: ")
            teor_alcoolico = input("Teor alcoólico: ")
            preco = float(input("Preço: "))
            cadastrar_vinho(marca, tipo, teor_alcoolico, preco)
        elif opcao == "2":
            listar_vinhos()
        elif opcao == "3":
            indices_para_excluir = input("Números das linhas a serem excluídas (separados por vírgula): ")
            excluir_vinhos(indices_para_excluir)
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

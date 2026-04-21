from generator import gerar_senha
from database import (
    create_table,
    insert_password,
    list_passwords,
    get_password_by_id,
    delete_password,
)

def menu():
    print("\n=== GERENCIADOR DE SENHAS ===")
    print("1 - Gerar e salvar nova senha")
    print("2 - Listar senhas salvas")
    print("3 - Ver senha específica")
    print("4 - Apagar senha")
    print("0 - Sair")

def opcao_1():
    service = input("Serviço (ex: Gmail): ")
    username = input("Usuário (opcional): ")
    try:
        tamanho = int(input("Tamanho da senha (padrão 12): ") or 12)
    except ValueError:
        tamanho = 12

    senha = gerar_senha(tamanho=tamanho)
    print(f"\nSenha gerada: {senha}")

    salvar = input("Salvar no banco? (s/n): ").strip().lower()
    if salvar == "s":
        insert_password(service, username, senha)
        print("Senha salva com sucesso!")

def opcao_2():
    senhas = list_passwords()
    if not senhas:
        print("Nenhuma senha cadastrada.")
        return
    print("\nID | Serviço | Usuário | Criado em")
    print("-" * 40)
    for row in senhas:
        _id, service, username, created_at = row
        print(f"{_id} | {service} | {username or '-'} | {created_at}")

def opcao_3():
    try:
        password_id = int(input("ID da senha que deseja ver: "))
    except ValueError:
        print("ID inválido.")
        return
    row = get_password_by_id(password_id)
    if row is None:
        print("Senha não encontrada.")
        return
    _id, service, username, password, created_at = row
    print("\n=== DETALHES DA SENHA ===")
    print(f"ID:       {_id}")
    print(f"Serviço:  {service}")
    print(f"Usuário:  {username or '-'}")
    print(f"Senha:    {password}")
    print(f"Criado em:{created_at}")

def opcao_4():
    try:
        password_id = int(input("ID da senha que deseja apagar: "))
    except ValueError:
        print("ID inválido.")
        return
    delete_password(password_id)
    print("Senha apagada (se existia).")

def main():
    create_table()
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            opcao_1()
        elif opcao == "2":
            opcao_2()
        elif opcao == "3":
            opcao_3()
        elif opcao == "4":
            opcao_4()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

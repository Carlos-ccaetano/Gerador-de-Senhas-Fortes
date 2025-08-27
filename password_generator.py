import random
import string
import csv

def generate_password(length=12, uppercase=True, numbers=True, symbols=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if length < 1:
        raise ValueError("O comprimento da senha deve ser pelo menos 1.")
    if not characters:
        raise ValueError("Nenhum tipo de caractere selecionado para gerar a senha.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_to_csv(password, filename='passwords.csv'):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([password])

if __name__ == "__main__":
    print("Gerador de Senhas Fortes")
    try:
        length = int(input("Comprimento da senha (padrão: 12): ") or 12)
        use_uppercase = input("Incluir letras maiúsculas? (s/n, padrão: s): ").lower() != 'n'
        use_numbers = input("Incluir números? (s/n, padrão: s): ").lower() != 'n'
        use_symbols = input("Incluir símbolos? (s/n, padrão: s): ").lower() != 'n'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Senha gerada: {password}")

        save = input("Salvar senha em 'passwords.csv'? (s/n, padrão: s): ").lower() != 'n'
        if save:
            save_to_csv(password, 'passwords.csv')
            print("Senha salva com sucesso em 'passwords.csv'.")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")



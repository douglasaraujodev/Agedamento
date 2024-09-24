import csv
from datetime import datetime

# Função para agendar exame
def agendar_exame():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    contato = input("Digite seu contato: ")
    data = input("Digite a data desejada para o exame (dd/mm/aaaa): ")
    
    # Verifica se a data está no formato correto
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        print("Data inválida! Tente novamente.")
        return

    # Salva os dados no arquivo CSV
    with open('agendamentos.csv', mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, idade, contato, data])
    
    print("Exame agendado com sucesso!")

# Função para visualizar agendamentos
def visualizar_agendamentos():
    print("\nAgendamentos realizados:")
    try:
        with open('agendamentos.csv', mode='r') as arquivo:
            reader = csv.reader(arquivo)
            for row in reader:
                print(f"Nome: {row[0]}, Idade: {row[1]}, Contato: {row[2]}, Data: {row[3]}")
    except FileNotFoundError:
        print("Nenhum agendamento encontrado.")

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Agendar exame")
        print("2. Visualizar agendamentos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            agendar_exame()
        elif opcao == '2':
            visualizar_agendamentos()
        elif opcao == '3':
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o sistema
if __name__ == "__main__":
    main()

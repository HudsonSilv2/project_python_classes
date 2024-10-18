# Criação da classe Pessoa
class Pessoa:
    nome = 'o'
    idade = 0
    signo = ' '
    tipo_sanguineo = ' '
    peso = 0.0
    cor_ojos = ' '
    altura = 0.0
    hobbies = ['','']


# criação de Pessoas
alex = Pessoa()
maria = Pessoa()
jonas = Pessoa()

# Area de cadastro "Hospital" de Alex

def info_clinica(self, nome, idade, tipo_sanguineo, peso, altura):
    self.nome = nome
    self.idade = idade
    self.tipo_sanguineo = tipo_sanguineo
    self.peso = peso
    self.altura = altura
    
    print(f'{'-'*24} \n')
    print(f"Nome: {self.nome}")
    print(f"Idade: {self.idade}")
    print(f"Tipo Sanguíneo: {self.tipo_sanguineo}")
    print(f"Peso: {self.peso}kg")
    print(f'Altura: {self.altura:.2f}')
    print('\n')
    
def chamar_lista_clinica(pacient1,pacient2,pacient3): # para chamar um array de clientes da clinica
    pacient1 = info_clinica(alex, 'Alex', 25, 'O+', 75.5, 1.80)
    pacient2 = info_clinica(maria, 'Maria', 27, 'AB+', 65.5, 1.70)
    pacient3 = info_clinica(jonas,  'Jonas', 28, 'A' , 68.8, 1.66)
    
    num_pacient = [pacient1,pacient2,pacient3]
    print('\n')
    print(f'Numero de pacientes: {len(num_pacient)}')
    print('\n')
    menu()
    return pacient1, pacient2, pacient3

# Area de cadastro "Agência Esotérica" de Maria

def app_esoterico(self, nome, idade, signo):
    self.nome = nome
    self.idade = idade
    self.signo = signo
    
    print(f'{'-'*24} \n')
    print(f"Nome: {self.nome}")
    print(f"Idade: {self.idade}")
    print(f"Signo: {self.signo}")

def chmar_lista_esoterica(pacient1,pacient2,pacient3): # para chamar um array com usuarios do app de Signos
    pacient1 = app_esoterico(maria, 'Maria', 27, 'Leão')
    pacient2 = app_esoterico(jonas, 'Jonas', 28, 'Leão')
    pacient3 = app_esoterico(alex, 'Alex', 25, 'Leão')
    
    num_pacient = [pacient1, pacient2, pacient3]
    print('\n')
    print(f'Numero de Usuarios: {len(num_pacient)}')
    print('\n')
    menu()
    return pacient1, pacient2, pacient3

# Area de cadastro de "Rede Social" de Jonas

def app_rede_social(self, nome, idade, hobbies, altura):
    self.nome = nome
    self.idade = idade
    self.hobbies = hobbies
    self.altura = altura
    
    print(f'{'-'*24} \n')
    print(f'Nome: {self.nome}')
    print(f'Idade: {self.idade}')
    print(f'Cor dos Olhos: {self.cor_ojos}')
    print(f'Hobbies: {(self.hobbies[0], self.hobbies[1])}')
    print(f'Altura: {self.altura:.2f}')

def chamar_lista_rede_social(user1, user2, user3): # para chamar uma lista de usuarios da rede social 
    user1 = app_rede_social(jonas, 'Jonas', 28, ['Leitura', 'Fotografia'], 1.66)
    user2 = app_rede_social(alex, 'Alex', 25, ['Boxe', 'Música'], 1.80)
    user3 = app_rede_social(maria, 'Maria', 27, ['Artes', 'Ciclismo'], 1.70)
    
    num_users = [user1, user2, user3]
    print('\n')
    print(f'Numero de Usuarios: {len(num_users)}')
    print('\n')
    menu()
    return user1, user2, user3

# menu de opçoes 

def menu():
    print('\n=> Escolha uma opção de informações:')
    print('1 - Clinica medica')
    print('2 - Centro Esoterico')
    print('3 - Redes Sociais')
    print('4 - Sair')

# chamada do menu
menu()

def opcoes():
    while True:
        op = int(input('Opção: '))
        if op == 1:
            print('\n---- Clinica Médica ----')
            chamar_lista_clinica(alex, maria, jonas)
        elif op == 2:
            print('\n---- Centro Esotérico ----')
            chmar_lista_esoterica(maria, jonas, alex)
        elif op == 3:
            print('---- Rede Social ----')
            chamar_lista_rede_social(jonas, alex, maria)
        elif op == 4:
            print('\nSaindo...')
            break
        else:
            print('\n')
            print('Opção inválida. Tente novamente.')
opcoes()
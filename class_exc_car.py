linha = '-' * 24 # linha simplificada 
car8_list = [] # lista com valor inicial dos carros2

# padrão de um carro de brinquedo
class carro_brinquedo:
    modelo = ' '
    cor = ' '
    preco = 0.0
    dimensao = 0.0
    material = ' '
    estoque = 0

# criação de carros 
car1 = carro_brinquedo()
car2 = carro_brinquedo()
car3 = carro_brinquedo()
car4 = carro_brinquedo()
car5 = carro_brinquedo()
car6 = carro_brinquedo()
car7 = carro_brinquedo()
car8 = carro_brinquedo()

# método para cadastrar um novo carro
def new_toy(self, modelo, cor, preco, dimensao, material, estoque):
    self.modelo = modelo
    self.cor = cor
    self.preco = preco
    self.dimensao = dimensao
    self.material = material
    self.estoque = estoque
    
    
    print(linha)
    print(f'Modelo: {self.modelo}')
    print(f'Cor: {self.cor}')
    print(f'Preço: R${self.preco:.2f}')
    print(f'Dimensão: {self.dimensao} cm²')
    print(f'Material: {self.material}')
    print(f'Estoque: {self.estoque} unidades')
    print('\n') 
    

# criar um novo carro 
def create_toy(car8):
    print("Você está criando um novo carro")
    print('\n')
    
    car8.modelo = input('Modelo do carro: ')
    car8.cor = input('Cor do carro: ')
    car8.preco = float(input('Preço do carro: '))
    car8.dimensao = float(input('Dimensão do carro (cm²): '))
    car8.material = input('Material do carro: ')
    car8.estoque = int(input('Estoque do carro: '))
    print('\n')
    
    new_toy(car8, car8.modelo, car8.cor, car8.preco, car8.dimensao, car8.material, car8.estoque)
    return car8


# devolve uma lista dos carros registrados
def qt_toy(car1, car2, car3, car4, car5, car6, car7, car8):
    car1 = new_toy(car1, 'Mario Kart', 'Preto e Vermelho', 64.90, 16.2, 'Plastico', 10)
    car2 = new_toy(car2, 'Trator', 'Azul', 59.90, 12.5, 'Plastico', 15)
    car3 = new_toy(car3, 'Ben-10 Car', 'Verde', 69.90, 15.7, 'Plastico', 5)
    car4 = new_toy(car4, 'Lamborguini', 'Vermelho', 49.90, 9.5, 'Plastico', 12)
    car5 = new_toy(car5, 'Camaro', 'Amarelo', 49.90, 7.8, 'Plastico', 20)
    car6 = new_toy(car6, 'Pac-Man Car', 'Verde', 49.90, 7.5, 'Plastico', 18)
    car7 = new_toy(car7, 'Carro do Sonic', 'Azul', 59.90, 12.5, 'Plastico', 10)
    car8 = new_toy(car8, car8.modelo, car8.cor, car8.preco, car8.dimensao, car8.material, car8.estoque)
    
    car_list = [car1, car2, car3, car4, car5, car6, car7, car8]
    
    return car_list.append(car8)


# ------------------------- Menu ---------------------------------
def menu():
    print('\n')
    print('1 - Novo Carro')
    print('2 - Listar Carros')
    print('3 - Sair')
    print('\n')

menu()

# Opcoes do menu 
def opcoes():
    while True:
        opcao = int(input('Escolha uma opção: '))
        print('\n')
        if opcao == 1:
            create_toy(car8)
            menu()
        elif opcao == 2:
            qt_toy(car1, car2, car3, car4, car5, car6, car7, car8)
            menu()
        elif opcao == 3:
            print('Saindo...')
            break
        else:
            print('Opção inválida!')
            print('\n')

opcoes()
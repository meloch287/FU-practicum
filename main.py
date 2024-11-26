# Создание текстового файла
with open('products.txt', 'w') as file:
    file.write("Яблоко: 50\n")
    file.write("Банан: 30\n")
    file.write("Апельсин: 40\n")
    file.write("Груша: 60\n")
    file.write("Виноград: 70\n")

# Функция для поиска цены товара
def F_P(x):
    with open('products.txt', 'r') as file:
        for l in file:
            name, price = l.strip().split(': ')
            if name == x:
                return price
    return "Цена не известна"

while True:
    x = input('Введите товар, который хотите найти (или "next" для завершения): ')
    if x.lower() == 'next':
        break
    print(f"Цена на {x}: {find_price(x)}")

# Функция для добавления новых товаров с клавиатуры
def ADD_P():
    NP = []
    while True:
        PN = input("Введите название товара, который хотите добавить (или 'next' для завершения): ")
        if PN.lower() == 'next':
            break
        price = input("Введите цену товара: ")
        NP.append(f"{PN}: {price}")

    with open('products.txt', 'a') as file:
        for product in NP:
            file.write(f"{product}\n")
            
ADD_P()

# Функция для удаления товара
def RP(x):
    with open('products.txt', 'r') as file: #читает и сохраняет их в список lines.
        lines = file.readlines()

    with open('products.txt', 'w') as file:
        for l in lines:
            name, price = l.strip().split(': ')  # Удаляет пробелы и разделяет строку на имя товара и цену.
            if name != x:
                file.write(l)

while True:
    x = input('Введите товар, который хотите удалить (или "next" для завершения): ')
    if x.lower() == 'next':
        break
    RP(x)
    print(f"Товар {x} удален.")


# Функция для создания нового файла с упорядоченными товарами
def C_S_F():
    with open('products.txt', 'r') as file:
        lines = file.readlines() #читает и сохраняет в список

    P = []
    for line in lines:
        name, price = line.strip().split(': ') #Удаляет пробелы и разделяет строку на имя товара и цену.
        P.append((name, int(price))) # Добавляет кортеж (имя товара, цена) в список

    SP = sorted(P, key=lambda x: x[1])

    with open('sorted_products.txt', 'w') as file:
        for name, price in SP:
            file.write(f"{name}: {price}\n")

    print("Два самых дешевых товара:")
    for name, price in SP[:2]:
        print(f"{name}: {price}")

    print("Два самых дорогих товара:")
    for name, price in SP[-2:]:
        print(f"{name}: {price}")

C_S_F()

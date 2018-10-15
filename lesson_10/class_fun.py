# class_fun.py
# Обновленная функция, которая обрабатывает объект типа (класса) Address.
# Вывести адрес на экран:
def print_address(address):
    print(address.name)
    if len(address.line1) > 0:
        print(address.line1)
    if len(address.line2) > 0:
        print(address.line2)
    print(address.city + ", " + address.zip)

# определяем шаблон адреса
class Address:
    pass

# Создать экземпляр (объект) класса (типа) Address: 
home = Address()

# Задать поля объекта:
home.name = "Иван Иванов"
home.line1 = "Улица"
home.line2 = "Район"
home.city = "СПб"
home.zip = "50125"

print_address(home)


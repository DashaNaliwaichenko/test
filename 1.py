from io import FileIO
#from typing import List, Dict
message1 = ' Выбор опции:' \
           '1 - список контактов' \
           '2 - поиск по адресу электронной  почты' \
           '3 - поиск по ФИО' \
           '4 - поиск контаков с пустыми данными' \
           '5 - редактирование контактов' \
           '6 - поиск по номеру телефона'

message2 = 'Выбор редактирования' \
           '1 - ФИО' \
           '2 - номер телефона' \
           '3 - адрес электронной почты'
class Contact:
    def __init__(self, phonenumber: str = '', name: str = '', mail: str = ''):
        self.phonenumber = phonenumber
        self.name = name
        self.mail = mail
    def serialized(self, delimet = ','):
        return f'{self.phonenumber}{delimet}{self.name}{delimet}{self.mail}'
def deserialize(contact:str, delimit = ',') -> Contact:
    x,y,z = contact.split(delimit)
    return Contact(x,y,z)
def show(contacts):
    for i in range(len(contacts)):
        print(str(i) +'\t' + contacts[i].serialized('\t'))
def find_by_phone_number(contacts):
    print('Введите номер телефона:')
    phonenumber = input()
    for contact in contacts:
        if contact.phonenumber == phonenumber:
            return str(contact)
    return 'Введенный контакт не найден'
def find_by_email(contacts):
    print('Введите адрес электронной почты:')
    mail = input()
    for contact in contacts:
        if contact.mail == mail:
            return str(contact)
    return 'Введенный адрес не найден'
def compare_names(find_name, contact_name):
    if len(find_name) == 0 or contact_name is None:
        return True
    return contact_name == find_name
def find_by_full_name(contacts):
    print('Введите ФИО:')
    full_name = input()
    full_name = full_name.split (' ')
    result = ''
    for contact in contacts:
        if compare_names(full_name[0], contact.surname) and \
                compare_names(full_name[1], contact.name) and \
                compare_names(full_name[2], contact.patronymic):
                result = result + str(contact) + '\n\n'
    if len(result) == 0:
        return 'Введенные данные не найдены'
def find_by_blank_email_or_phone(contacts):
    result = ''
    for contact in contacts:
        if contact.email is None or contact.phone_number is None:
            result = result + str(contact) + '\n\n'
    if len(result) == 0:
        return 'Такие контакты не найдены'
    return result
def edit_contact(contacts):
    print ('Введите номер контакта, который хотите изменить ')
    result = ''
    for i in range (len(contacts)):
        result = result+f'Номер{i+1}\n'+str(contacts[i])+'\n\n'
        print (result)
        number = int(input())
        number -=1
        if 0>number or number>= len(contacts):
            return 'Неверно введен номер'
def Start(file:FileIO):
    contacts = []
    for contact in file.read().split('\n'):
        if contact:
            contacts.append(deserialize(contact))
    while True:
        try:
            vybor = int(input(message1))
        except:
            print('Выбор опции')
            continue
#Выбор функции
        if vybor == 1:
            show(contacts)
        elif vybor == 2:
            find_by_email(contacts)
        elif vybor == 3:
            find_by_full_name(contacts)
        elif vybor == 4:
            find_by_blank_email_or_phone(contacts)
        elif vybor == 5:
            edit_contact(contacts)
        elif vybor == 6:
            find_by_phone_number(contacts)
if __name__ == '__main__':
    file_name = input('Введите адрес')
    with open(file_name, 'r+', encoding='utf-8') as file:
        Start(file)
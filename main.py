from io import FileIO
from typing import List, Dict
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
def show_contacts_keep_ids(contacts:Dict[int,Contact]):
    print('ID\tНомер\tФИО\tEmail')
    for i in contacts:
        print(str(i)+'\t'+contacts[i].serialized("\t"))
def show(contacts):
    for i in range(len(contacts)):
        print(str(i) +'\t' + contacts[i].serialized('\t'))
def find_by_phone_number(phone_number:str,contacts:List[Contact]):
    show_contacts_keep_ids({id:x for id,x in enumerate(contacts) if phone_number in x.phonenumber})
def find_by_email(mail:str,contacts:List[Contact]):
    show_contacts_keep_ids({id:x for id,x in enumerate(contacts) if mail in x.mail})
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
            find_by_phone_number(input("Введите телефон для поиска:"),contacts)
if __name__ == '__main__':
    file_name = input('Введите адрес')
    with open(file_name, 'r+', encoding='utf-8') as file:
        Start(file)

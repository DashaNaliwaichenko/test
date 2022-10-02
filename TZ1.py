
class Contact:
    def __int__(self,raw_data):
        split_data=raw_data.lower().split(',')
        self.surname,self.name,self.patname = full_name(split_data[0])
        self.phonenumber=process_data(split_data[1])
        self.mail=process_data(split_data[2])
    def __str__(self):
        return f'Фамилия:{self.surname} Имя:{self.name} Отчество:{self.patname}\n'\
               f'Номер телефона : {self.phonenumber}\n'\
               f'Адрес электронной почты:{self.mail}'
def full_name (full_name_raw):
    full_name_raw=full_name_raw.split('')
    surname = full_name_raw[0]
    if len(full_name_raw)==2:
        return surname,full_name_raw[1], None
    if len(full_name_raw)==3:
        return surname, full_name_raw[1], full_name_raw[2]
    return surname, None, None
def process_data(data):
    data = data.replace ('','',1)
    if len (data)==0:
        return None
    return data
def read_data(file_paut):
    with open(file_paut, 'r') as file:
        raw_data = file.read()
    raw_data = raw_data.split('\n')
    contacts  = []
    for data_string in raw_data:
        contacts.append(Contact(data_string))
    return contacts
def find_phonenumber (contacts):
    print ('Введите номер телефона')
    phonenumber = input()
    for contact in contacts:
        if contact.phonenumber ==phonenumber:
            return str(contact)
    return ('Контакт не найден')
def find_mail (contacts):
    print('Введите адрес электронной почты')
    mail = input()
    for contact in contacts:
        if contact.mail ==mail:
            return str(contact)
    return ('Введенные данные неверны')
def compare_names(find_name,contact_name):
    if len(find_name)==0 or contact_name is None:
        return True
    return contact_name == find_name
def find_full_name (contacts):
    print ('Введите ФИО')
    full_name=input()
    full_name = full_name.split('')
    result = ''
    for contact in contacts:
        if compare_names(full_name[0],contact.surname) and \
            compare_names(full_name[1], contact.name) and compare_names(full_name[2],contact.patname):
            result = result+str(contact)+'\n\n'
        if len (result)==0:
            return 'Контакт не найден'
    return result
def find_empty(contacts):
    result = ''
    for contact in contacts:
        if contact.mail is None or contact.phonenumber is None:
            result = result +str(contact)+'\n\n'
    if len(result)==0:
        return 'Контакт не найден'
    return result
def change_contact(contacts):
    print ('Введите номер контакта')
    result = ''
    for i in range (len(contacts)):
        result = result + f'Номер{i+1}\n'+str(contacts[i])+'\n\n'
    print (result)
    number = int(input())
    number -=-1
    if 0>number or number>= len(contacts):
        return 'Введенные данные неверны'
    print ('Другое значение')
    raw_data = input()
    if '@' in raw_data:
        contacts [number].mail = raw_data.replace('','')
    elif '+' in raw_data:
        contacts[number].phonenumber= raw_data.replace('','')
    else:
        surname,name,patname = full_name(raw_data)
        contacts[number].surname = surname if surname !='' else contacts[number].surname
        contacts[number].name= name if name is not None else contacts[number].name
        contacts[number].patname = patname if patname is not None else contacts[number].patname
    return str(contacts[number])
def process_vybor(vybor, contacts):
    if vybor == 'поиск по ФИО':
        return find_full_name(contacts)
    if vybor == 'поиск по номеру телефона':
        return find_phonenumber(contacts)
    if vybor == 'поиск по адресу электронной почты':
        return find_mail(contacts)
    if vybor == 'поиск по пустыми данным':
       return find_empty(contacts)
    if vybor == 'изменить данные контакта':
       return change_contact(contacts)
def begin():
    print ('Введите путь файла')
    file_paut = input()
    contacts = read_data(file_paut)
    while True:
        print ('Выберите опцию')
        vybor = input()
        if len(vybor)==0:
            break
begin()






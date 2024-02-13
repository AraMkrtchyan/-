# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. Создание файла:
#   - открываем файл на дозапись # a
# 2. Добавление контакта:
#   - запросить у пользователя новый контакта
#   - открыть файл на дозапись # a
#   - добавить новый контакт
# 3. Вывод данных на экран:
#   - открыть файл на чтение # r
#   - считать файл
#   - вывести на экран
# 4. Поиск контакта:
#    - выбор варианта поиска
#    - запросить данные для поиска
#    - открыть файл на чтение
#    - считываем данные файла, сохранить их в переменную
#    - осуществляем поиск контакта
#    - выводим на экран найденный контакта
# 5. Создание UI:
#   - вывести меню на экран
#   - запросить у пользавателя вариант действия
#   - запустить соответствующую функцию
#   - осуществить возможность выхода из программы
def Input_Lastname():
    return input("Введите фамилю контакта: ").title()


def Input_name():
    return input("Введите имя контакта: ").title()


def Input_Patronymic():
    return input("Введите отчество контакта: ").title()


def Input_Phone():
    return input("Введите телефон контакта: ")


def Input_address():
    return input("Введите адресс(город) контакта: ").title()


def Create_contact():
    surname = Input_Lastname()
    name = Input_name()
    patronymic = Input_Patronymic()
    phone = Input_Phone()
    address = Input_address()
    return f"{surname} {name} {patronymic} {phone}\n {address}\n\n"


def Add_Contact():
    with open("Phonebook.txt", "a", encoding="utf-8") as file:
        file.write(Create_contact())


def Print_Contacts():
    with open("Phonebook.txt", "r", encoding="utf-8") as file:
        with open("Phonebook.txt", "r", encoding="utf-8") as file:
            contacts_str = file.read()
        contactslist = contacts_str.strip().split("\n\n")
        for n, contact in enumerate(contactslist, 1):
            print(n, contact)


def Search_Contact():
    print(
        "Возможние варианти поиска:\n"
        "1.По фамиллии\n"
        "2.По имени\n"
        "3.По отчеству\n"
        "4.По телефону\n"
        "5.По адрессу\n"
    )

    var = input("Виберите вариант поиска: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод!")
        var = input("Виберите вариант поиска: ")
    ivar = int(var) - 1
    search = input("Введите данные для поиска: ").title()
    with open("Phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()
    contactslist = contacts_str.strip().split("\n\n")
    for str_contact in contactslist:
        lst_contact = str_contact.replace(":", "").split()
        if search in lst_contact[ivar]:
            print(str_contact)


def Copy_Contact():
    num = int(input("Введите номер контакта: "))
    with open("Phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()
    contactslist = contacts_str.strip().split("\n\n")
    for n, contact in enumerate(contactslist, 1):
        if num == n:
            print(n, contact)
            with open("CopyPhonebook.txt", "a", encoding="utf-8") as file:
                print()
                file.write(contact)



def interface():
    with open("Phonebook.txt", "a", encoding="utf-8"):
        pass
    var = 0
    while var != "5":

        print(
            "Возможние варианти:\n"
            "1.Добавление контакта\n"
            "2.Вывод на экран\n"
            "3.Поиск контакта\n"
            "4.Копирование\n"
            "5.выход"
        )
        print()
        var = input("Виберите вариант действия: ")
        while var not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод!")
            var = input("Виберите вариант действия: ")
        print()
        match var:
            case "1":
                Add_Contact()
            case "2":
                Print_Contacts()
            case "3":
                Search_Contact()
            case "4":
                Copy_Contact()
            case "5":
                print("До свидания")
        print()


if __name__ == "__main__":
    interface()

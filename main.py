
from collections import UserDict

class Field:
    def __init__(self, value: str) -> None:
        self.__field = value

    def get_field(self) -> str:
        return self.__value
    
    def set_field(self, field) -> None:
        self.__value = field

    def __str__(self) -> str:
        return self.__value


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)

class Record():
    def __init__(self, name: Name, phone: Phone = None, phones: list = None) -> None:
        self.name = name
        if phone:
            self.__phones = [phone]
        elif phones:
            for el in phones:
                if type(el) != Phone:
                    raise TypeError('List of phones must contain only elements of Phone class')
            self.__phones = phones
        else:
            self.__phones = []
    
    def add_phone(self, phone: Phone) -> None:
        self.__phones.append(phone)
    
    def remove_phone(self, index: int) -> None:
        self.__phones.pop(index)          
    
    def edit_phone(self, index: int, new_phone: str) -> None:
        self.__phones[index].set_field(new_phone)
    
    def __str__(self) -> str:
        result = self.name.__str__() + ': '
        for phone in self.__phones:
            result += phone.__str__() + ', '
        return result[0, -2]

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.get_field()] = record

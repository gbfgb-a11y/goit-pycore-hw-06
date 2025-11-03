from collections import UserDict

class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("Phone must be a string")
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)


    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if isinstance(phone, Phone):
            phone = phone.value
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if isinstance(phone, Phone):
            phone = phone.value
        isornot2 = self.find_phone(phone)
        if isornot2 is not None:
            self.phones.remove(isornot2)
        else:
            raise ValueError('Phone does not exist.')
        

    def edit_phone(self, old_phone, new_phone):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        validcount = 0
        if isinstance(old_phone, Phone):
            pass
        if isinstance(new_phone, Phone):
            pass
        if new_phone and old_phone:
            for i, a in enumerate(self.phones):
                if a.value == old_phone:
                    if len(new_phone) == 10:
                        for i in new_phone:
                            if i in numbers:
                                validcount+=1
                            else:
                                pass
                        if validcount == 10:
                            self.add_phone(new_phone)
                            self.remove_phone(old_phone)
        else:
            raise ValueError('Phone does not anwer requirements.')
    def find_phone(self, phone):
        if isinstance(phone, Phone):
            phone = phone.value
        for i in self.phones:
            if i.value == phone:
                return i
        return None
    

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data.get(name)
    

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

john_record.edit_phone('1234567890', '0000000003')
print(john_record)

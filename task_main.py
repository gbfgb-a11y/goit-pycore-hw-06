from collections import UserDict

class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
def validator(func):
    def inner(nothing , something):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        valc = 0
        if len(something) == 10:
            for i in something:
                if i in numbers:
                    pass
                else:
                    valc+=1
            if valc == 0:
                return something
    return inner

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("Phone must be a string")
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")
        
        super().__init__(value)
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        if isinstance(phone, Phone):
            phone = phone.value
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if isinstance(phone, Phone):
            phone = phone.value
        existing = self.find_phone(phone)
        if existing:
            self.phones.remove(existing)
        else:
            raise ValueError("Phone does not exist.")

    def edit_phone(self, old_phone, new_phone):
        # Перевіряемо чи існує старий номер
        existing = self.find_phone(old_phone)
        if not existing:
            raise ValueError("Old phone number not found.")
        
        # Перевіряємо чи валідний новий номер
        try:
            validated_phone = Phone(new_phone)  # если невалидный — вызовет ValueError
        except ValueError as e:
            raise ValueError(f"Invalid new phone number: {e}")

        # Якщо обидві перевірки пройшли тоді ми міняємо номера.
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        if isinstance(phone, Phone):
            phone = phone.value
        for p in self.phones:
            if p.value == phone:
                return p
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

john_record.edit_phone('1234567890', '098765431')
print(Phone('123'))
print(john_record)


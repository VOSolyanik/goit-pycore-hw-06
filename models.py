from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value: str):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        
        if len(value) != 10:
            raise ValueError("Phone number must contain at least 10 digits")
        
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone: str) -> None:
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(f"Error: {e}")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]

    def find_phone(self, phone: str) -> Phone | None:
        for p in self.phones:
            if p.value == phone:
                return p

        return None

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    
    def delete(self, name: str) -> None:
        del self.data[name]
        
    def find(self, name: str) -> Record | None:
        if name in self.data:
            return self.data[name]
        
        return None
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
        """Add phone to record if it's valid, otherwise handle ValueError"""

        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(f"Error: {e}")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit phone in record if it exists"""

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def remove_phone(self, phone: str) -> None:
        """Remove phone from record if it exists"""

        self.phones = [p for p in self.phones if p.value != phone]

    def find_phone(self, phone: str) -> Phone | None:
        """Find phone in record by value, return None if not found"""

        for p in self.phones:
            if p.value == phone:
                return p

        return None

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        """Add record to address book"""

        self.data[record.name.value] = record
    
    def delete(self, name: str) -> None:
        """Delete record from address book by name"""

        del self.data[name]
        
    def find(self, name: str) -> Record | None:
        """Find record in address book by name, return None if not found"""
        
        if name in self.data:
            return self.data[name]
        
        return None
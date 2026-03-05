from colorama import Fore, Style
from address_book import Record, AddressBook

def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args

def print_done(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + message + Style.RESET_ALL)

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, TypeError, ValueError, KeyError) as e:
            print_error(str(e))
    return wrapper

@input_error
def add_contact(args, book):
    if len(args) < 2:
        raise ValueError("Provide name and phone number.")
    name, phone = args[0], args[1]
    record = book.find(name)
    if record:
        record.add_phone(phone)
        print_done("Phone added to existing contact.")
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        print_done("Contact added.")

@input_error
def change_contact(args, book):
    if len(args) < 3:
        raise ValueError("Provide name, old phone number, and new phone number.")
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found.")
    record.edit_phone(old_phone, new_phone)
    print_done("Contact updated.")

@input_error
def show_phone(args, book):
    if len(args) < 1:
        raise ValueError("Provide a name.")
    record = book.find(args[0])
    if not record:
        raise ValueError("Contact not found.")
    print_done(str(record))

@input_error
def remove_phone(args, book):
    if len(args) < 2:
        raise ValueError("Provide name and phone number.")
    name, phone = args[0], args[1]
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found.")
    record.remove_phone(phone)
    print_done("Phone removed.")

@input_error
def delete_contact(args, book):
    if len(args) < 1:
        raise ValueError("Provide a name.")
    book.delete(args[0])
    print_done("Contact deleted.")

@input_error
def add_birthday(args, book):
    if len(args) < 2:
        raise ValueError("Provide name and birthday (DD.MM.YYYY).")
    name, birthday = args[0], args[1]
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found.")
    record.add_birthday(birthday)
    print_done("Birthday added.")

@input_error
def show_birthday(args, book):
    if len(args) < 1:
        raise ValueError("Provide a name.")
    record = book.find(args[0])
    if not record:
        raise ValueError("Contact not found.")
    if not record.birthday:
        raise ValueError("Birthday not set.")
    print_done(f"{record.name.value}'s birthday: {record.birthday.value}")

@input_error
def birthdays(_args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        print_done("No birthdays in the next 7 days.")
        return
    for entry in upcoming:
        print_done(f"{entry['name']}: {entry['congratulation_date']}")

@input_error
def show_all_contacts(book):
    if not book.data:
        raise ValueError("No contacts found.")
    for record in book.data.values():
        print_done(str(record))

def add_test_data(book):
    users = [
        {"name": "John-Doe", "birthday": "15.02.1985", "phones": ["1234567890", "9876543210"]},
        {"name": "John-Smith", "birthday": "05.03.1990", "phones": ["1234567890", "9876543210"]},
        {"name": "John-Connor", "birthday": "10.03.1990", "phones": ["1234567890", "9876543210"]},
        {"name": "John-Wick", "birthday": "02.01.1990", "phones": ["1234567890", "9876543210"]}
    ]
    
    for user in users:
        record = Record(user["name"])
        for phone in user["phones"]:
            record.add_phone(phone)
        record.add_birthday(user["birthday"])
        book.add_record(record)
    

def main():
    book = AddressBook()
    add_test_data(book)
    print_done("Welcome to the assistant bot!")

    handlers = {
        "add": lambda args: add_contact(args, book),
        "change": lambda args: change_contact(args, book),
        "remove-phone": lambda args: remove_phone(args, book),
        "phone": lambda args: show_phone(args, book),
        "delete": lambda args: delete_contact(args, book),
        "all": lambda _: show_all_contacts(book),
        "add-birthday": lambda args: add_birthday(args, book),
        "show-birthday": lambda args: show_birthday(args, book),
        "birthdays": lambda args: birthdays(args, book),
        "hello": lambda _: print_done("How can I help you?"),
    }

    while True:
        command = input(Fore.BLUE + "Enter a command: " + Fore.RESET).strip()
        if not command:
            continue
        cmd, *args = parse_input(command)

        if cmd in ("close", "exit"):
            print_done("Good bye!")
            break
        elif cmd in handlers:
            handlers[cmd](args)
        else:
            print_error("Invalid command.")


if __name__ == "__main__":
    main()

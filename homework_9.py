phone_book = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid input format. Please enter name and phone number separated by a space"
        except IndexError:
            return "Invalid command. Please try again"
    return inner

@input_error
def handle_input(command):
    return command.lower()

def add_contact(name, phone):
    phone_book[name] = phone
    return f"Contact {name} has been added with phone number {phone}"

def change_contact(name, phone):
    phone_book[name] = phone
    return f"Phone number for {name} has been updated to {phone}"

def find_contact(name):
    return phone_book[name]

def show_all_contacts():
    output = ""
    for name, phone in phone_book.items():
        output += f"{name}: {phone}\n"
    return output

def main():
    print("Hello! This CLI phone book assistant.")
    while True:
        command = input("> ")
        command = handle_input(command)
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid input format. Please enter name and phone number separated by a space")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                print(change_contact(name, phone))
            except ValueError:
                print("Invalid input format. Please enter name and phone number separated by a space")
            except KeyError:
                print("Contact not found")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(find_contact(name))
            except KeyError:
                print("Contact not found")
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again")


if __name__ == "__main__":
    main()

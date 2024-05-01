class View:
    @staticmethod
    def display_contacts(contacts):
        if contacts:
            print("Contact list:")
            for contact in contacts:
                print(f"Username: {contact[0]}, Phone number: {contact[1]}")
        else:
            print("No contacts")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_error(error_message):
        print(f"Error: {error_message}")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def main_menu():
        print("\n1. Add contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. Show all contacts")
        print("5. Import contacts from CSV")

        return input("\nEnter your choice: ")

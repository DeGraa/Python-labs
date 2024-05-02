from model import Database
from view import View


class Controller:
    def __init__(self):
        self.model = Database()
        self.view = View()

    def add_contact(self):
        username = self.view.get_input("Enter name: ")
        phone_number = self.view.get_input("Enter phone number: ")
        try:
            self.model.insert_username(username, phone_number)
            self.view.display_message("Contact added successfully")
        except Exception as e:
            self.view.display_error(f"Error when adding a contact: {e}")

    def update_contact(self):
        phone_number = self.view.get_input("Enter phone number: ")
        new_username = self.view.get_input("Enter a new name: ")
        try:
            self.model.update_username(phone_number, new_username)
            self.view.display_message("The contact details were updated successfully")
        except Exception as e:
            self.view.display_error(f"Error when updating a contact: {e}")

    def delete_contact(self):
        phone_number = self.view.get_input("Enter the phone number to delete: ")
        try:
            self.model.delete_username(phone_number)
            self.view.display_message("Contact deleted successfully")
        except Exception as e:
            self.view.display_error(f"Error when deleting a contact: {e}")

    def show_all_contacts(self):
        try:
            contacts = self.model.get_all_contacts()
            self.view.display_contacts(contacts)
        except Exception as e:
            self.view.display_error(f"Error when displaying contacts: {e}")

    def import_contacts_from_csv(self):
        csv_file_path = self.view.get_input("Enter the path to the CSV file: ")
        try:
            self.model.import_contacts_from_csv(csv_file_path)
            self.view.display_message("Contacts imported successfully")
        except Exception as e:
            self.view.display_error(f"Error importing contacts: {e}")

    def search_contacts(self):
        pattern = self.view.get_input("Enter search pattern (name, phone number): ")
        try:
            results = self.model.search(pattern)
            if results:
                self.view.display_contacts(results)
            else:
                self.view.display_message(
                    "No contacts found matching the search criteria"
                )
        except Exception as e:
            self.view.display_error(f"Error when searching contacts: {e}")

    def import_contacts_from_list(self):
        user_input = self.view.get_input("Enter the list: ")
        try:
            contact_list = [tuple(item.split(",")) for item in user_input.split(";")]
            validated_contacts = [
                contact
                for contact in contact_list
                if len(contact) == 2
                and contact[1].isdigit()
                and len(contact[1]) in {11, 12}
            ]
            if validated_contacts:
                self.model.import_contacts_from_list(validated_contacts)
                self.view.display_message("Valid contacts imported successfully")
            if not validated_contacts:
                self.view.display_error("No valid contacts to import")
        except Exception as e:
            self.view.display_error(f"Error processing contacts: {e}")

    def show_some_contacts(self):
        limit = self.view.get_input("Enter the number of contacts: ")
        offset = self.view.get_input("Enter the entry index: ")
        try:
            contacts = self.model.get_some_contacts(limit, offset)
            self.view.display_contacts(contacts)
        except Exception as e:
            self.view.display_error(f"Error when displaying contacts: {e}")

    def run(self):
        while True:
            choice = self.view.main_menu()
            if choice == "1":
                self.add_contact()
                break
            elif choice == "2":
                self.update_contact()
                break
            elif choice == "3":
                self.delete_contact()
                break
            elif choice == "4":
                self.show_all_contacts()
                break
            elif choice == "5":
                self.import_contacts_from_csv()
                break
            elif choice == "6":
                self.search_contacts()
                break
            elif choice == "7":
                self.import_contacts_from_list()
                break
            elif choice == "8":
                self.show_some_contacts()
                break
            else:
                self.view.display_error("Invalid input, try again")
                break


if __name__ == "__main__":
    controller = Controller()
    controller.run()

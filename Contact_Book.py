# Contact Book

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("\nContact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {index}:")
                print(contact)

    def search_contact(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not found_contacts:
            print("\nNo contact found with the given search criteria.")
        else:
            for index, contact in enumerate(found_contacts, start=1):
                print(f"\nSearch Result {index}:")
                print(contact)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nContact found:")
                print(contact)
                contact.name = input("Enter new name (leave blank to keep current): ") or contact.name
                contact.phone = input("Enter new phone (leave blank to keep current): ") or contact.phone
                contact.email = input("Enter new email (leave blank to keep current): ") or contact.email
                contact.address = input("Enter new address (leave blank to keep current): ") or contact.address
                print("\nContact updated successfully.")
                return
        print("\nNo contact found with the given name.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("\nContact deleted successfully.")
                return
        print("\nNo contact found with the given name.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

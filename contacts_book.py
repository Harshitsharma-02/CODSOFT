contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts to display.\n")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\nContact Found:")
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'], "\n")
            found = True
    if not found:
        print("Contact not found.\n")


def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Leave blank to keep current value.")
            new_name = input(f"New Name ({contact['name']}): ") or contact['name']
            new_phone = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New Email ({contact['email']}): ") or contact['email']
            new_address = input(f"New Address ({contact['address']}): ") or contact['address']

            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")


def main():
    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        print()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

main()

def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ")
    email = input("Enter the contact email: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }

    contacts.append(contact)
    print("\nContact added successfully!\n")


def view_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def update_contact():
    name = input("Enter the contact name to update: ")
    contact_to_update = None
    for contact in contacts:
        if contact['name'] == name:
            contact_to_update = contact
            break

    if contact_to_update:
        print("\nUpdating contact...\n")
        phone = input("Enter the updated contact phone number: ")
        email = input("Enter the updated contact email: ")

        contact_to_update['phone'] = phone
        contact_to_update['email'] = email
        print("\nContact updated successfully!\n")
    else:
        print("\nNo contact found with that name.\n")


def delete_contact():
    name = input("Enter the contact name to delete: ")
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    print("\nContact deleted successfully!\n")


def search_contact():
    name = input("Enter the contact name to search: ")
    for contact in contacts:
        if contact['name'] == name:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            break
    else:
        print("\nNo contact found with that name.\n")


contacts = []

if __name__ == "__main__":
    while True:

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            break
        else:
            print("\nInvalid choice. Please try again.\n")
import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def add_contact(contacts):
    print("\n➕ Add New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully!")


def view_contacts(contacts):
    print("\n📒 Contact List")
    if not contacts:
        print("No contacts found.")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    keyword = input("\n🔍 Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print(f"\n📇 Found Contact:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("❌ No contact found with that information.")


def update_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("\n✏️ Enter the number of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave blank to keep existing value.")
            name = input(f"New Name ({contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"New Phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"New Email ({contacts[index]['email']}): ") or contacts[index]['email']
            address = input(f"New Address ({contacts[index]['address']}): ") or contacts[index]['address']

            contacts[index] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            print("✅ Contact updated successfully!")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("\n🗑️ Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"✅ Deleted contact: {deleted['name']}")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    contacts = load_contacts()
    while True:
        print("\n===== 📱 Contact Manager =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option (1–6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

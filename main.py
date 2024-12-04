from utils import load_contacts, save_contacts
from add_contact import add_contact
from view_contacts import view_contacts
from search_contact import search_contact
from update_contact import update_contact
from delete_contact import delete_contact

def main():
    """Main function to display the menu and handle user choices."""
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
            load_contacts()
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()

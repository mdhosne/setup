def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

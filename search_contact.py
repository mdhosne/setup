def search_contact(contacts):
    """Search for a contact."""
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact not found.")

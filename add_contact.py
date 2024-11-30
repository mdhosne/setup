def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address (optional): ").strip()
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully.")
def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave blank if you don't want to update a field.")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

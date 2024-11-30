import csv

CONTACTS_FILE = "contacts.csv"

def load_contacts():
    """Load contacts from the CSV file."""
    contacts = {}
    try:
        with open(CONTACTS_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts[row["name"]] = {"phone": row["phone"], "email": row["email"]}
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    """Save contacts to the CSV file."""
    with open(CONTACTS_FILE, mode="w", newline="") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for name, info in contacts.items():
            writer.writerow({"name": name, "phone": info["phone"], "email": info["email"]})

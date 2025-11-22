import json

def delete_email():
    file_path = "./data/emails.json"

    email_to_delete = input("Enter email to Delete : ")

    try:
        with open(file_path) as file:
            emails = json.load(file)
    except(FileNotFoundError):
        emails = []
    
    if email_to_delete in emails:
        emails.remove(email_to_delete)

        with open(file_path, "w") as file:
            json.dump(emails, file, indent=4)
        print(f"{email_to_delete} deleted successfully.")
    
    else: 
        print(f"{email_to_delete} not Found...")


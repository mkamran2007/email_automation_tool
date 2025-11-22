import json

def add_emails():
    file_path = "./data/emails.json"

    while True:
        print("-----------------------------------------------")
        print("----Please Enter Email or Press b or 0 to go Back ----")
        email = input("\nEnter your email : ")

        if email.lower() in ["b", "0", "back"]:
            print("returning to menu...")
            return
        
        if email.lower().endswith("@gmail.com"):
            try:
                with open(file_path) as file:
                    emails = json.load(file)
            except( FileNotFoundError, json.JSONDecodeError):
                emails = []
            
            emails.append(email.lower())

            with open(file_path, "w") as file:
                json.dump(emails, file, indent=4)
            
            print(f"\n{email} added successfully!")
    
        else:
            print("\nInvalid email! Only Gmail is allowed...")






import sys
sys.path.append("src")

from add_email import add_emails
from remove_email import delete_email
from write_email import write_email

def main():
    while True:
        print("\n#################################################################")
        print("######################## QuantumFrame Lab #######################")
        print("#################################################################\n")

        print("1- Add Email")
        print("2- Remove Email")
        print("3- Write Email")
        print("4- Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            add_emails()
        elif choice == "2":
            delete_email()
        elif choice == "3":
            write_email()
        elif choice == "4":
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()


# Functions


contacts = {}

def add_contact ():
    user_name = input("Enter your Name: \n")
    user_phone = input("Enter your Phone: \n")
    user_mail = input("Enter your Email: \n")

    contacts [user_name] = {
        "phone": user_phone,
        "email": user_mail
    }

def all_contacts ():
    if len(contacts) == 0:
        print("Contact Book is empty")
    print("=== All Contacts ===")
    for name, info in contacts.items():
        print("Name:" , name)
        print("Phone" , info ["phone"])


while True:
    print("===== Contact Book =====")
    print ("1. Add Contact\n 2. Search Contact \n 3. Delete Contact \n 4. View All Contact\n 5.Exit\n" )


    user_choice = int (input ("Enter your Choice please: \n"))
    if user_choice == 1:
        add_contact()
        print("Contact added Successfully!\n")

    elif user_choice == 5:
        print("Thanks for using the Contact Booking System")
        break
    else:
        ("Ivalid Choice!")
    
# Khali dictionary jahan saara data save hoga
contacts = {}

# 1. Contact Add karne ka function
def add_contact():
    user_name = input("Enter contact name: ")
    
    # Agar naam pehle se majood ho
    if user_name in contacts:
        print("Yeh naam pehle se majood hai!\n")
        return
        
    user_phone = input("Enter phone number: ")
    user_mail = input("Enter email address: ")
    
    # Nested dictionary mein data save ho raha hai
    contacts[user_name] = {
        "phone": user_phone,
        "email": user_mail
    }
    print("Contact successfully add ho gaya!\n")

# 2. Contact Search karne ka function
def search_contact():
    search_name = input("Dhoondne ke liye naam enter karein: ")
    
    if search_name in contacts:
        print("\n--- Details ---")
        print("Phone:", contacts[search_name]['phone'])
        print("Email:", contacts[search_name]['email'], "\n")
    else:
        print("Contact nahi mila!\n")

# 3. Contact Delete karne ka function
def delete_contact():
    delete_name = input("Delete karne ke liye naam enter karein: ")
    
    if delete_name in contacts:
        del contacts[delete_name]  # del se data delete hota hai
        print("Contact successfully delete ho gaya!\n")
    else:
        print("Yeh contact list mein nahi hai!\n")

# 4. Saare Contacts dekhne ka function
def view_all_contacts():
    if len(contacts) == 0:
        print("Contact book khali hai!\n")
        return
        
    print("\n===== SAARE CONTACTS =====")
    for name, info in contacts.items():
        print("Naam:", name)
        print("  Phone:", info['phone'])
        print("  Email:", info['email'])
        print("-------------------------")
    print()

# ===== MAIN PROGRAM MENU =====
while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")
    
    user_choice = int(input("\nEnter your choice (1-5): "))
    
    if user_choice == 1:
        add_contact()
    elif user_choice == 2:
        search_contact()
    elif user_choice == 3:
        delete_contact()
    elif user_choice == 4:
        view_all_contacts()
    elif user_choice == 5:
        print("Thanks for using the Contact Booking System. Allah Hafiz!")
        break
    else:
        print("Ghalat number! Meherbani kar ke 1 se 5 ke darmiyan choose karein.\n")

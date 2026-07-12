contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        contacts.append(contact)
        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found!")
        else:
            print("\n----- Contact List -----")
            for i in range(len(contacts)):
                print(i + 1)
                print("Name :", contacts[i]["Name"])
                print("Phone:", contacts[i]["Phone"])
                print()

    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False

        for contact in contacts:
            if search == contact["Name"] or search == contact["Phone"]:
                print("\nContact Found")
                print("Name    :", contact["Name"])
                print("Phone   :", contact["Phone"])
                print("Email   :", contact["Email"])
                print("Address :", contact["Address"])
                found = True

        if found == False:
            print("Contact Not Found!")

    elif choice == "4":
        phone = input("Enter Phone Number of Contact to Update: ")

        found = False

        for contact in contacts:
            if phone == contact["Phone"]:
                contact["Name"] = input("Enter New Name: ")
                contact["Phone"] = input("Enter New Phone: ")
                contact["Email"] = input("Enter New Email: ")
                contact["Address"] = input("Enter New Address: ")

                print("Contact Updated Successfully!")
                found = True

        if found == False:
            print("Contact Not Found!")

    elif choice == "5":
        phone = input("Enter Phone Number to Delete: ")

        found = False

        for contact in contacts:
            if phone == contact["Phone"]:
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break

        if found == False:
            print("Contact Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
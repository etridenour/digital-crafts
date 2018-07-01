# Phone Book App


answer = '1'
entry_count = 0
entry_list = {}

while answer != '5':
    print(" ")
    print("""Electronic Phone Book 
===================== 
1. Look up an entry 
2. Set an entry 
3. Delete an entry 
4. List all entries 
5. Quit""")
    answer = input("What do you want to do? (1-5): ")
    
    if answer == '1':
        if entry_count == 0:
            print("There are currently no entries.")
        elif entry_count > 0:
            name_input = input("Name: ")
            name_input = name_input.capitalize()
            entry_find = name_input in entry_list
            if entry_find == True:
                print("Found entry for " + name_input + ": " + str(entry_list[name_input]))
            else:
                print("Entry not found.")

    elif answer == '2':
        name_input = input("Name: ")
        number_input = str(input("Phone Number: "))
        name_input = name_input.capitalize()
        double_name_entry = name_input in entry_list
        double_number_entry = number_input in entry_list.values()
        double_name_number_entry = name_input in entry_list and number_input in entry_list.values()

        if double_name_number_entry == True:
            print("This name already exists.")
            print("Name: " + name_input)
            print("Number: " + str(number_input))
            double_name_entry = False
            double_number_entry = False
           
    
        elif double_name_entry == True:
            double_name_entry_input = input("This entry name already exists. Overwrite with new number? (y/n): ")
            if double_name_entry_input == "y":
                entry_list[name_input] = number_input
                
            else:
                print("No changes made.")

        else:
            entry_list[name_input] = number_input
            print("Entry stored for " + name_input)
            entry_count += 1

        

        

    elif answer == '3':
        if entry_count == 0:
            print("There are no entries to delete.")

        if entry_count > 0:
            name_input = input("Name: ")
            name_input = name_input.capitalize()
            if name_input not in entry_list:
                print("This entry does not exist.")
            else:
                del entry_list[name_input]
                print("Deleted entry for " + name_input)
                entry_count -= 1

    elif answer == '4':
        if entry_count == 0:
            print("There are no entries in the phone book.")
        elif entry_count > 0:
            print("Phone book entries:")
            entry_list_sorted = sorted(entry_list)
            for key in entry_list_sorted:
                print(key + ': ' + str(entry_list[key]))

    elif answer == '5':
        break
    
    else:
        print("Invalid entry.")

print("Bye")

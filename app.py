
contact_book=[]

def create_contact():
    name=input("please enter your name : ")
    phone=input("please enter your phone number : ")
    email=input("please enter your email address : ")
    
    contact={
        "name":name,
        "phone":phone,
        "email":email
    }
    
    contact_book.append(contact)
    
#create_contact()
    

def view_all_contact():
    for contact in contact_book:
        print(contact['name'],contact['phone'],contact['email'],sep='  | ')
            

#view_all_contact()

def search_contact():
    search_result=False
    name=input("enter your name for search : ")
    for contact in contact_book:
        if name.lower()  in contact['name'].lower():
            search_result=True
            print(f"Found : {contact['name']},  -  {contact['email']},  -{contact['phone']}")
    if not search_result:
        print("contact not found")
    

            
#search_contact()

def remove_contact():
    search_term=input("enter your text for remove : ")
    for index,contact in enumerate (contact_book):
        if search_term.lower() in contact['name']:
            print(f"Found,index no-{index+1},  {contact['name']} ,  {contact['phone']}, {contact['email']}")
    selected_index=int(input("enter an contact to remove : "))
    contact_book.pop(selected_index -1)
    
def update_contact():
    #1. select the contact
    search_term=input("enter your text for remove : ")
    for index,contact in enumerate (contact_book):
        if search_term.lower() in contact['name']:
            print(f"Found,index no-{index+1},  {contact['name']} ,  {contact['phone']}, {contact['email']}")
    selected_index=int(input("enter an contact index for update : "))
    #contact[selected_index-1]
    
    #2.get new values
    new_name=input("enter new name : ")
    new_phone=input("enter new phone : ")
    new_email=input("enter new phone : ")
    'l'
    #3.replace the old values with new values
    contact_book[selected_index -1].update(
        {
            "name":new_name,
            "email":new_email,
            "phone":new_phone
        }
    )
    print("contact update successfully")


def backup_contact():
    #1.take all the contact and write them to a file
    with open("contact.csv","wt") as file_pointer:
        for contact in contact_book:
            line=f"{contact['name']} , {contact['phone']}, {contact['email']}"
            file_pointer.write(line)
    print("Contacts Backed Up !")
    
def restore_contact():
    contact_book.clear()
    #1.open file 
    with open("contact.csv","r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted=line.strip().split(",")  
            # here strip() => use for remove space/slice(\n) 
            # split(",") for separate date using (,)
            contact={
                "name":line_splitted[0],
                "phone":line_splitted[1],
                "email":line_splitted[2],
            }
            print(contact)
            contact_book.append(contact)
    print("contact re-store successfully")
            
    #2.read all contact book 
    #3.save them to global contact book variable
        
        
    
            
    
print("welcome")

menu_text="""
Your Options: 
1.Create Contact
2.View All Contact 
3.Search All Contact 
4.Chose index number  And Remove Contact
5.Update Contact
6.Backup Contact
7.Restore Contact
0.Exit
"""

while True:
    print(menu_text)
    choice=input("Enter Your Choice: ")
    
    if choice=="1":
       create_contact() 
    elif choice=="2":
        view_all_contact()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        remove_contact()
    elif choice=='5':
        update_contact()
    elif choice=='6':
        backup_contact()
    elif choice=='7':
        restore_contact()
    elif choice=='0':
        break;
    else:
        print("Wrong Choice")


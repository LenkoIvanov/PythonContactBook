import csv
from datetime import date

class Contact: #class for basic contacts
    def __init__(self, name, number, birth, melody, mail):
        self.__name = name
        self.__number = number #personal number
        self.__birth = birth
        self.__melody = melody
        self.__mail = mail #personal email
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    def getNumber(self):
        return self.__number
    def setNumber(self,number):
        self.__number = number
    def getBirth(self):
        return self.__birth
    def setBirth(self,birth):
        self.__birth = birth
    def getMelody(self):
        return self.__melody
    def setMelody(self,melody):
        self.__melody = melody
    def getMail(self):
        return self.__mail
    def setMail(self,mail):
        self.__mail = mail
    def __str__(self):
        return "Name: " + self.__name + " Number: " + self.__number + " Email: " + self.__mail + " Birth: " + self.__birth

class Family(Contact): #class for family contacts
    def __init__(self, name, number, birth, melody, mail):
        super().__init__(name, number, birth, melody, mail)
        self.__member = '' #family member (ex. wife, mum, dad)
        self.__address = ''
    def setMember(self, role):
        self.__member = role
    def getMember(self):
        return self.__member
    def setAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def __str__(self):
        return super().__str__() + " Address: " + self.__address + " Member: " + self.__member

class Friend(Contact): #class for friend contacts
    def __init__(self, name, number, birth, melody, mail):
        super().__init__(name, number, birth, melody, mail)
        self.__address = ''
    def setAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def __str__(self):
        return super().__str__() + " Address: " + self.__address
    
class Work(Contact): #class for work contacts
    def __init__(self, name, number, birth, melody, mail):
        super().__init__(name, number, birth, melody, mail)
        self.__company = '' #company name
        self.__position = '' #job position (ex. software engineer, sysadmin)
    def setCompany(self,company):
        self.__company = company
    def getCompany(self):
        return self.__company
    def setJob(self, position):
        self.__position = position
    def getJob(self):
        return self.__position
    def __str__(self):
        return super().__str__() + " Company: " + self.__company + " Position: " + self.__position

def selectMelody():
    melodies = { 1: "Family melody",
                 2: "Friends melody",
                 3: "Work melody",
                 4: "Misc. melody"}
    print("The melodies are as follows: \n",
          "1 - Family \n",
          "2 - Friend \n",
          "3 - Work \n",
          "4 - Others")
    number = int(input("Enter a number between 1 or 4:"))
    chosenMelody = melodies.get(number)
    return chosenMelody

def createContactFamily(contactList):
    name = input("Enter name: ")
    number = input("Enter number: ")
    birth = input("Enter birthdate (DD/MM): ")
    if("/" not in birth):
        birth = input("Wrong input! Enter birthdate again (DD/MM): ")
    melody = selectMelody()
    mail = input("Enter email address: ")
    familyContact = Family(name,number,birth,melody,mail)
    familyRole = input("Family member: ")
    familyContact.setMember(familyRole)
    address = input("Home adress: ")
    familyContact.setAddress(address)
    contactList.append(familyContact)
    
def createContactFriend(contactList):
    name = input("Enter name: ")
    number = input("Enter number: ")
    birth = input("Enter birthdate (DD/MM): ")
    if("/" not in birth):
        birth = input("Wrong input! Enter birthdate again (DD/MM): ")
    melody = selectMelody()
    mail = input("Enter email address: ")
    friendContact = Friend(name, number, birth, melody, mail)
    address = input("Enter address: ")
    friendContact.setAddress(address)
    contactList.append(friendContact)
    
def createContactWork(contactList):
    name = input("Enter name: ")
    number = input("Enter number: ")
    birth = input("Enter birthdate (DD/MM): ")
    if("/" not in birth):
        birth = input("Wrong input! Enter birthdate again (DD/MM): ")
    melody = selectMelody()
    mail = input("Enter email address: ")
    workContact = Work(name, number, birth, melody, mail)
    company = input("Enter company name: ")
    workContact.setCompany(company)
    job = input("Enter position at company: ")
    workContact.setJob(job)
    contactList.append(workContact)
    
def createContactOther(contactList):
    name = input("Enter name: ")
    number = input("Enter number: ")
    birth = input("Enter birthdate (DD/MM): ")
    if("/" not in birth):
        birth = input("Wrong input! Enter birthdate again (DD/MM): ")
    melody = selectMelody()
    mail = input("Enter email address: ")
    contact = Contact(name, number, birth, melody, mail)
    contactList.append(contact)

def deleteContact(contactList):
    name = input("Enter name of the contact you wish to delete: ")
    if(not contactList):
        print("There are no contacts in this list!")
    else:
        for contact in contactList:
            currentName = contact.getName()
            if(currentName == name):
                contactList.remove(contact)
                print("Deletion successful!")
            else:
                print("There is no such contact!")
                
def printTxt(contactList, contactType):
    if(contactType == "family"):
        file = open("Family.txt", "w")
        for contact in contactList:
            text = contact.__str__()
            file.write(str(text) + "\n")
        file.close()
    elif(contactType == "friend"):
        file = open("Friends.txt", "w")
        for contact in contactList:
            text = contact.__str__()
            file.write(str(text) + "\n")
        file.close()
    elif(contactType == "work"):
        file = open("Work.txt", "w")
        for contact in contactList:
            text = contact.__str__()
            file.write(str(text) + "\n")
        file.close()
    elif(contactType == "other"):
        file = open("Others.txt", "w")
        for contact in contactList:
            text = contact.__str__()
            file.write(str(text) + "\n")
        file.close()

def remindBirthday(contactList):
    today = date.today()
    formatted = today.strftime("%d/%m")
    name = input("Enter name of contact: ")
    for contact in contactList:
        currentName = contact.getName()
        if(currentName == name):
            birthday = contact.getBirth()
            if(birthday == formatted):
                print(name + " has a birthday today!")
            else:
                print(name + " does not have a birthday today.")

def update_Family(familyList):
    name_to_update = input("Enter name of contact you wish to update: ")
    to_update = input("Which attribute do you wish to update? (name,number,birth,melody,mail,member or address):")
    for contact in familyList:
        currentName = contact.getName()
        if(currentName == name_to_update):
            if(to_update == "name"):
                newName = input("Enter new name: ")
                contact.setName(newName)
            elif(to_update == "number"):
                newNumber = input("Enter new number: ")
                contact.setNumber(newNumber)
            elif(to_update == "birth"):
                newBirth = input("Enter new birthday: ")
                contact.setBirth(newBirth)
            elif(to_update == "melody"):
                newMelody = selectMelody()
                contact.setMelody(newMelody)
            elif(to_update == "mail"):
                newMail = input("Enter new email: ")
                contact.setMail(newMail)
            elif(to_update == "member"):
                newMember = input("Enter new family member status: ")
                contact.setMember(newMember)
            elif(to_update == "address"):
                newAddress = input("Enter new address: ")
                contact.setAddress(newAddress)
            else:
                to_update = input("Wrong input! Enter again: ")

def update_Friend(friendList):
    name_to_update = input("Enter name of contact you wish to update: ")
    to_update = input("Which attribute do you wish to update? (name,number,birth,melody,mail or address):")
    for contact in friendList:
        currentName = contact.getName()
        if(currentName == name_to_update):
            if(to_update == "name"):
                newName = input("Enter new name: ")
                contact.setName(newName)
            elif(to_update == "number"):
                newNumber = input("Enter new number: ")
                contact.setNumber(newNumber)
            elif(to_update == "birth"):
                newBirth = input("Enter new birthday: ")
                contact.setBirth(newBirth)
            elif(to_update == "melody"):
                newMelody = selectMelody()
                contact.setMelody(newMelody)
            elif(to_update == "mail"):
                newMail = input("Enter new email: ")
                contact.setMail(newMail)
            elif(to_update == "address"):
                newAddress = input("Enter new address: ")
                contact.setAddress(newAddress)
            else:
                to_update = input("Wrong input! Enter again: ")
                
def update_Work(workList):
    name_to_update = input("Enter name of contact you wish to update: ")
    to_update = input("Which attribute do you wish to update? (name,number,birth,melody,mail,company or position):")
    for contact in workList:
        currentName = contact.getName()
        if(currentName == name_to_update):
            if(to_update == "name"):
                newName = input("Enter new name: ")
                contact.setName(newName)
            elif(to_update == "number"):
                newNumber = input("Enter new number: ")
                contact.setNumber(newNumber)
            elif(to_update == "birth"):
                newBirth = input("Enter new birthday: ")
                contact.setBirth(newBirth)
            elif(to_update == "melody"):
                newMelody = selectMelody()
                contact.setMelody(newMelody)
            elif(to_update == "mail"):
                newMail = input("Enter new email: ")
                contact.setMail(newMail)
            elif(to_update == "company"):
                newCompany = input("Enter new company: ")
                contact.setCompany(newCompany)
            elif(to_update == "position"):
                newPosition = input("Enter new position: ")
                contact.setJob(newPosition)
            else:
                to_update = input("Wrong input! Enter again: ")

def update_Other(otherList):
    name_to_update = input("Enter name of contact you wish to update: ")
    to_update = input("Which attribute do you wish to update? (name,number,birth,melody or mail):")
    for contact in otherList:
        currentName = contact.getName()
        if(currentName == name_to_update):
            if(to_update == "name"):
                newName = input("Enter new name: ")
                contact.setName(newName)
            elif(to_update == "number"):
                newNumber = input("Enter new number: ")
                contact.setNumber(newNumber)
            elif(to_update == "birth"):
                newBirth = input("Enter new birthday: ")
                contact.setBirth(newBirth)
            elif(to_update == "melody"):
                newMelody = selectMelody()
                contact.setMelody(newMelody)
            elif(to_update == "mail"):
                newMail = input("Enter new email: ")
                contact.setMail(newMail)
            else:
                to_update = input("Wrong input! Enter again: ")

def export_csv_family(familyList,familyDict):
    for contact in familyList:
        name = contact.getName()
        number = contact.getNumber()
        birth = contact.getBirth()
        melody = contact.getMelody()
        mail = contact.getMail()
        member = contact.getMember()
        address = contact.getAddress()
        familyDict["Name"] = name
        familyDict["Number"] = number
        familyDict["Birth"] = birth
        familyDict["Melody"] = melody
        familyDict["Mail"] = mail
        familyDict["Member"] = member
        familyDict["Address"] = address

    with open("Family.csv",mode="w") as family_file:
        fieldnames = ["Name", "Number", "Birth", "Melody", "Mail", "Member", "Address"]
        writer = csv.DictWriter(family_file, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerow(familyDict)
            
def import_csv_family(list_dicts): #works for only last rows
    family_file = open("Family.csv",mode="r")
    data = csv.DictReader(family_file)
    list_dicts = list(data)
    family_file.close()
    


           
def main():
    print("Enter a number to choose the action you wish to perform: \n",
          "1 - Add contact \n",
          "2 - Remove contact \n",
          "3 - Update contact \n",
          "4 - Set up a birthday reminder \n",
          "5 - Export contacts to a .txt file \n",
          "6 - Export contacts to a .csv file \n",
          "7 - Import contacts from a .csv file")
    number = int(input("Number: "))
    
    # lists to store object instances of contacts
    family = []
    friends = []
    work = []
    others = []

    #dictionaries for storing contact-specific information
    family_dict = {}
    friends_dict = {}
    work_dict = {}
    basic_dict = {}

    #list of dictionaries
    family_dict_list = []
    
    while True:
        if(number == 1): #create new contact
            contactType = input("What type of contact do you wish to add? (family, friend, work or other):")
            if(contactType == "family"):
                createContactFamily(family)  
            elif(contactType == "friend"):
                createContactFriend(friends)
            elif(contactType == "work"):
                createContactWork(work)
            elif(contactType == "other"):
                createContactOther(others)
            else:
                print("Wrong type!")
                
        elif(number == 2): #delete existing contact
            contactType = input("What type of contact do you wish to delete? (family, friend, work or other): ")
            if(contactType == "family"):
                deleteContact(family)
            elif(contactType == "friend"):
                deleteContact(friends)
            elif(contactType == "work"):
                deleteContact(work)
            elif(contactType == "other"):
                deleteContact(others)
            else:
                print("Wrong type!")
                
        elif(number == 3): #info update
            contactType = input("What type of contact do you wish to update? (family,friend,work or other): ")
            if(contactType == "family"):
                update_Family(family)
            elif(contactType == "friend"):
                update_Friend(friends)
            elif(contactType == "work"):
                update_Work(work)
            elif(contactType == "other"):
                update_Other(others)
            else:
                print("Wrong type!")
        
        elif(number == 4): #birthday reminders
            contactType = input("Which contacts do you wish to check for a birthday? (family, friend, work or other): ")
            if(contactType == "family"):
                remindBirthday(family)
            elif(contactType == "friend"):
                remindBirthday(friends)
            elif(contactType == "work"):
                remindBirthday(work)
            elif(contactType == "other"):
                remindBirthday(others)
                
        elif(number == 5): #print all contacts from list to .txt
            contactType = input("Which contacts do you wish to export to a .txt? (family, friend, work or other): ")
            if(contactType == "family"):
                printTxt(family, contactType)
            elif(contactType == "friend"):
                printTxt(friends, contactType)
            elif(contactType == "work"):
                printTxt(work, contactType)
            elif(contactType == "other"):
                printTxt(others, contactType)
            else:
                print("Wrong type!")
                
        elif(number == 6): #export to .csv file
            export_csv_family(family,family_dict)
        
        elif(number == 7): #import from .csv file
            import_csv_family(family_dict_list)
            for every_dict in family_dict_list :
                name = every_dict.get("Name")
                number = every_dict.get("Number")
                birth = every_dict.get("Birth")
                melody = every_dict.get("Melody")
                mail = every_dict.get("Mail")
                member = every_dict.get("Member")
                address = every_dict.get("Address")
                familyContact = Family(name,number,birth,melody,mail)
                familyContact.setMember(member)
                familyContact.setAddress(address)
                family.append(familyContact)
                
        else:
            print("Wrong input!")
        answer = input("Enter another action? (yes/no): ")
        if(answer == 'yes'):
            number = int(input("Number: "))
        elif(answer == 'no'):
            break
        else:
            print("Invalid answer!")
    
main()

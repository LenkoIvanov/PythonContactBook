import csv

class Contact: #class for basic contacts
    def __init__(self, name, number, birth, melody, mail):
        self.__name = name
        self.__number = number #personal number
        self.__birth = birth
        self.__melody = melody
        self.__mail = mail #personal email
    def getName(self):
        return self.__name

class Family(Contact): #class for family contacts
    def __init__(self, name, number, birth, melody, mail):
        super().__init__(name, number, birth, melody, mail)
        self.__member = '' #family member (ex. wife, mum, dad)
        self.__address = ''
    def setMember(self, role):
        self.__member = role
    def getMembet(self):
        return self.__member
    def setAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address

class Friend(Contact): #class for friend contacts
    def __init__(self, name, number, birth, melody, mail):
        super().__init__(name, number, birth, melody, mail)
        self.__address = ''
    def setAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address
    
class Work(Contact): #class for work contacts
    def __init__(self, name, birth, melody):
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

def selectMelody():
    melodies = { 1: "Family melody",
                 2: "Friends melody",
                 3: "Work melody",
                 4: "Misc. melody"}
    print("The melodies are as follows: \n",
          "1 - Family \n",
          "2 - Friend \n",
          "3 - Work \n",
          "4 - Others \n")
    number = int(input("Enter a number between 1 or 4:"))
    chosenMelody = melodies.get(number)
    return chosenMelody
            
def main():
    print("Enter a number to choose the action you wish to perform: \n",
          "1 - Add contact \n",
          "2 - Remove contact \n",
          "3 - Update contact \n",
          "4 - Set up a birthday reminder \n",
          "5 - Export contact to a .txt file \n",
          "6 - Export contact to a .csv file")
    number = int(input("Number: "))
    # dictionaries to store all types of contacts
    family = []
    friends = []
    work = []
    others = []
    while True:
        if(number == 1):
            contactType = input("What type of contact do you wish to add? (family, friend, work or other):")
            if(contactType == "family"):
                print("Enter the following: ")
                name = input("Enter name: ")
                number = input("Enter number: ")
                birth = input("Enter birthdate: ")
                melody = selectMelody()
                mail = input("Enter email address: ")
                familyContact = Family(name,number,birth,melody,mail)
                familyRole = input("Family member: ")
                familyContact.setMember(familyRole)
                address = input("Home adress: ")
                familyContact.setAddress(address)
                family.append(familyContact)
                
            elif(contactType == "friend"):
                print("Enter the following: ")
                name = input("Enter name: ")
                number = input("Enter number: ")
                birth = input("Enter birthdate: ")
                melody = selectMelody()
                mail = input("Enter email address: ")
                friendContact = Friend(name, number, birth, melody, mail)
                address = ("Enter address: ")
                friendContact.setAddress(address)
                
            elif(contactType == "work"):
                print("Enter the following: ")
                name = input("Enter name: ")
                number = input("Enter number: ")
                birth = input("Enter birthdate: ")
                melody = selectMelody()
                mail = input("Enter email address: ")
                workContact = Work(name, number, birth, melody, mail)
                company = input("Enter company name: ")
                workContact.setCompany(company)
                job = input("Enter position at company: ")
                workContact.setJob(job)
                work.append(workContact)
                
            elif(contactType == "other"):
                print("Enter the following: ")
                name = input("Enter name: ")
                number = input("Enter number: ")
                birth = input("Enter birthdate: ")
                melody = selectMelody()
                mail = input("Enter email address: ")
                contact = Contact(name, number, birth, melody, mail)
                other.append(contact)
            else:
                contactType = input("Wrong type! Enter again: ")
                
        elif(number == 2):
            contactType = input("What type of contact do you wish to delete?: ")
            if (contactType == "family"):
                name = input("Enter name of the contact you wish to delete: ")
                for contact in family:
                    currentName = contact.getName()
                    if(currentName == name):
                        del contact
            elif(contactType == "friend"):
                name = input("Enter name of the contact you wish to delete: ")
                for contact in friends:
                    currentName = contact.getName()
                    if(currentName == name):
                        del contact
            elif(contactType == "work"):
                name = input("Enter name of the contact you wish to delete: ")
                for contact in work:
                    currentName = contact.getName()
                    if(currentName == name):
                        del contact
            elif(contactType == "other"):
                name = input("Enter name of the contact you wish to delete: ")
                for contact in others:
                    currentName = contact.getName()
                    if(currentName == name):
                        del contact
            else:
                contactType = input("Wrong type! Enter again: ")
                
        elif(number == 3):
            pass
        elif(number == 4):
            pass
        elif(number == 5):
            pass
        elif(number == 6):
            pass
        else:
            print("Wrong input! Enter another action.")
        answer = input("Enter another action? (yes/no): ")
        if(answer == 'yes'):
            number = int(input("Number: "))
        elif(answer == 'no'):
            break
        else:
            print("Invalid answer!")
    
main()

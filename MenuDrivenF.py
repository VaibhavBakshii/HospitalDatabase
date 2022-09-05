def MenuDriven():
    print('[1] Create')
    print('[2] Update')
    print('[3] View')
    print('[4] Add')
    print('[5] Search')
def MenuUpdate():
    print('[7] Update Doctors Table')
    print('[8] Update Patients Table')
def ShowView():
    print('[9] View Patient')
    print('[10] View Doctor')
    print('[11] View Assignment')
    print('[12] View GenInfo')
    print('[13] View Assignedperdoc')
    print('[14] View RecoveryP')
    print('[15]  View Casualties')
def Search():
    print('[16] Search Doctor')
    print('[17] Search Patient')   
def Add():
    print('[18] Add Patient')
    print('[19] Add Doctor')

MenuDriven()
option = int(input('Enter The Option'))

while option !=0:
    if option == 1: 
        Create()
    elif option == 2: 
        print('Select what you want to update?')
    elif option == 3:
        print('select What you want to view?')
    elif option == 4:
        print('select what you want to Search?')
    elif option == 5:
        print('select what you want to update?')
    elif option == 6:
        print('What info?')
    elif option == 7:
        UpdateD()
    elif option == 8:
        UpdateP()
    elif option == 9:
        ViewP()
    elif option == 10:
        ViewD()
    elif option == 11:
        ViewAssignment()
    elif option == 12:
        ViewGenInfo()
    elif option == 13:
        ViewDoctorAssigned()
    elif option == 14:
        RecoveryP()
    elif option == 15:
        Casualties()
    elif option == 16:
        SearchD()
    elif option == 17:
        SearchP()
    elif option == 18:
        AddP()
    elif option == 19:
        AddD()
    else:
        print('Invalid Input')
    


    print()
    if option == 2:
        MenuUpdate()
        print()
        option = int(input('Enter The Option You Want To Be Updated'))
    print ()
    if option == 3:
        ShowView()
        print()
        option = int(input('Enter the Option You Want To View'))
    if option == 4 :
        Add()
        print()
        option = int(input('Enter The Option You Want To Add To'))
    if option == 5:
        Search()
        print()
        option = int(input('Enter The Option To Search'))
    
        
        
        
        
print('Program end Go Home')
    

        

        

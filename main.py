import pymysql
import pickle
import csv

db = pymysql.connect(host='localhost', user='root', password='zohaibninja')
Mycur = db.cursor()
Mycur.execute('Use Computer_Project')


# Adding a Patient's Record
def AddP():
    with open('GenInfo.dat', 'rb+') as F:
        R = pickle.load(F)
        Pno = input("Pno :")
        Name = input("Name :")
        Ailment = input("Ailment :")
        RoomNo = input("RoomNo.")
        Block = input("Block.")
        Ano = input('Ano.')
        DOJ = input("Date [YY-MM-DD]")
        SQL = "INSERT INTO Patient_Record VALUES (" + Pno + ",'" + Name + "','" + Ailment + "'," + RoomNo + ",'" + Block + "'," + Ano + ",'" + DOJ + "')"
        Mycur.execute(SQL)
        db.commit()
        for i in R:
            if i[0] == "No.ofPatients":
                i[1] += 1
        F.seek(0)
        pickle.dump(R, F)


# Adding a Doctor's Record
def AddD():
    with open('GenInfo.dat', 'rb+') as F:
        R = pickle.load(F)
        Dno = input("Dno :")
        Name = input("Name :")
        Specialisation = input("Specs :")
        Degree = input("Degree")
        FromInstitution = input("Inst")
        DOJ = input("Date [YY-MM-DD]")
        SQL = "INSERT INTO Doctor_Record VALUES (" + Dno + ",'" + Name + "','" + Specialisation + "','" + Degree + "','" + FromInstitution + "','" + DOJ + "')"
        Mycur.execute(SQL)
        db.commit()
        for i in R:
            if i[0] == "No.ofDoctors":
                i[1] += 1
        F.seek(0)
        pickle.dump(R, F)


# If Patient ends in a casualty
def CasualtyP():
    with open('GenInfo.dat', 'rb+') as F:
        R = pickle.load(F)
        A = input('Enter the Patient No.')
        SQL = "Delete from Patient_Record where Pno=" + A + ""
        Mycur.execute(SQL)
        db.commit()
        for i in R:
            if i[0] == "No.ofPatients":
                i[1] -= 1
            if i[0] == "Casualty":
                i[1] += 1
        F.seek(0)
        pickle.dump(R, F)


# If Patient recovers
def RecoveryP():
    with open('GenInfo.dat', 'rb+') as F:
        R = pickle.load(F)
        A = input('Enter the Patient No.')
        SQL = "Delete from Patient_Record where Pno=" + A + ""
        Mycur.execute(SQL)
        db.commit()
        for i in R:
            if i[0] == "No.ofPatients":
                i[1] -= 1
            if i[0] == "Recovery":
                i[1] += 1
        F.seek(0)
        pickle.dump(R, F)


# Removing a doctor
def RemoveD():
    with open('GenInfo.dat', 'rb+') as F:
        R = pickle.load(F)
        A = input('Enter the Doctor No.')
        SQL = "Delete from Doctor_Record where Dno=" + A + ""
        Mycur.execute(SQL)
        db.commit()
        for i in R:
            if i[0] == "No.ofDoctors":
                i[1] -= 1
        F.seek(0)
        pickle.dump(R, F)


def ViewPatient():
    SQL = "SELECT * FROM Patient_Record"
    Mycur.execute(SQL)
    R = Mycur.fetchall()
    for Pno, PName, Ailment, Roomno, Block_, Ano, DOJ in R:
        print("%5d | %20s | %10s | %5d | %2s | %5d |%s" % \
              (Pno, PName.ljust(20, "_"), Ailment.ljust(10, '_'), Roomno, Block_.ljust(2, '_'), Ano,
               DOJ.strftime("%Y-%m-%d")))


# Viewing Doctor_Record
def ViewDoctor():
    SQL = "SELECT * FROM Doctor_Record"
    Mycur.execute(SQL)
    R = Mycur.fetchall()
    for Dno, DName, Specialisation, Degree, FromInstitution, DOJ in R:
        print("%5d | %20s | %10s | %7s | %20s| %s" % \
              (Dno, DName.ljust(20, "_"), Specialisation.ljust(10, '_'), Degree.ljust(7, '_'),
               FromInstitution.ljust(2, '_'), DOJ.strftime("%Y-%m-%d")))


# Viewing Assignments
def ViewAssignment():
    SQL = "Select A.Ano,B.DName, A.Ailment as Assigned_For, A.Pno as Assigned_to, A.Pname as Pname from Patient_Record A, Doctor_Record B where A.Ano=B.Dno Order by A.Ano"
    Mycur.execute(SQL)
    R = Mycur.fetchall()
    for Ano, DName, Assigned_For, Assigned_to, Pname in R:
        print(" %20s | %10s | %5d | %20s" % \
              (DName.ljust(20, "_"), Assigned_For.ljust(10, '_'), Assigned_to, Pname.ljust(20, '_')))


# Viewing No. of Patient assigned per Doctor
def ViewPatientPerDoctor():
    SQL = "SELECT B.Dno, count(*) as PatientAssigned FROM Patient_Record A JOIN Doctor_Record B ON A.Ano = B.Dno GROUP BY B.Dno"
    Mycur.execute(SQL)
    R = Mycur.fetchall()
    for Dno, PatientAssigned in R:
        print("%5d | %3d" % \
              (Dno, PatientAssigned))


# To search a patient Record
def searchP():
    Pno = input('Enter The Patient Number')
    SQL = "Select * from Patient_Record where PNo=" + Pno + ""
    N = Mycur.execute(SQL)
    if N > 0:
        R = Mycur.fetchone()
        print('Patient Found')
        print('PatientNo. :', R[0])
        print('Name :', R[1])
        print('Ailment :', R[2])
        print('Room No. :', R[3])
        print('Block :', R[4])
        print('ANo. :', R[5])
        print('DOJ:', R[6])
    else:
        print(' Patient Record Not Found ')


# To search Doctor Record
def searchD():
    Dno = input('Enter The Doctor Number')
    SQL = "Select * from Doctor_Record where DNo=" + Dno + ""
    N = Mycur.execute(SQL)
    if N > 0:
        R = Mycur.fetchone()
        print('Doctor Found')
        print('DoctorNo. :', R[0])
        print('Name :', R[1])
        print('Specialisation :', R[2])
        print('Degree :', R[3])
        print('From Institution:', R[4])
        print('DOJ:', R[5])
    else:
        print(' Doctor Record Not Found ')


# To Modify Patient Record
def updateP():
    while True:
        Pno = input('Pno:')
        X = input('What to change')
        while True:
            if X not in ['Pno', 'PName', 'Ailment', 'Roomo', 'Block', 'Ano', 'DOJ']:
                X = input('Field does not exist. Enter Again')
            else:
                break
        Y = input('Change to')
        SQL = 'Update Patient_Record Set ' + X + "='" + Y + "' Where Pno=" + Pno + ""
        Mycur.execute(SQL)
        db.commit()
        cont = input("Update more?")
        if cont in ["n", "N"]:
            break


# To Modify Doctor Record
def updateD():
    while True:
        Dno = input('Dno:')
        X = input('What to change')
        while True:
            if X not in ['Dno', 'Name', 'Specialisation', 'Degree', 'From_Institution']:
                X = input('Field does not exist. Enter Again')
            else:
                break
        Y = input('Change to (enclose in Apsotrophe if string)')
        SQL = 'Update Doctor_Record Set ' + X + "=" + Y + " Where Pno=" + Dno + ""
        MyCur.execute(SQL)
        db.commit()
        cont = input('Update more?')
        if cont in ['n', 'N']:
            break
        # To create the GenInfo/ Reset GenInfo


def creategeninfo():
    with open("GenInfo.dat", "wb") as F:
        R = [['Name of Hospital', "PeeJay"], ['No.ofPatients', 5], ['No.ofDoctors', 5], ["Recovered", 0],
             ["Casualty", 0]]
        pickle.dump(R, F)


# To show the GenInfo
def showgeninfo():
    with open("GenInfo.dat", 'rb') as F:
        R = pickle.load(F)
        for i in R:
            print(i)


'''
JUST AN ADD ON
#To manage the AdminAccess Records
def create():
    with open ("Accounts.csv",'w') as F:
        LEL=csv.writer(F)
        R=[]
        while True:
            Username=input('Enter Username')
            Password=input('Enter Password')
            R.append([Username,Password])
            cont=input('Continue?')
            if cont in ['n','N']:
                break
        LEL.writerows(R)
def show():
    with open ("Accounts.csv",'r') as F:
        R=csv.reader(F)
        for i in R:
            print(i)
def add():
    with open ("Accounts.csv",'a') as F:
        LEL=csv.writer(F)
        R=[]
        while True:
            Username=input('Enter Username')
            Password=input('Enter Password')
            R.append([Username,Password])
            cont=input('Continue?')
            if cont in ['n','N']:
                break
        LEL.writerows(R)
def change():
    with open ("Accounts.csv",'r+') as F:
        R=csv.reader(F)
        a=[]
        c=input('Enter Username')
        for i in R:
            if i[0]==c:
                i[1]=input('Enter the new password')
            a.append(i)
        F.seek(0)
        potata=csv.writer(F)
        potata.writerows(a)
def getpassword(Username):
    with open ("Accounts.csv",'r') as F:
        R=csv.reader(F)
        for i in R:
            if i[0]==Username:
                return i[1]

#___________________________________________________________________________________________________________
ffs=input('Join as general?(Y/N)')
if ffs in ['n','N']:
    while True:
        User=input("Enter Username")
        Pass=input("Enter Password")
        if Pass==getpassword(User):
            AdminAccess="Y"
            break
        elif:
            ffs=input('Join as general?(Y/N)')
            if ffs in ['Y','y']:
                AdminAccess="N"
                break
else:
    AdminAcces="N"'''


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


def Delete():
    print('[14] RecoveryP')
    print('[15] Casualties')
    print('[16] RemoveD')


def Search():
    print('[17] Search Doctor')
    print('[18] Search Patient')


def Add():
    print('[19] Add Patient')
    print('[20] Add Doctor')


option = 1
while option != 0:
    MenuDriven()
    option = int(input('Enter The Option'))
    if option == 1:
        creategeninfo()
    elif option == 2:
        print('Select what you want to update?')
    elif option == 3:
        print('select What you want to view?')
    elif option == 4:
        print('select what you want to Search?')
    elif option == 5:
        print('select what you want to update?')
    elif option == 6:
        print('Select what you want to Remove?')
    else:
        print('Invalid Input')

    print()
    if option == 2:
        MenuUpdate()
        print()
        option = int(input('Enter The Option You Want To Be Updated'))
    print()
    if option == 3:
        ShowView()
        print()
        option = int(input('Enter the Option You Want To View'))
    if option == 4:
        Add()
        print()
        option = int(input('Enter The Option You Want To Add To'))
    if option == 5:
        Search()
        print()
        option = int(input('Enter The Option To Search'))
    if option == 6:
        Delete()
        print()
        option = int(input('Enter the Option to Remove'))

    if option == 7:
        updateD()
    elif option == 8:
        updateP()
    elif option == 9:
        ViewPatient()
    elif option == 10:
        ViewDoctor()
    elif option == 11:
        ViewAssignment()
    elif option == 12:
        showgeninfo()
    elif option == 13:
        ViewPatientPerDoctor()
    elif option == 14:
        RecoveryP()
    elif option == 15:
        CasualtyP()
    elif option == 16:
        RemoveD()
    elif option == 17:
        searchD()
    elif option == 18:
        searchP()
    elif option == 19:
        AddP()
    elif option == 20:
        AddD()
    print()
    print()
print('Program end Go Home')














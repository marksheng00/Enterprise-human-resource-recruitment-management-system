import sqlite3
import time
import data_structure
import os

class user:
    def __init__(self, name, password, address, email):
        self.name = name
        self.password = password
        self.address = address
        self.email = email

    def id_genertor(self):
        id_stack = data_structure.Stack()
        id_stack.push(str(int(time.time())))
        id_stack.push(self.name[0])
        id = id_stack.pop() + id_stack.pop()
        self.id = id
        print("YOU ID IS: "+self.id)

    def register(self):
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        print("<<Opened database successfully>>")

        c.execute("INSERT INTO USER (ID,NAME,PASSWORD,ADDRESS,EMAIL) \
                VALUES ('{}','{}','{}','{}','{}')".format(self.id,self.name,self.password,self.address,self.email))

        conn.commit()
        print("<<Records created successfully>>")
        print("Register is successfully")
        conn.close()

    def load_user_id_password(self):
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        print("Opened database successfully")

        cursor = c.execute("SELECT ID,NAME,PASSWORD,ADDRESS,EMAIL  from USER")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("PASSWORD = ", row[2])
            print("ADDRESS = ", row[3])
            print("EMAIL = ", row[4], "\n")

        print("Operation done successfully")
        conn.close()


class database:
    def create_user_db(self):
        conn = sqlite3.connect('user.db')
        print("<<Opened database successfully>>")
        c = conn.cursor()
        c.execute('''CREATE TABLE USER
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               PASSWORD       TEXT     NOT NULL,
               ADDRESS        TEXT,
               EMAIL          TEXT);''')
        print("<<Table created successfully>>")
        conn.commit()
        conn.close()


class applicant(user):
    def __init__(self):
        self.nric = input("please input your nric")
        self.postcode = input("please input your postcode")
        self.phone_no = input("please input your phone_no")
        self.mobile_no = input("please input your mobile_no")
        self.birthday = input("please input your birthday")
        self.gender = input("please input your gender")

    def create_applicant_db(self):
        conn = sqlite3.connect('user.db')
        print("<<Opened database successfully>>")
        c = conn.cursor()
        c.execute('''CREATE TABLE APPLICANT
                               (ID TEXT PRIMARY KEY     NOT NULL,
                               NRIC                    TEXT,
                               POSTCODE                TEXT,
                               PHONE_NO                TEXT,
                               MOBILE_NO               TEXT,
                               BIRTHDAY                TEXT,
                               GENDER                  TEXT);''')
        print("<<Table created successfully>>")
        conn.commit()
        conn.close()

    def applicant(self,u_id):
        try:
            conn = sqlite3.connect('USER.db')
            c = conn.cursor()
            print("<<Opened database successfully>>")
            c.execute("INSERT INTO APPLICANT (ID,NRIC,POSTCODE,PHONE_NO,MOBILE_NO,BIRTHDAY,GENDER) \
                                            VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(u_id,self.nric,self.postcode,self.phone_no,self.mobile_no,self.birthday,self.gender))
            conn.commit()
            print("<<Records created successfully>>")
            print("Collect applicant info Successfully")
            conn.close()
        except:
            print("This id has already been applied to relevant information once")

class application():

    def create_application_db(self):
        conn = sqlite3.connect('user.db')
        print("<<Opened database successfully>>")
        c = conn.cursor()
        c.execute('''CREATE TABLE APPLICATION
                       (ID INT PRIMARY KEY     NOT NULL,
                       APPLICATION_NUMBER          TEXT);''')
        print("<<Table created successfully>>")
        conn.commit()
        conn.close()


    def application_number_generator(self,id):
        try:
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            print("<<Opened database successfully>>")
            c = c.execute("SELECT APPLICATION_NUMBER  from APPLICATION")
            for row in c:
                pass
            print(row)
            application_number = int(row[0])+1
            conn.close()
        except:
            application_number = 1

        try:
            conn = sqlite3.connect('USER.db')
            c = conn.cursor()
            print("<<Opened database successfully>>")
            c.execute("INSERT INTO APPLICATION (ID,APPLICATION_NUMBER) \
                                    VALUES ('{}','{}')".format(id, application_number))
            conn.commit()
            print("id:{} application_number:{} are updated".format(id, application_number))
            print("<<Records created successfully>>")
            print("Apply Successfully")
            conn.close()
            return application_number
        except:
            conn = sqlite3.connect('USER.db')
            c = conn.cursor()
            print("<<Opened database successfully>>")
            c.execute("REPLACE INTO APPLICATION (ID,APPLICATION_NUMBER) \
                                                VALUES ('{}','{}')".format(id, application_number))
            conn.commit()
            print("id:{} application_number:{} are updated".format(id, application_number))
            print("<<Records created successfully>>")
            print("Apply Successfully")
            conn.close()
            return application_number
            print("Each id only allow to apply one application, A new application will be generated and the previous one will be overridden")

    def test_application(self):
        conn = sqlite3.connect('USER.db')
        c = conn.cursor()
        print("<<Opened database successfully>>")
        c.execute("INSERT INTO APPLICATION (ID,APPLICATION_NUMBER) \
                                       VALUES ('m1608193736','0001')")
        print("<<Records created successfully>>")
        print("Application is successfully")
        conn.close()

class apply():

    def create_apply_db(self):
        conn = sqlite3.connect('user.db')
        print("<<Opened database successfully>>")
        c = conn.cursor()
        c.execute('''CREATE TABLE APPLY
                               (APPLICATION_NUMBER PRIMARY KEY     NOT NULL,
                                POSITION_APPLIED         TEXT,
                                DATE_APPLIED             TEXT,
                                EXPECTED_SALARY          TEXT);''')
        print("<<Table created successfully>>")
        conn.commit()
        conn.close()

    def apply(self,application_number):
        position_applied = input("Please input your applied position")
        date_applied = input("Please input your applied date")
        expected_salary = input("Please input your expected salary")

        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        print("<<Opened database successfully>>")
        c.execute("INSERT INTO APPLY (APPLICATION_NUMBER,POSITION_APPLIED,DATE_APPLIED,EXPECTED_SALARY) \
                VALUES ('{}','{}','{}','{}')".format(application_number,position_applied,date_applied,expected_salary))
        conn.commit()
        print("<<Records created successfully>>")
        print("Apply position is successfully")
        conn.close()


class qualification():

    def create_qualification_db(self):
        conn = sqlite3.connect('user.db')
        print("<<Opened database successfully>>")
        c = conn.cursor()
        c.execute('''CREATE TABLE QUALIFICATION
                                       (APPLICATION_NUMBER      NOT NULL,
                                        QUALIFICATION        TEXT,
                                        INSTITUTION          TEXT,
                                        MAJOR_GRADE          TEXT,
                                        YEAR_GRADUATED       TEXT);''')
        print("<<Table created successfully>>")
        conn.commit()
        conn.close()

    def qualification(self,application_number):
        times = input("How many qualifications do you have?")
        for i in range(int(times)):
            qualification = input("please input your qualification")
            institution = input("please input your institution")
            major_grade = input("please input your major_grade")
            year_graduated = input("please input your year_graduated")

            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            print("<<Opened database successfully>>")
            c.execute("INSERT INTO QUALIFICATION (APPLICATION_NUMBER,QUALIFICATION,INSTITUTION,MAJOR_GRADE,YEAR_GRADUATED) \
                            VALUES ('{}','{}','{}','{}','{}')".format(application_number, qualification, institution,
                                                                major_grade, year_graduated))
            conn.commit()
            print("<<Records created successfully>>")
            print("Apply qualification is successfully")
            conn.close()


class working_experience():

    def create_working_experience_db(self):
        conn = sqlite3.connect('user.db')
        print("<<Opened database successfully>>")
        c = conn.cursor()
        c.execute('''CREATE TABLE WORKING_EXPERIENCE
                                               (APPLICATION_NUMBER      NOT NULL,
                                                COMPANY       TEXT,
                                                POSITION      TEXT,
                                                START_DATE    TEXT,
                                                END_DATE      TEXT,
                                                LEVEL         TEXT,
                                                MONTHLY_SALARY    TEXT);''')
        print("<<Table created successfully>>")
        conn.commit()
        conn.close()

    def working_experience(self,application_number):
        times = input("How many working experiences do you have?")
        for i in range(int(times)):
            company = input("please input your company")
            position = input("please input your position")
            start_date = input("please input your start_date")
            end_date = input("please input your end_date")
            level = input("please input your position level")
            monthly_salary = input("please input your monthly salary")

            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            print("<<Opened database successfully>>")
            c.execute("INSERT INTO WORKING_EXPERIENCE (APPLICATION_NUMBER,COMPANY,POSITION,START_DATE,END_DATE,LEVEL,MONTHLY_SALARY) \
                            VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(application_number, company, position,
                                                                start_date, end_date, level, monthly_salary))
            conn.commit()
            print("<<Records created successfully>>")
            print("Apply working experience is successfully")
            conn.close()


class reference():

    def create_reference_db(self):
        conn = sqlite3.connect('user.db')
        print("<<Opened database successfully>>")
        c = conn.cursor()
        c.execute('''CREATE TABLE REFERENCE
                                               (APPLICATION_NUMBER      NOT NULL,
                                                NAME       TEXT,
                                                DATE_RECEIVED      TEXT,
                                                HR_OFFICER     TEXT,
                                                OUTCOME        TEXT,
                                                REASON         TEXT,
                                                DATE    TEXT);''')
        print("<<Table created successfully>>")
        conn.commit()
        conn.close()

    def reference(self,application_number):
        for i in range(2):
            name = input("please input your reference's name")
            date_received = input("please input your reference's date received")
            hr_officer = input("please input your reference's hr officer")
            outcome = input("please input your reference's out come")
            reason = input("please input your reference's reason")
            date = input("please input your reference's date")

            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            print("<<Opened database successfully>>")
            c.execute("INSERT INTO REFERENCE (APPLICATION_NUMBER,NAME,DATE_RECEIVED,HR_OFFICER,OUTCOME,REASON,DATE) \
                            VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(application_number, name, date_received,
                                                                hr_officer, outcome, reason, date))
            conn.commit()
            print("<<Records created successfully>>")
            print("Apply reference is successfully")
            conn.close()


def user_register(register):
    if register == "register":
        name = input("Please input you name")
        password = input("Please input you password")
        address = input("Please input you address")
        email = input("Please input you email")
        return name, password, address, email


def login():
    u_id = input("Please input you id")
    u_password = input("Please input you password")
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    print("<<Opened database successfully>>")
    cursor = c.execute("SELECT ID,NAME,PASSWORD,ADDRESS,EMAIL  from USER")
    dict_login = {}
    for row in cursor:
        id = row[0]
        password = row[2]
        element = {id: password}
        dict_login.update(element)

    for i in dict_login:
        if str(i) == u_id:
            if u_password == dict_login[i]:
                print(u_password, dict_login[i])
                print("Login successfully")
            else:
                print("Login failed")

    print("<<Operation done successfully>>")
    conn.close()
    return u_id


def menu():
    command = input("Select the function\n 1:Register 2:Login 3:Apply application 4: Check status \nPlease input your choice")
    if command == "1":
        return "register"
    elif command == "2":
        return "login"
    elif command == "3":
        return "apply"
    elif command == "2":
        return "check"


if __name__ == "__main__":

# create user database
    if os.access("user.db", os.F_OK) == 0:
        db = database()
        db.create_user_db()
    else:
        print("File path is exist.")

for i in range(5):
# run menu
    command = menu()
    print(command)
# register
    if command == "register":
        name, password, address, email = user_register("register")
        user = user(name, password, address, email)
        user.id_genertor()
        user.register()
# login
    elif command == "login":
        u_id = login()

# apply
    if command == "apply":
        applicant = applicant()
        #applicant.create_applicant_db()
        applicant.applicant(u_id)

        application = application()
        #application.create_application_db()
        application_number = application.application_number_generator(u_id)

        apply =apply()
        #apply.create_apply_db()
        apply.apply(application_number)

        qualification = qualification()
        #qualification.create_qualification_db()
        qualification.qualification(application_number)

        working_experience = working_experience()
        #working_experience.create_working_experience_db()
        working_experience.working_experience(application_number)

        reference = reference()
        reference.create_reference_db()
        reference.reference(application_number)

        print("Apply the application successfully")


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()
print("<<Opened database successfully>>")

def query_application():
    print("---" * 10 + "APPLICATION" + "---" * 10)
    cursor = c.execute("SELECT ID,APPLICATION_NUMBER  from APPLICATION")
    for row in cursor:
        print(row)

def query_user():
    print("---" * 10 + "USER" + "---" * 10)
    cursor = c.execute("SELECT *  from USER")
    for row in cursor:
        print(row)

def del_db_table(db_name,db_table_name):
    conn = sqlite3.connect('{}.db'.format(db_name))
    c = conn.cursor()
    print("Opened database successfully")
    c.execute("DROP TABLE {};".format(db_table_name))
    conn.commit()
    conn.close()

def query_apply():
    print("---" * 10 + "APPLY" + "---" * 10)
    cursor = c.execute("SELECT *  from APPLY")
    for row in cursor:
        print(row)

def query_applicant():
    print("---"*10+"APPLICANT"+"---"*10)
    cursor = c.execute("SELECT *  from APPLICANT")
    for row in cursor:
        print(row)

def query_qualification():
    print("---" * 10 + "QUALIFICATION" + "---" * 10)
    cursor = c.execute("SELECT *  from QUALIFICATION")
    for row in cursor:
        print(row)

def query_working_experience():
    print("---" * 10 + "WORKING_EXPERIENCE" + "---" * 10)
    cursor = c.execute("SELECT *  from WORKING_EXPERIENCE")
    for row in cursor:
        print(row)

def query_reference():
    print("---" * 10 + "REFERENCE" + "---" * 10)
    cursor = c.execute("SELECT *  from REFERENCE")
    for row in cursor:
        print(row)


if __name__ == "__main__":
    query_user()
    query_applicant()
    query_application()
    #del_db_table("user","WORKING_EXPERIENCE")
    query_apply()
    query_qualification()
    query_working_experience()
    query_reference()

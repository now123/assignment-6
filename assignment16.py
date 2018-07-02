#Q.1- Create a database. Create the following tables:
#1. Book
#2. Titles
#3. Publishers
#4. Zipcodes
#5. AuthorsTitles
#6. Authors

import sqlite3
conn=sqlite3.connect('tanu,db')
print("job done")
#conn.execute('''CREATE TABLE BOOK1
#            (BOOK_ID INT PRIMARY KEY       NOT NULL,
#             LOCATION     CHAR(40)          NOT NULL,
#             GENRE        CHAR(20)         NOT NULL)''')
#print("table book created")

conn.execute('''CREATE TABLE TITLES
            (TITLE_ID INT     PRIMARY KEY       NOT NULL,
             TITLE            CHAR(40)          NOT NULL,
             ISBN             CHAR(20)          NOT NULL,
             PUBLISHER_ID     INT               NOT NULL,
             PUBLICATION YEAR INT               NOT NULL )''')
print("table TITLE created")

conn.execute('''CREATE TABLE PUBLISHERS
            (PUBLISHERS_ID INT     PRIMARY KEY       NOT NULL,
             NAME                  CHAR(40)          NOT NULL,
             STREET_ADDRESS        CHAR(20)          NOT NULL,
             SUITE_NO              INT               NOT NULL,
             ZIP_CODE_ID           INT               NOT NULL )''')
print("table PUBLISHER created")

conn.execute('''CREATE TABLE ZIP_CODES
            (ZIP_CODE_ID INT     PRIMARY KEY       NOT NULL,
             CITY                CHAR(40)          NOT NULL,
             STATE               CHAR(20)          NOT NULL,
             ZIP_CODE            INT               NOT NULL)''')
print("table ZIP_CODE created")


conn.execute('''CREATE TABLE AUTHOR_TITLES
            (AUTHOR_TITLE_ID INT     PRIMARY KEY       NOT NULL,
             AUTHOR ID               INT               NOT NULL,
             TITLE_ID                 INT         NOT NULL )''')
print("table AUTHOR TITLES created")


conn.execute('''CREATE  TABLE AUTHOR 
            (AUTHOR_ID INT     PRIMARY KEY       NOT NULL,
             FIRST NAME             CHAR(40)               NOT NULL,
             MIDDLE NAME            CHAR(20)               NOT NULL
             LAST NAME              CHAR(40)               NOT NULL)''')
print("table AUTHOR  created")

#Q.2- Insert values in the tables.

conn.execute("INSERT INTO AUTHOR(AUTHOR_ID,FIRST_NAME, MIDDLE_NAME,LAST_NAME) VALUES(1,'efdsf','ded','rf')")
conn.execute("INSERT INTO AUTHOR(AUTHOR_ID,FIRST_NAME, MIDDLE_NAME,LAST_NAME) VALUES(2,'sham','fdc','ddff')")
conn.commit()
print("record created")


#Q.3- Update any values in any of the tables. Print the original and updated values.
cursor=conn.execute("SELECT AUTHORs_ID,FIRST_NAME, MIDDLE_NAME,LAST_NAME from AUTHOR")
for row in cursor:
    print("AUTHOR_ID=",row[0])
    print("FIRST_NAME=", row[1])
    print("MIDDLE_NAME=", row[2])
    print("LAST_NAME=",row[3]),"\n"
print ("operation done")


conn.execute("UPDATE AUTHOR set FIRST_NAME= 'Naruto' where AUTHORs_ID=2")
conn.commit()
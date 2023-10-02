import sqlite3 as s

con=s.connect("ContactManagementSystem0.db")

c=con.cursor()

###  Create Table contact_tbl

def create_tbl(tblq):
    c.execute(tblq)
    con.commit()
tblq='''create table if not exists contact_tbl
               (
                      fname text,
                      lname text,
                      contactno int,
                      email text,
                      city text
               )'''

### Create Trigger To Validate Input On The Contact Table

def validate_inputdata():
    tq='''
               create trigger if not exists validate_phoneno
               before insert on contact_tbl
               BEGIN
                   SELECT
                       CASE
                           WHEN LENGTH(NEW.contactno) != 10 THEN
                               RAISE(ABORT, 'Invalid Phone Number,Phone Number Should Be 10 Digits')
                      
                           WHEN NEW.email NOT LIKE '%_@___%.__%' THEN 
                                RAISE(ABORT,'Invalid Email Id , Email Id Should Be In Proper Format')
                        END;
                END;
            '''
    c.execute(tq)

### Function For Creating<u> Log Table For Insert Trigger</u>

def logtbl_for_insert(inslogq):
    c.execute(inslogq)
    con.commit()
inslogq='''create table if not exists insertlog_tbl
                (
                        fname text,
                        lname text,
                        contactno int,
                        datetime text,
                        operation_name text
                )'''

### Function For Creating Insert Trigger


def ins_trigger(t2q):
    c.execute(t2q)
    con.commit()
t2q='''create trigger if not exists insert_trigger
      after insert on contact_tbl
      begin
          insert into insertlog_tbl
          values(NEW.fname,NEW.lname,NEW.contactno,datetime('now','localtime'),'INSERT');
      end;'''

### Function For Creating Log Table For Delete Trigger

def logtbl_for_delete(dellogq):
    c.execute(dellogq)
    con.commit()
dellogq='''create table if not exists deletelog_tbl
                (
                        fname text,
                        lname text,
                        contactno int,
                        datetime text,
                        operation_name text
                )'''

### Function For Creating Delete Trigger

def del_trigger(t3q):
    c.execute(t3q)
    con.commit()
t3q='''create trigger if not exists del_trigger
       after delete on contact_tbl
       begin
           insert into deletelog_tbl 
           values(OLD.fname,OLD.lname,OLD.contactno,datetime('now','localtime'),'DELETE');
       end;'''

### Function For Creating Log Table For Update Trigger

def logtbl_for_update(uplogq):
    c.execute(uplogq)
    con.commit()
uplogq='''create table if not exists updatelog_tbl
           (
                        fname text,
                        lname text,
                        contactno int,
                        newcontactno int,
                        datetime text,
                        operation_name text
            )'''

### Function For Creating Update Trigger

def update_trigger(t4q):
    c.execute(t4q)
    con.commit()
t4q='''create trigger if not exists update_trigger
       after update on contact_tbl
       begin
           insert into updatelog_tbl
           values(OLD.fname,OLD.lname,OLD.contactno,NEW.contactno,datetime('now','localtime'),'UPDATE');
       end;'''

#Insert Records In Contact table
def insert_record():
    c.execute('''insert into contact_tbl values('Jay','Patel',9867890543,'jay@gmail.com','Mumbai'),
                                               ('Shree','Rajput',9812390543,'shree@gmail.com','Delhi'),
                                               ('Ram','Rajput',9867890999,'ram@gmail.com','Delhi'),
                                               ('Shiv','Vyas',9998909992,'shiv@gmail.com','Surat'),
                                               ('Ganesha','Patel',9866660543,'ganesha@gmail.com','Surat')''')


#Update Records In Contaact table
def update_record():
    upq=""" update contact_tbl
            set contactno=6353459898
            where fname='Shiv' and lname='Vyas';
        """
    c.execute(upq)

#Delete Record From Contact Table
def delete_record():
    delq="""
             delete from contact_tbl
             where fname='Shree' and lname='Rajput';
         """
    c.execute(delq)

### Function For Print All Records Of Contact Table And All Log Table.

def printrecords_of_maintbl():
    print("\n\n\t\t Records In Main Contact Table \n---------------------------------------------------------------------------")  
    q="select * from contact_tbl;"
    c.execute(q)
    records=c.fetchall()
     # For Printing headers
    header = "{:^12} {:^12} {:^12} {:^25} {:^12}".format('First Name', 'Last Name', 'Contact No', 'email','city')
    print(header,"\n---------------------------------------------------------------------------")

    # For Printing records
    for re in records:
            record_line = "{:^12} {:^12} {:^12} {:^25} {:^12}".format(re[0], re[1], re[2], re[3], re[4])
            print(record_line)

def records_of_inslog_tbl():
    print("\n\n\t\t Insert Log Table Details \n-------------------------------------------------------------------------------------------")  
    q1="select * from insertlog_tbl;"
    c.execute(q1)
    records1=c.fetchall()
    # For Printing headers
    header = "{:^12} {:^12} {:^12} {:^25} {:^25}".format('First Name', 'Last Name', 'Contact No', 'Date-Time','Operation Name')
    print(header,"\n-------------------------------------------------------------------------------------------")

    # For Printing records
    for re in records1:
            record_line1 = "{:^12} {:^12} {:^12} {:^25} {:^25}".format(re[0], re[1], re[2], re[3], re[4])
            print(record_line1)

def records_of_dellog_tbl():
    print("\n\n\t\t Delete Log Table Details \n-----------------------------------------------------------------------------------------")  
    q2="select * from deletelog_tbl;"
    c.execute(q2)
    records=c.fetchall()
     # For Printing headers
    header = "{:^12} {:^12} {:^12} {:^25} {:^25}".format('First Name', 'Last Name', 'Contact No', 'Date-Time','Operation Name')
    print(header,"\n-----------------------------------------------------------------------------------------")

    # For Printing records
    for re in records:
            record_line = "{:^12} {:^12} {:^12} {:^25} {:^25}".format(re[0], re[1], re[2], re[3], re[4])
            print(record_line)

def records_of_uplog_tbl():
    print("\n\n\t\t Update Log Table Details \n------------------------------------------------------------------------------------------------------")  
    q3="select * from updatelog_tbl ;"
    c.execute(q3)
    records=c.fetchall()
     # For Printing headers
    header = "{:^12} {:^12} {:^12} {:^25} {:^12} {:^25}".format('First Name', 'Last Name', 'Old Contact No', 'New Contact No','Date-Time','Operation Name')
    print(header,"\n------------------------------------------------------------------------------------------------------")

    # For Printing records
    for re in records:
            record_line = "{:^12} {:^12} {:^12} {:^25} {:^12} {:^25}".format(re[0], re[1], re[2], re[3], re[4], re[5])
            print(record_line)

def mainfunc():
    create_tbl(tblq)
    validate_inputdata()
    logtbl_for_insert(inslogq)
    ins_trigger(t2q)
    logtbl_for_delete(dellogq)
    del_trigger(t3q)
    logtbl_for_update(uplogq)
    update_trigger(t4q)
    insert_record()
    update_record()
    delete_record()
    printrecords_of_maintbl()
    records_of_inslog_tbl()
    records_of_dellog_tbl()
    records_of_uplog_tbl()
mainfunc()








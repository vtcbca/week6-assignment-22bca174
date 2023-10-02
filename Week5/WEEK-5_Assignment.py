#Insert Records Directly And Take Input From User Into CSV File.

def insert_records(attribute,records):#,list_of_records):
    pass

attribute=['StudentId','StudentName','City','Contact_Number']

#Insert 5 records Directly
records=[[11,'Jay Patel','Surat',9510500989],
        [12,'Shree Rajput','Mumbai',9511100989],
        [14,'Om Vyas','Surat',9911500989],
        [13,'Krishna Prajapati','Delhi',9510522989],
        [15,'Shiv Pandya','Surat',9712530989]]

# Insert 5 records By User
list_of_records=[]
for i in range(5):
        no=int(input(" Enter ID Of Student : "))
        name=input(" Enter Name Of Student : ")
        city=input(" Enter City Of Student : ")
        phoneno=int(input(" Enter Contact Number Of Student : "))
        li=[no,name,city,phoneno]
        list_of_records.append(li)

# Write Above Records Into student.csv File.

def write_on_csvfile():
    import csv as c
    with open('D:\PythonPractice\student.csv','w',newline='') as csvobj:
        whole_file=c.writer(csvobj)
        whole_file.writerow(attribute)
        whole_file.writerows(records)
        #whole_file.writerows(list_of_records)


# Read Student.csv File And Print It.

def read_csvfile():
    import csv
    
    with open('D:\PythonPractice\student.csv', 'r') as obj:
        allrecords_of_file = csv.DictReader(obj)
        
        # For Printing header
        header = "{:^12} {:^20} {:^15} {:^15}".format('StudentId', 'StudentName', 'City', 'Contact_Number')
        print(header,"\n")
        
              
        # For Printing records
        for records in allrecords_of_file:
            record_line = "{:^12} {:^20} {:^15} {:^15}".format(records['StudentId'], records['StudentName'], records['City'], records['Contact_Number'])
            print(record_line)


#Function Call

insert_records(attribute, records)#,list_of_records)
write_on_csvfile()
print("\n\n")
print("\n\t\t  Records In CSV File Are As Below\n\t\t------------------------------------\n\n")
read_csvfile()


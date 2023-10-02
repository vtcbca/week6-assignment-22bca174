### 1. Create a result table which contain student id, student name and 5 subject marks. 

### 2. Enter 10 studnet details with its marks.


import sqlite3

con=sqlite3.connect('D://PythonPractice//result_database2.db')

cur=con.cursor()

create_tbl='''create table if not exists result_tbl
              (
                  Student_id int Primary key,
                  Student_name text NOT NULL,
                  subject1_marks int,
                  subject2_marks int,
                  subject3_marks int,
                  subject4_marks int,
                  subject5_marks int)'''

cur.execute(create_tbl)

insert_record='''insert into result_tbl values(1,'Jay Sharma',67,78,77,88,56),
                                              (2,'Shree Patel',75,77,65,87,66),
                                              (3,'Ram Sharma',67,78,77,88,56),
                                              (4,'Ram Patel',49,35,45,58,60),
                                              (5,'Shiv Desai',55,40,67,68,56),
                                              (6,'Shivu Patel',92,93,96,88,85),
                                              (7,'Krishna Prajapati',29,35,43,40,51),
                                              (8,'Krish Patel',70,65,55,62,56),
                                              (9,'Radhika Sharma',87,85,77,70,88),
                                              (10,'Radha Desai',89,98,87,88,86)'''

cur.execute(insert_record)

records='select * from result_tbl'
cur.execute(records)
data=cur.fetchall()

import csv

with open('D://PythonPractice//result.csv', 'w+', newline='') as file:
    fileobj = csv.writer(file)
    head = ['Student_ID', 'Student_Name', 'Subject1_Marks', 'Subject2_Marks', 'Subject3_Marks', 'Subject4_Marks', 'Subject5_Marks']
    fileobj.writerow(head)
    fileobj.writerows(data)

### 4. Read result.csv file and Print Total Marks and Grade of each student. Also Append Total Marks and Grade column into result.csv file.

with open('D://PythonPractice//result1.csv', 'r', newline='') as file, open('D://PythonPractice//mainresult2.csv', 'w+', newline='') as file2:
    allre=csv.reader(file)
    fileobj=csv.writer(file2)
    head=next(allre)
    head.extend(['Total_Marks','Percentage','Grade'])
    fileobj.writerow(head)
    for i in allre:
        totalmarks=int(i[2])+int(i[3])+int(i[4])+int(i[5])+int(i[6])
        i.append(totalmarks)
        percentage=i[7]/500*100
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >=55 and percentage < 70:
            grade = 'C'
        elif percentage >=30 and percentage < 55 :
            grade = 'D'
        else:
            grade = 'Fail'
        i.extend([percentage,grade])
        fileobj.writerow(i)
    file2.seek(0)
    header = "{:^12} {:^15} {:^15} {:^15} {:^15} {:^15} {:^15} {:^15} {:^20} {:^15}".format('Student_ID', 'Student_Name', 'Subject1_Marks', 'Subject2_Marks', 'Subject3_Marks', 'Subject4_Marks', 'Subject5_Marks','Total_Marks','Percentage','Grade')
    print(header, "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    allrecords = file2.readlines()[1:]
    
    for record in allrecords: 
        record = record.strip().split(',') 
        record_line = "{:^12} {:^20} {:^15} {:^15} {:^15} {:^15} {:^15} {:^15} {:^20} {:^15}".format(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7],record[8],record[9])
        print(record_line)

   
        
    

'''#5. List out Top 3 Student id and name with its percentage. (1st method)

with open('D://PythonPractice//mainresult2.csv', 'r', newline='') as file2:
    head = next(file2)
    header = "{:^12} {:^20} {:^15}\n-----------------------------------------------------".format('Student_ID', 'Student_Name', 'Percentage')
    print(header)
    d = csv.reader(file2)
    d = sorted(d, key=lambda stud: stud[8], reverse=True)
    c=0
    # Iterate through the sorted data and print each record
    for i in d:
        record_line = "{:^12} {:^20} {:^15} ".format(i[0], i[1], i[8])
        print(record_line)
        c+=1
        if c==3:
            break'''




'''#5. List out Top 3 Student id and name with its percentage. (2nd method)

with open('D://PythonPractice//mainresult2.csv', 'r', newline='') as file:
    allre =csv.reader(file)  # Read the CSV data into a list
    head = next(allre)  # Get the header
    allre=list(allre)
    # Use a loop to find the top 3 records based on the 'Percentage' column
    top_3_records = []
    for _ in range(3):
        if allre:  # Check if there are records in the list
            max_record = max(allre, key=lambda stud: float(stud[8]))  # Find the maximum by 'Percentage'
            print(max_record)
            top_3_records.append(max_record)
            allre.remove(max_record)'''

 #print(top_3_records)

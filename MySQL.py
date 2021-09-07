import mysql.connector
from datetime import datetime


user = 'root'
password = 'kali'
host_name='localhost'
database_name='MyDb'

try:
    conn = mysql.connector.connect(
        user=user,
        passwd=password,
        host=host_name,
        database=database_name
    )
    cursor = conn.cursor()
    print("Connection Made With The Database!")
except mysql.connector.Error as e:
    print(f"Error: {e}")

def create_database():
    cursor.execute("CREATE DATABASE MyDb")
    print("Database Created!")

def delete_database_Table(Table_name):
    cursor.execute(f"DROP TABLE {Table_name}")  
    print("Table Deleted!")


def delete_data_from_Table(Table_name):
    cursor.execute(f"DELETE FROM {Table_name}")
    print("Data deleted from the Table Created!")

def create_table():
    cursor.execute("CREATE TABLE Student_Table (StudentID int PRIMARY KEY AUTO_INCREMENT not NULL, Name varchar(50) not NULL, Class smallint UNSIGNED not NULL, Gender ENUM('Male', 'Female'), Date_Created datetime)")
    print("Table Created!")
def main():
    while True:
        now = datetime.now()
        created_time = now.strftime('%Y-%m-%d %H:%M:%S')
        try:
            first_name_of_the_Student = input("First Name of the Student: ").title()
            last_name_of_the_Student = input("Last Name of the Student: ").title()
            full_name = f"{first_name_of_the_Student} {last_name_of_the_Student}"
            class_of_the_Student = int(input("Class: "))
            gender_of_the_Student = input("Male or Female: ").title()
            print(gender_of_the_Student)
            if class_of_the_Student  > 12:
                print("Table Accepts Classes Upto 12th Only!")
            elif len(first_name_of_the_Student) + len(last_name_of_the_Student) < 2 or len(first_name_of_the_Student) + len(last_name_of_the_Student) > 50:
                print("Name is Invalid!")
            elif gender_of_the_Student not in ['Male', 'Female']:
                print("Invalid Gender!")
            else:
                print(f"->> Name: {full_name}, Class: {class_of_the_Student}, Gender: {gender_of_the_Student}, Date Created: {created_time}")


                cursor.execute("INSERT INTO Student_Table(Name, Class, Gender, Date_Created) VALUES(%s, %s, %s, %s)", (full_name, class_of_the_Student, gender_of_the_Student, created_time))
                conn.commit()
                print("Added To The Table!")
        except KeyboardInterrupt:
            break
    
def data_from_the_table(Table_name):
    cursor.execute(f"SELECT * FROM {Table_name}")
    print("\n__________")
    for i in cursor:
        print(i)
    print("__________")

# create_database()
# delete_database_Table('Student_Table')
# create_table()
# delete_data_from_Table('Student_Table')
# main()
# data_from_the_table('Student_Table')


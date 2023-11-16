
import json
import io as _io

FILE_NAME: str = 'enrollments.json'

MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
menu_choice: str = ''
student: dict = {}
students: list = []
file_data: str = ''
file = _io.TextIOWrapper


try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()



while True:

    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()

    if menu_choice == "1":

        print("-"*50)
        for student in students:
            if float(student["GPA"]) >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif float(student["GPA"]) >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif float(student["GPA"]) >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif float(student["GPA"]) >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["FirstName"], student["LastName"], float(student["GPA"])))
        print("-"*50)
        continue

    elif menu_choice == "2":
        try:

            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try:
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "GPA": float(student_gpa)}
            students.append(student)
        except ValueError as e:
            print(e)
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        continue

    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)
            file.close()
            print(json.dumps(students, indent=4))
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    elif menu_choice == "4":
        break
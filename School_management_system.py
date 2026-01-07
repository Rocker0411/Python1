class Student:
    fees = 10000
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a student."
    

def total_students():
    try:
        with open("Student_list.txt") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0
    

def save_students_list():
    while True:
        try:
            num_students = int(input("How many students have been taken : "))

            if (num_students > 10):
                print("Please enter a number that is less than 10.")

            else:
                break

        except ValueError:
            print("Please enter a NUMBER.")

    start_num = total_students()

    with open("Student_list.txt","a")as f:
        for i in range(num_students):
            name = input("Enter Student name: ")

            while True:
                try:
                    class_student = int(input("Enter student's class : "))
                    Age = int(input("Enter student's age : "))
                    Roll = int(input("Enter his roll number : "))
                    Address = input("Enter student's address : ")
                    Address = Address.title()
                    if not (1 <= class_student <= 12):
                        print("Invalid class")
                        continue

                    if not (5 <= Age <= 18):
                        print("Invalid age")
                        continue

                    if not (0 < Roll <= 100):
                        print("Invalid roll")
                        continue

                    break
    
                except ValueError:
                    print("Please enter a valid class!")

            student = Student(name)

            f.write(
                student.name.capitalize() +
                f" \n\t(Grade : {class_student})"+ 
                f" \n\t(Age : {Age})" + 
                f" \n\t(Roll no. : {Roll})" + 
                f" \n\t(Address : {Address})" + "\n"
                )


def students_by_grade():
    try:
        grade = input("Enter grade : ").strip()

        with open("Student_list.txt") as f:
            lines = [line.strip() for line in f.readlines()]

        result = []

        for i in range(1, len(lines)):
            if lines[i] == f"(Grade : {grade})":
                name_line = lines[i - 1]
                name = name_line.replace(" Information :-", "")
                result.append(name)

        if result:
            return f"Students in Grade {grade}:\n" + "\n".join(result)
        else:
            return f"No students found in Grade {grade}"

    except FileNotFoundError:
        return "Student list does not exist"


def student_info():
    result = ""

    try:
        student_name = input("Enter student's name : ")
        student_name = student_name.capitalize()
        key = f"{student_name}"

        with open("Student_list.txt") as f:
            lines = f.readlines() 
            for i in range(len(lines)):
                if lines[i].strip() == key:
                    for line in lines[i : i + 5]:
                        result += line
                    return result
            
            return f"{student_name} is not enrolled in this school."
                
    except FileNotFoundError:
        return "Student list does not exist"
        

class Teacher:
    salary  = 50000
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a teacher."
    

def save_teachers_list():
    num_teachers = int(input("How many teachers have been taken : "))

    with open("Teachers_list.txt","a")as f:
        for i in range(num_teachers):
            name = input("Enter teacher's name : ")

            while True:
                subject_teacher = input("Enter the teachers's subject : ")
                    
                if subject_teacher.lower() in [
                    "science","maths","social science","sports" ,
                    "hindi","english","pt","computer"
                    ]:
                    break
                    
                else:
                    print("Please enter a valid subject!")

            teacher = Teacher(name)
            
            f.write(teacher.name.capitalize() + f" (Subject : {subject_teacher.lower()})\n")


def see_teacher_list():
    result = "\nTeacher list:--\n"

    with open("Teachers_list.txt") as f:
            desired_subject = input("Enter subject (or type 0 to view all teachers): ")

            desired_subject = desired_subject.lower()

            if (desired_subject == "0"):
                result += f.read()
                return result
    
            elif desired_subject in  ["science","maths","social science",
                            "sports","hindi","english","pt","computer"]:
                
                lines = f.readlines()

                for line in lines:
                    if desired_subject in line:
                         result += line

                return result
            
            else:
                return "Please enter a valid subject!"
            
        
def total_teachers():
    try:
        with open("Teachers_list.txt") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0
    
    
print(
    "What do you want to do?\n" \
    "The functions you can perform are : \n" \
    "1. Enroll students.\n" \
    "2. See students list.\n" \
    "3. Check total number of students in school.\n" \
    "4. Take info about a student.\n" \
    "5. Recruit teachers.\n" \
    "6. See teachers list.\n" \
    "7. Check total number of teachers in school." \
)


while True:
    user_input = input("Enter function name or number written before it : ")

    if user_input == "1" or user_input.lower() == "enroll students": 
        save_students_list()
        break

    elif user_input == "2" or user_input.lower() == "see students list":
        print(students_by_grade())
        break

    elif user_input == "3" or user_input.lower() == "check total number of students in school":
        print(f"The total number of students in the school is {total_students()}")
        break

    elif user_input == "4" or user_input.lower() == "take info about a student":
        print(student_info())
        break

    elif user_input == "5" or user_input.lower() == "recruit teachers":
        save_teachers_list()
        break

    elif user_input == "6" or user_input.lower() == "see teachers list":
        print(see_teacher_list())
        break

    elif user_input == "7" or user_input.lower() == "check total number of teachers":
        print(f"The total number of teachers in the school is {total_teachers()}")
        break

    else:
        print("Please enter a valid function to be performed.")
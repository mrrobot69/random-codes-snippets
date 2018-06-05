students=[]

def get_students_titlecase():
    sttudents_titlecase=[]
    for student in students:
        sttudents_titlecase=student.title()
    return sttudents_titlecase
def print_student_titlecase():
    student_titlecase=get_students_titlecase()
    print(student_titlecase)
def add_student(name):
    students.append(name)

	
def write_file(student):
	try:
		f=open("student.txt","a")
		f.write(student + '\n')
		f.close
	except Exception:
		print("could not write")
		
		
def read_file():
	try:
		f=open("student.txt","r")
		for student in f.readlines():
			add_student(student)
		f.close
	except Exception:
		print("could not read file")




read_file()
print_student_titlecase()

student_name=input("students' name?")

add_student(student_name)
write_file(student_name)







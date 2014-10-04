#! usr/bin/python3

student_dict=dict()

def create_input():
	student_id=input("Please enter Student Id :")
	student_name=input("Please enter Student Name :")
	create_student(student_id,student_name)
	#

def create_student(student_id,student_name):
	if(student_id in student_dict):
		print("There already exist a student with provided id")
		print("To re-assign this id to someone else, please consider deleteing previous ones")
	else:
		student_dict[student_id]=student_name

	#

def view_input():
	print("1.View student using student_id\n2.View all students")
	choice=int(input("Please enter your choice :"))
	if(choice==1):
		student_id=input("Please enter student_id :")
		view_student(student_id)
	elif(choice==2):
		view_student()
	else:
		print("Please enter valid choice")
		view_input()
	#


def view_student(student_id=None):
	if(student_id==None):
		for student in student_dict.items():
			#print (student)
			print("Student Id :",student[0], "  Student Name :",student[1])
	elif(student_id in student_dict):
		print("Student Name :",student_dict[student_id])
	else:
		print("No such student exist")
		

	#

def delete_input():
	print("1.Delete student using student_id\n2.Delete all students")
	choice=int(input("Please enter your choice :"))
	if(choice==1):
		student_id=input("Please enter student_id :")
		delete_student(student_id)
	elif(choice==2):
		delete_student()
	else:
		print("Please enter valid choice")
		delete_input()


def delete_student(student_id=None):
	if(student_id==None):
		print("Deleting all students....")
		student_dict.clear()
	else:
		if(student_id in student_dict):
			del student_dict[student_id]
		else:
			print("No student with given student_id")

	#

def menu():
	print("1.Create\n2.View\n3.Delete")
	choice=int(input("Please enter your choice :"))
	if(choice==1):
		create_input()
	elif(choice==2):
		view_input()
	elif(choice==3):
		delete_input()
	else:
		print("Please enter valid choice")
		menu()
	#

if __name__=='__main__':
	menu()


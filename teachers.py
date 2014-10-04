#! usr/bin/python3
import association 


teacher_dict=dict()

def create_input():
	teacher_id=input("Please enter id of teacher :")
	teacher_name=input("Please enter name of teacher :")
	create_teacher(teacher_id,teacher_name)
	#

def create_teacher(teacher_id,teacher_name):
	if(teacher_id in teacher_dict):
		print("There is already a teacher with given id")
		print("To re-assign this to someone else, please consider deleting existing one")
	else:
		teacher_dict[teacher_id]=teacher_name

	#

def view_input():
	print("1.View teacher by id\n2.View all teachers")
	choice=int(input("Please enter your choice :"))
	if(choice==1):
		teacher_id=input("Please enter teacher_id :")
		view_teachers(teacher_id)
	elif(choice==2):
		view_teachers()
	else:
		print("Please enter valid choice")
		view_input()
	#

def view_teachers(teacher_id=None):
	if(teacher_id==None):
		for teacher in teacher_dict.items():
			print ("Teacher Id :" ,teacher[0] ,"   Teacher Name :",teacher[1])
	elif(teacher_id in teacher_dict):
		print("Teacher Name :",teacher_dict[teacher_id])
	else:
		print("No such teacher exists")

	#

def delete_input():
	teacher_id=input("Please enter id of teacher to be deleted :")
	delete_teacher(teacher_id)

	#

def delete_teacher(teacher_id):
	if(teacher_id not in teacher_dict):
		print("No such teacher_id exists")
	elif(teacher_id in association.association_dict.values()):
		print("Can't delete ",teacher_dict[teacher_id] ," , assiggned to some subject")
	else:
		del teacher_dict[teacher_id]

	#

def menu():
	print("1.Create\n2.View\n3.Delete ")
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

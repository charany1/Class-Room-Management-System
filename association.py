#! usr/bin/python3
import subjects,teachers

association_dict=dict()

def create_input():
	subject_id=input("Please enter subject_id :")
	teacher_id=input("Please enter teacher_id :")
	create_association(subject_id,teacher_id)
	#

def create_association(subject_id,teacher_id):
	if((subject_id not in subjects.subject_dict.keys() or teacher_id not in teachers.teacher_dict.keys())):
		print("Either given subject or teacher does not exist")
	if(subject_id in association_dict):
		print(subjects.subject_dict[subject_id] ," is already assigned to ", teachers.teacher_dict[teacher_id])
		print("Can't assign a subject to multiple teachers")
	else:
		association_dict[subject_id]=teacher_id

	#

def view_input():
	print("1.View by subject_id\n2 View all assocaitions")
	choice=int(input("Please enter your choice :"))
	if(choice==1):
		subject_id=input("Please enter subject_id :")
		view_association(subject_id)
	elif(choice==2):
		view_association()
	else:
		print("Please enter valid choice")
		view_input()
	#


def view_association(subject_id=None):
	if(subject_id==None):
		for association in association_dict.items():
			print ("Subject Name :" ,subjects.subject_dict[association[0]] ,"  Teacher Name :",teachers.teacher_dict[association[1]])
	elif(subject_id not in subjects.subject_dict.keys() or subject_id not in association_dict.keys()):
		print("Association does not exist")
	else:
		print("Subject Name :",subjects.subject_dict[subject_id],"  Teacher Name :",teachers.teacher_dict[association_dict[subject_id]])

	#

def delete_input():
	print("1.Delete by subject_id\n2.Delete all assocaitions")
	choice=int(input("Please enter your choice :"))
	if(choice==1):
		subject_id=input("Please enter subject_id :")
		delete_association(subject_id)
	elif(choice==2):
		delete_association()
	else:
		print("Please enter valid choice")
		delete_input()
	#

def delete_association(subject_id=None):
	if(subject_id not in subjects.subject_dict):
		print("There is no such subject .")
	elif(subject_id==None):
		print(" Deleting all assocaitions ...")
		association_dict.clear()
	elif(subject_id in association_dict):
		del association_dict[subject_id]
	else:
		print("This subject has no teacher assigned to it.")


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



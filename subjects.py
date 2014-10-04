#! usr/bin/env/python3

import association

subject_dict=dict()

def create_input():
	subject_id=input("Please enter subject_id :")
	subject_name=input("Please enter subject_name :")
	create_subject(subject_id,subject_name)
	#

def create_subject(subject_id,subject_name):
	if(subject_id in subject_dict):
		print("There is already a subject with given subject_id")
		print("To re-assign this subject_id to some other subject , please consider deleting existing one")
	else:
		subject_dict[subject_id]=subject_name

	#

def view_input():
	print("1.View subject by id\n2.View all subjects")
	choice=int(input("Enter your choice :"))
	if(choice==1):
		subject_id=input("Please enter subject_id :")
		view_subjects(subject_id)
	elif(choice==2):
		view_subjects()
	else:
		print("Please enter valid choice")
		view_input()
	#

def view_subjects(subject_id=None):
	if(subject_id==None):
		for subject in subject_dict.items():
			print("Subject Id :",subject[0],"  Subject Name :",subject[1])
	elif(subject_id in subject_dict):
		print("Subject Name :",subject_dict[subject_id])
	else:
		print("No such subject exists")
		

	#

def delete_input():
	subject_id=input("Please enter id of subject to be deleted :")
	delete_subject(subject_id)
	#

def delete_subject(subject_id):
	if(subject_id not in subject_dict):
		print("No such subject_id present")
	elif(subject_id in subject_dict and subject_id in association.association_dict.keys()):
		print("Can\'t delete ",subject_dict[subject_id]," already assigned to some teacher.")
	else:
		del subject_dict[subject_id]


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

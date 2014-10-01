#! usr/bin/ python 3.4

import os,json,sys

print("=================Classroom Management Program=============================")


student_list=subject_list=teacher_list=list()
subject_teacher_pairs=dict()

"""
Cretes new files if not already created.
If files already exist, doesn't delete them.

"""

print()

print("If you are first time user files to store information will be created")

print()


temp_file_ptr=open("students.json","a")
temp_file_ptr.close()

temp_file_ptr=open("teachers.json","a")
temp_file_ptr.close()

temp_file_ptr=open("subjects.json","a")
temp_file_ptr.close()

temp_file_ptr=open("subject_teacher_pairs.json","a")
temp_file_ptr.close()


print("============Loading information from files for the session ....=============")


print()

"""
For loading already exisitng information from files into the program

"""



if(os.stat("students.json")[6]!=0):
	fp=open("students.json")
	student_list=json.load(fp)
	fp.close()
	#print (student_list)
	#
if(os.stat("teachers.json")[6]!=0):
	fp=open("teachers.json")
	teacher_list=json.load(fp)
	fp.close()

if(os.stat("subjects.json")[6]!=0):
	fp=open("subjects.json")
	subject_list=json.load(fp)
	fp.close()

if(os.stat("subject_teacher_pairs.json")[6]!=0):
	fp=open("subject_teacher_pairs.json")
	subject_teacher_pairs=json.load(fp)
	fp.close()

"""
At this stage data to be processed is available in student_list,teacher_list,subject_list,
subject_teacher_pairs

"""
print(" ========Information loading completed=========== ")


print()
#Menu driven operations start here
while True:
	print("1:Student[View|Delete|Create|]\n2:Subject[View|Delete|Create|]")  
	print("3:Teacher[View|Delete|Create|]\n4:Subject_Teacher_Association[View|Assign|Deassign]\n0:Exit\n")

	choice=int(input("Please enter your choice :"))
	#student block starts here
	if(choice==1):
		print("1:View\n2:Delete\n3:Create")
		subchoice=int(input("Please enter your choice :"))
		if(subchoice==1 or subchoice==2):
			#check for underflow
			if(not student_list):
				print("There are no students...Please add some")
				continue
			elif(subchoice==1):
				for student  in student_list:
					print(student)
			elif(subchoice==2):
				student_to_be_deleted=input("Enter name of student to be deleted :")
				if(student_to_be_deleted not in student_list):
					print("There is no student with given name.......Going to main menu")
					continue
				else:
					student_list.remove(student_to_be_deleted)
		elif(subchoice==3):
			student_to_be_added=input("Please enter the name of student to added :")
			student_list.append(student_to_be_added)
		else:
			print("Invalid Choice......Going to main menu")
			continue
		# student block ends here

	#subject block starts here
	elif(choice==2):
		print("1:View\n2:Delete\n3:Create")
		subchoice=int(input("Please enter your choice :"))
		if(subchoice==1 or subchoice==2):
			if(not subject_list):
				print("There are no subject...Please add some")
				continue
			elif(subchoice==1):
				for subject in subject_list:
					print(subject)
			elif(subchoice==2):
				subject_to_be_deleted=input("Enter subject to be deleted :")
				if(subject_to_be_deleted not in subject_list):
					print("There is no subject with given name......Going to main menu")
					continue
				else:
					subject_list.remove(subject_to_be_deleted)
		elif(subchoice==3):
			subject_to_be_added=input("Please enter the name of subject to added")
			subject_list.append(subject_to_be_added)
		else:
			print("Invalid Choice......Going to main menu")
			continue

		#subject block ends here 

	#teacher block starts here

	elif(choice==3):
			print("1:View\n2:Delete\n3:Create")
			subchoice=int(input("Please enter your choice :"))
			if(subchoice==1 or subchoice==2):
				if(not teacher_list):
					print("There are no teachers...Please add some")
					continue
				elif(subchoice==1):
					for teacher in teacher_list:
						print(teacher)
				elif(subchoice==2):
					teacher_to_be_deleted=input("Enter teacher to be deleted :")
					if(teacher_to_be_deleted not in teacher_list):
						print("There is no teacher with given name......Going to main menu")
						continue
					else:
						teacher_list.remove(teacher_to_be_deleted)
			elif(subchoice==3):
				teacher_to_be_added=input("Please enter the name of teacher to added")
				teacher_list.append(teacher_to_be_added)
			else:
				print("Invalid Choice......Going to main menu")
				continue
			#teacher block ends here

	#subject-teacher associationship block starts here
	elif(choice==4):
		print("1:View\n2:Deassign\n3:Assign")
		subchoice=int(input("Please enter your choice :"))
		if(subchoice==1 or subchoice==2):
			if(not subject_teacher_pairs):
				print("There are no subject-teacher pairs yet .....Please add some")
			elif(subchoice==1):
				for subject_teacher_pair in subject_teacher_pairs.items():
					print(subject_teacher_pair[0],"   :   ",subject_teacher_pair[1])
			elif(subchoice==2):
				subject_teacher_pair_to_be_deassigned=input(" Enter name of subject  \
					which is to be deassigned ")
				del subject_teacher_pairs[subject_teacher_pair_to_be_deassigned]
		elif(subchoice==3):
			subject_to_be_assigned=input("Enter name of subject to be assigned")
			teacher_to_be_assigned=input("Enter name of teacher to be assigned")
			subject_teacher_pairs[subject_to_be_assigned]=teacher_to_be_assigned
		else:
			print("Please enter a valid choice ...Going back to main menu")

			#subject-teacher block ends here
	#exit block starts here
	elif(choice==0):
		print("Saving current session to files ......")
		for filename in ["students.json","teachers.json","subjects.json","subject_teacher_pairs.json"]:
			fp=open(filename,"w")
			if(filename=="students.json"):
				_json_data=json.dumps(student_list)
			elif(filename=="teachers.json"):
				_json_data=json.dumps(teacher_list)
			elif(filename=="subjects.json"):
				_json_data=json.dumps(subject_list)
			elif(filename=="subject_teacher_pairs.json"):
				_json_data=json.dumps(subject_teacher_pairs)
			else:
				pass
			fp.write(_json_data)
			fp.close()
		print("Current session saved successfully ..........")
		print()
		print("...................Session ends...............")
		sys.exit()

		#exit block ends here
	#default block starts here
	else:
		print("Please enter a valid choice ....Going to main menu")
		continue
		#default block ends here








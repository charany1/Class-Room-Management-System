#! usr/bin/env/python3

import json ,os,students,teachers,subjects,association

def loader():
	filename=input("Enter name of file :")
	if(os.path.isfile(filename) and filename.split('.')[-1]=='json'):
		print("Loading...")
		fp=open(filename,"r")
		all_data=json.load(fp)
		fp.close()
		students.student_dict=all_data[0]
		subjects.subject_dict=all_data[1]
		teachers.teacher_dict=all_data[2]
		association.association_dict=all_data[3]
	else:
		print("No such file exist")



def dumper():
	filename=input("Please enter filename :")
	all_data=[students.student_dict,subjects.subject_dict,teachers.teacher_dict,association.association_dict]
	fp=open(filename,"w")
	json.dump(all_data,fp)
	fp.close()

if __name__=='__main__':
	pass

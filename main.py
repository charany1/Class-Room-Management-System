#! usr/bin/python3

import sys,students,teachers,subjects,association,loader_dumper


def show_about():
    print('\n','-'*20)
    print ("Class Room Management System")
    print("(c) 2014 Yogeshwar Dan Charan")
    print("charany1 <www.github.com/charany1>")
    print('\n','-'*20)
    

def main_menu():
    while True:
        print("1.Students \n2.Subjects \n3.Teachers\n4.Subject-Teacher Association")
        print("5.Load\n6.Dump\n7.About\n0.Exit")
        choice=int(input("Please enter your choice :"))
        if(choice==1):
        	students.menu()
        elif(choice==2):
        	subjects.menu()
        elif(choice==3):
        	teachers.menu()
        elif(choice==4):
        	association.menu()
        elif(choice==5):
        	loader_dumper.loader()                #see about load interface-load() method signature
        elif(choice==6):
        	loader_dumper.dumper()
        elif(choice==7):
        	show_about()
        elif(choice==0):
        	sys.exit(0)
        else:
        	print("Please enter valid choice")
        	main_menu()


if __name__ == '__main__':
	main_menu()
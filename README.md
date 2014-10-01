Class Room Management System
===============================

A simple command line based  python program to demonstrate a **Class Room Management System** ,stores data in *json* format.

Usage
--------------
git clone 
cd Class_Room_Management_System
python3 class_room_management_system.py


Features:
------------

* *Create  |View   |Delete* Student   

* *Create  |View   |Delete* Teacher   

* *Create  |View   |Delete* Subject  
 
* *View    |Assign |Deassign* Subject-Teacher Associationship  

* Creates file for storing information when used for *first time*.   

* Automatically loads information from *json* files on startup   

* Saves current session's information in *json* files on exit.  

Issues:
-------------

* Currently there is no *consistency*(*integrity constraint*) *check* imposed  subject_teacher_pairs.json,subjects.json and teacher.json i.e. these all are currently independent of each other.


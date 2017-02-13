# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:39:10 2016

@author: sdasdadasdad
"""
from  PrettyTable import PrettyTable
from collections import defaultdict
import sys

def remain_courses(major,course1,file1):
    c = defaultdict(set)
    try:        
        content3 = open(file1,'r')
    except:
        print('tsadssssss')
        sys.exit()
    else:
        for line3 in content3.readlines(): 
            lst3 = line3.strip().split('|')
            major1 = lst3[0]
            course2 = set(lst3[1:])
            c[major1] = course2
        e = c[major]# to get all the course in this major
        p = e.difference(set(course1))# compare the course1 from def get_grades() with all the courses in this major.
        return p # the remained courses

def get_grades(CWID,file2):
    b = defaultdict(lambda: defaultdict(str))
    try:
        content2 = open(file2,'r')
    except:
        print('the file is not exist,please try again')
        sys.exit()
    else:
        for line2 in content2.readlines():               
            lst2 = line2.strip().split('|')
            CWID1,course,grade= lst2                 
            b[CWID1][course] = grade
        z = b[CWID] 
        course1 = list(z.keys()) # get a list of the courses
        return course1
    

def main(file3):
    a = defaultdict(lambda: defaultdict(str))
    try:
        content1 = open(file3,'r')
        x = PrettyTable(["CWID", "Major", "Name", "Remain courses"])        
    except:
        print('the file is not exist,please try again')
        sys.exit()
    else:
        for line1 in content1.readlines():
# each line in file of HW09_students.txt provides the CWID,name,major which will be using in def get_grades() and remain_courses()
            lst1 = line1.strip().split('|')
            CWID,name,major = lst1        
            a[CWID][major] = name
            w = get_grades(CWID,file2) # to get the courses which have been graded.
            q = remain_courses(major,w,file1)# to get the remain courses. 
            x.add_row([CWID,major,name,q]) # add all data to prettytable             
        print(x)        

       
file3 = input('Please input the file of student:')
file2 = input('Please input the file of grades:')
file1 = input('Please input the file of required courses:')
main(file3)




        
        

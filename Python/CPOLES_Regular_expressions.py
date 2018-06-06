#!/usr/bin/python3

"""
Copyright May 2018, Courtney Poles 
Purpose:
    Create and store student records for the Admission's office 
"""
#this class will store the below personal information for each student entry
class AdmissionsStudent:   
    _name =""
    _address = ""
    _city = ""
    _state = ""
    _zip = ""
    _gen=""
    _studentid = ""
    _gpa = 0.0

    # create student object with the above data members initialized to none
    def __init__(self,name=None,address=None,city=None,state=None,zipcode=None,gender=None,studentid=None,gpa=None):
        self._name = name
        self._address = address
        self._city = city
        self._state = state
        self._gen = gender
        self._zip = zipcode
        self._studentid = studentid
        self._gpa = gpa
    
    
    def display_student_record(self):
        # allows \ you to continue code on next line
        # "\n" new line
        return "\n"+"Student Name: " + self._name + "\n" + "Student Address: "+ self._address + "\n" + "Student City: " + self._city + "\n" + "Student State: " + self._state + "\n" + "Student Zipcode: " + self._zip + "\n"+"Student Gender: " + self._gen + "\n" + "Student ID: " + self._studentid + "\n" + "Student GPA: " + self._gpa + "\n"
        
        
        
    def __str__(self):
        return self.display_student_record()
    



#functions

#student_data_sublists
#purpose: break list into sublists
#student_data_sublists(list,desired size of sublists)

# the generator function student_data_sublists yields a series of results over time as opposed to a return function which executes
#once with a single result. A function becomes a generator function once the keyword yield is used.
# on the first iteration i = 0 and size= 8, on the second iteration i = 8 and size = 16, on the third i = 16 
# and size will equal 24
#yield returns a list of lists, each sublist will have the number of elements = to the value of parameter "size"

#put data for each student in a seperate list
def student_data_sublists(data,size):
    for i in range(0,len(data),size):
        yield data[i:i+size]
        


#read student data from file and put into list
#gracefully exit program with communication to user if file is not found

try:
    file = open('student.txt','r')
    lines = file.read().split('\n')
    file.close()
except:
    print("File not found.")
    exit()

#clean spaces
for s in lines:
    if s =='':
        lines.remove(s)



#create student record sublists
student_data= list(student_data_sublists(lines,8))



#generate an AdmissionsStudent object for each student sublist
student_objects = []
for i in range(0,len(student_data)):
    student_objects.append(AdmissionsStudent(*student_data[i]))


#print student records
for i in range(0,len(student_objects)):
    print(student_objects[i])


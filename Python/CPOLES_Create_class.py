
#!/usr/bin/python3


"""
Copyright April 2018, Courtney Poles 
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
    _studentid = ""
    _gpa = 0.0

    # create student object with the above data members initialized to none
    def __init__(self,name=None,address=None,city=None,state=None,zipcode=None,studentid=None,gpa=None):
        self._name = name
        self._address = address
        self._city = city
        self._state = state
        self._zip = zipcode
        self._studentid = studentid
        self._gpa = gpa
    
    
    def display_student_record(self):
        # allows \ you to continue code on next line
        # "\n" new line
        return "\n"+"Student Name: " + self._name + "\n" +         "Student Address: "+ self._address + "\n" +         "Student City: " + self._city + "\n" +         "Student State: " + self._state + "\n" +         "Student Zipcode: " + self._zip + "\n" +         "Student ID: " + self._studentid + "\n" +         "Student GPA: " + self._gpa + "\n"
        
        
        
    def __str__(self):
        return self.display_student_record()
        

    



#variables

#this variable regulates the while loop that collects student data from users
student_counter = 0

#these questions are used to collect student data from the user
input_requests = ["Please enter the student's name.","Please enter the student's street address.", 
                      "Please enter the student's city.","Please enter the student's state.",
                      "Please enter the student's zipcode.", "Please enter the student's id.", 
                      "Please enter the student's gpa."]

#student record variables
student1 = ""
student2 = ""
student3 = ""



#functions
def create_student_record():
    data_list = []
    for i in input_requests:
        entry = input(i+" "+":" )
        data_list.append(entry)
        
        #putting a * before a list inside () will turn list values into arguments
        student_record = AdmissionsStudent(*data_list)
   
    return student_record
    
#collect student data from users and create student objects
while student_counter < 3:
    print("Please enter student " + str(student_counter+1)+"'s information.")
    if student_counter == 0:
        student1 = create_student_record()
    elif student_counter == 1:
        student2 = create_student_record()
    else:
        student3 = create_student_record()
    student_counter = student_counter + 1
    
#print student information
print(student1,student2,student3, sep="\n")
    


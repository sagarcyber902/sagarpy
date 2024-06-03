class student:
    #class variable
    school_name="ABC School"

    #constructor
    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age

s1=student("Sagar",19)
#access instance variable
print("Student:",s1.name,s1.age)

#access class variable
print("School name:",student.school_name)

#modify instance variables
s1.name="Kedar"
s1.age=18
print("Student:",s1.name,s1.age)

#modify class variable
student.school_name="XYZ School"
print("School name:",student.school_name)

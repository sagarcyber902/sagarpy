#class methods demo
class student:
    #class variable
    school_name="ABC School"

    #constructor
    def __init__(self,name,age):
        #instance variable
        self.name=name
        self.age=age

    #instance method
    def show(self):
        #access instance variable and class variables
        print("Student:",self.name,self.age,student.school_name)

    #instance method
    def change_age(self,new_age):
        #modify instance variable
        self.age=new_age

    #class method
    @classmethod
    def modify_school_name(cls,new_name):
        #modify class variable
        cls.school_name=new_name

s1=student("Sagar",20)

#call instance method
s1.show()
s1.change_age(19)

#call class method
student.modify_school_name("XYZ School")
#call instance method
s1.show()
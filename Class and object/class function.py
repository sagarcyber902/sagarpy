#Python In-Built class function

class student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age

#creates the object of the class student
s=student("Sagar",47,20)

#prints the attribute name of the object s
print(getattr(s,"name"))

#reset the value of attribute age to 23
setattr(s,"age",23)

#prints the modified value of age
print(getattr(s,"age"))

#prints true if the student contains the attribute with name id
print(hasattr(s,"id"))

#deletes the attribute age
delattr(s,"age")

#gives error since age is deleted
print(s.age)

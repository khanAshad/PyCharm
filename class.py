class student:
    '''This is documentation for class'''
    College='MITS'                         #static variable,class level
    def __init__(self):
        self.name="Ashad"                  #instance variable, object level
        self.rollno=15
        self.marks=100
        student.Department="cse & it"        #static variable,class level
        print("hello you are in init method")
    def __str__(self):
        return "This is from __str__ method"
    def display(self):
        Branch="IT"                          #local variable,method level
        print("Name:",self.name)
        print("Roll no.:",self.rollno)
        print("Marks:",self.marks)
        print("College:",student.College)
        print("Department:",student.Department)
        print("Branch:",Branch)
student.City="Gwalior"              #static variable,class level
S=student()
print(S.__doc__)
print(S)                          ## calling __str__ method
S.display()
print(S.College)                 #calling static variable
print(S.Department)


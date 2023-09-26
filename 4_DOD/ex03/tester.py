
from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

student = Student(name="Edward", surname="agle", id="toto")
print(student)

# Expected output
# Student(name='Edward', surname='agle', active=True,
# login='Eagle', id='trannxhndgtolvh')

# TypeError: Student.__init__() got an unexpected keyword argument 'id'

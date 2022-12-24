student=[[25,'Kasheefa',76,80],[4,'Bareera',80,85],[35,'Mounika',79,84],[60,'Supriya',78,84]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)

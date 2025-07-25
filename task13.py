#TASK 1   ASSIGNMENT 5


students = {'alice' : 85 , 'aryan' : 78 , 'john' : 54}
n = input("Enter student name: ")
if (n in students):
    print(f"{n}'s marks:",students[n])
else:
    print("student not found")


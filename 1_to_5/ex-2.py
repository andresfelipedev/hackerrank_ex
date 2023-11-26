"""

Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

"""



def doing_array(arr):
    for item in range(len(arr)):
        print(arr[item][1])



def main():
    students_and_grades = []
    for i in range(0,3):

        name = input()
        score = float(input())

        each_one = [name, score]
        students_and_grades.append(each_one)

    doing_array(students_and_grades)



main()
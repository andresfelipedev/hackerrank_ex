"""

Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

"""
##### array real
real_arr = [["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]


#####


def doing_array(arr):
    order_arr = sorted(arr, key = lambda x: x[1])
##
    print(order_arr)
##
    looking_for = order_arr[1][1]
    getting_same = [student_data[0] for student_data in order_arr for value in student_data if value == looking_for]

    diference_ = sorted(getting_same, reverse=False)



    for i in range(len(getting_same)):
        print(diference_[i])





doing_array(real_arr)

"""
def main():
    students_and_grades = []
    for i in range(0,3):

        name = input()
        score = float(input())

        each_one = [name, score]
        students_and_grades.append(each_one)

    doing_array(students_and_grades)



main()
"""
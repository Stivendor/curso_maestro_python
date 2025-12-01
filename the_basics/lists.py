# Lists are ordered collections of items that can be of different data types 
students_grades = [1, 2, 3, 4, 5]
print(students_grades)

## the list can be of different data types
students_grades = ["John", 1, 2, 3, 4, 5]
print(students_grades)

## it also exists the range function that generates a sequence of numbers
students_grades = list(range(0, 5, 2)) # the number 2 is the step, so it will generate 0, 2, 4
print(students_grades)

# Average of a list of numbers, in this case the list is students_grades
student_grades = [2.2, 5, 4.7]
# the lists have methods that can be used to perform operations on the list
average = sum(student_grades) / len(student_grades)
print(average)
# sum = sum(list) with this we can sum all the numbers in the list
# len = len(list) with this we can get the length of a list

# Maximum and minimun value of a list of numbers
max_value = max(student_grades)
print(max_value)
min_value = min(student_grades)
print(min_value)

# Count the number of times a value appears in a list
count = student_grades.count(2.2)
print(count)
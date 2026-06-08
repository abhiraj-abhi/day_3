student_name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

if marks >= 40:
    status = "PASS"
else:
    status = "FAIL"

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("\nStudent Result")
print("Student Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)
print("Status:", status)
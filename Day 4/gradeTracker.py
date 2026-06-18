students = {
    "hareesh": 43,
    "arjun": 90,
    "rahul": 35,
    "anu": 80
}

#compute average  

average = sum(students.values()) / len(students)

#find toper 

topper = max(students,key=students.get)
# print(toper)

# failed students

failed = {name :mark for name,mark in students.items() if mark < 50}
print(failed)

# formated report 

print("----- Student Report -----")
print(f"Average Marks: {average:.2f}")
print(f"Topper: {topper} ({students[topper]})")

print("\nFailed Students:")
for name, marks in students.items():
    print(f"{name} - {marks}")

print("\nAll Students:")
for name, marks in students.items():
    status = "Pass" if marks >= 50 else "Fail"
    print(f"{name:<10} : {marks} ({status})")
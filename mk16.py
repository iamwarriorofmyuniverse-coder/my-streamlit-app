import matplotlib.pyplot as plt

students = ["Bruce", "Wayne", "Ronin", "Hal", "Clark"]
colors = ["#38bdf8", "#34d399", "#f59e0b", "#f87171", "#a855f7"]
marks_data = {
    "Maths": [95, 78, 92, 65, 88],
    "Physics": [88, 82, 90, 70, 85],
    "Chemistry": [92, 80, 94, 68, 89],
    "English": [85, 75, 88, 80, 90],
    "Computer": [98, 89, 96, 74, 91]
}


print("Available Subjects: Maths, Physics, Chemistry, English, Computer")
sub = input("Enter the subject name: ")


if sub in marks_data:
    subject_marks = marks_data[sub]
    
    print("\n--- Marks of 5 Students in", sub, "---")
    for i in range(len(students)):
        print(students[i], ":", subject_marks[i])
        
    avg = sum(subject_marks) / len(subject_marks)
    print("\nAverage Marks:", avg)
    
 
    plt.bar(students, subject_marks, color=colors, edgecolor='black')
    plt.title("Marks in " + sub)
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.show()

else:
    print("Subject not found! Please check spelling.")
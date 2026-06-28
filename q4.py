# Class to represent a Student
class Student:

    # Constructor to initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Method to add a mark to the list
    def add_mark(self, mark):
        try:
            # Check if mark is within valid range
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")

            self.marks_list.append(mark)

        except ValueError as e:
            print("Error:", e)

    # Method to calculate average marks
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Method to display student details
    def display_info(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average Marks:", self.get_average())


# Main Program

# Take student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Create Student object
student = Student(name, roll_no)

# Take marks input
print("\nEnter marks for 5 subjects:")

for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter mark {i + 1}: "))
            student.add_mark(mark)

            # Add only valid marks
            if 0 <= mark <= 100:
                break

        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Display student information
student.display_info()

# Display average separately
print("Average returned by get_average():", student.get_average())
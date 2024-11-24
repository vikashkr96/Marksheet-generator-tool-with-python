class Marksheet:
    
    # Method to calculate percentage
    def calculate_percentage(self, total_marks, max_marks):
        return total_marks / max_marks * 100

    # Method to determine grade based on percentage
    def grade_vikash(self, percentage):
        if percentage > 90 and percentage <= 100:
            return "Grade- A+"
        elif percentage > 80 and percentage <= 90:
            return "Grade- A"
        elif percentage > 70 and percentage <= 80:
            return "Grade- B+"
        elif percentage > 60 and percentage <= 70:
            return "Grade- B"
        elif percentage > 33 and percentage <= 60:
            return "Grade- C"
        elif percentage > 0 and percentage <= 33:
            return "Fail !"
        else:
            return "Invalid input !!"
        
    # Method to generate the marksheet
    def marksheet_vikash(self):
        print("-------------------------- LAXMI NARAYAN DUBEY COLLEGE, MOTIHARI ---------------------\n")
        print("A CONSTITUENT UNIT OF B.R.A. BIHAR UNIVERSITY, MUZAFFARPUR\n")

        name = input("Enter name of Student - ")
        roll_number = input("Enter registration number  - ")
    
        print("Course Name | Intermediate(12th) \n")
    
        subjects = [
            "Physics",
            "Maths",
            "Chemistry",
            "English",
            "Hindi"
        ]
        
        total_subject_marks = 0
        max_marks_per_subject = 100
        max_total_marks = len(subjects) * max_marks_per_subject  # 5 subjects, 100 marks each
        
        input_marks = []  # To store marks for each subject

        # Input marks for each subject
        for subject in subjects:
            marks = int(input(f"Enter marks for | {subject}: "))
            input_marks.append(marks)
            total_subject_marks += marks

        total_marks = total_subject_marks
        percentage = self.calculate_percentage(total_marks, max_total_marks)
        grade = self.grade_vikash(percentage)

        print("\n")
        print("                                                MARKSHEET                                                   \n")
        print("--------------------------- Laxmi Narain Dubey College, Motihari -------------------\n")
        print("A CONSTITUENT UNIT OF B.R.A. BIHAR UNIVERSITY, MUZAFFARPUR\n")
        print("                                         ANNUAL STATEMENT OF MARKS                                          \n")
        print(f"Name: {name}")
        print(f"Roll Number: {roll_number}")
        print("Course Name | Intermediate(12th) \n")
    
        print("\n------------------------------------------------------------------------------------------------------------\n")
        
        # Print subject names with aligned max and obtained marks
        print("Subject Name                             Max Marks     |   Obtained Marks")
        
        for subject in subjects:
            print(f"{subject:<40} {max_marks_per_subject:<13} |   {input_marks[subjects.index(subject)]:<13}")

        print("\n---------------------------------------------------- Results -----------------------------------------------")
        print(f"Total Marks: {total_marks} / {max_total_marks}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print("\n------------------------------------------------------------------------------------------------------------")
    
# Create an instance of the Marksheet class
marksheet_instance = Marksheet()
# Generate the marksheet by calling the method
marksheet_instance.marksheet_vikash()
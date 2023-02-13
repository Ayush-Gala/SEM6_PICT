#script to generate with NaN values
import random
import csv

# Create a list of 7000 student IDs
student_ids = [i+1 for i in range(7000)]

# Define a function to generate a random gender
def random_gender():
    return random.choice(["Male", "Female"])

# Define a function to generate a random age
def random_age():
    return random.randint(17, 21)

# Define a list of schools
schools = ["A", "B", "C", "D", "E"]

# Define a function to generate a random school
def random_school():
    return random.choice(schools)

# Define a function to generate a random score
def random_score():
    return random.randint(30, 100)

# Define a function to generate a random class performance
def random_performance(score):
    # score = random_score()
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Create a list of lists to store the student data
data = []

# Loop over the student IDs and generate random data for each student
for student_id in student_ids:
    gender = random_gender()
    age = random_age()
    school = random_school()
    math_score = random_score()
    reading_score = random_score()
    writing_score = random_score()
    performance = random_performance((math_score+reading_score+writing_score)/3)
    
    # Include missing values in a random percentage of cases
    missing_value = random.random()
    if missing_value < 0.05:
        math_score = None
    elif missing_value < 0.1:
        reading_score = None
    elif missing_value < 0.15:
        writing_score = None
    
    # Include outliers in a random percentage of cases
    outlier = random.random()
    if outlier < 0.01:
        math_score = random.randint(110, 150)
    elif outlier < 0.02:
        reading_score = random.randint(110, 150)
    elif outlier < 0.03:
        writing_score = random.randint(110, 150)
    
    student_data = [student_id, gender, age, school, math_score, reading_score, writing_score, performance]
    data.append(student_data)

# Write the data to a .csv file
with open("student_performance_2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Student ID", "Gender", "Age", "School", "Math Score", "Reading Score", "Writing Score", "Class Performance"])
    writer.writerows(data)

import pandas as pd
import random

# ==============================================================================
# EDUPREDICTAI - COMPLETE ROSTER LIBRARY GENERATOR
# Generates the 60-Student Original list alongside the Expanded Tiers
# ==============================================================================

# 1. GENERATE THE ORIGINAL VERSION (60 Students)
original_roster = [
    {"roll_number": "2026CS01", "student_name": "Prajnyashree Giri", "study_hours": 8, "attendance": 92, "assignments": 88, "quizzes": 90},
    {"roll_number": "2026CS02", "student_name": "Samruddhi Gosalkar", "study_hours": 7, "attendance": 85, "assignments": 80, "quizzes": 78},
    {"roll_number": "2026CS03", "student_name": "Sara Pawar", "study_hours": 6, "attendance": 80, "assignments": 75, "quizzes": 72},
    {"roll_number": "2026CS04", "student_name": "Sayali Shanuja", "study_hours": 5, "attendance": 78, "assignments": 70, "quizzes": 68},
    {"roll_number": "2026CS05", "student_name": "Simran Singh", "study_hours": 4, "attendance": 70, "assignments": 65, "quizzes": 60},
    {"roll_number": "2026CS06", "student_name": "Aanchal More", "study_hours": 3, "attendance": 65, "assignments": 60, "quizzes": 55},
    {"roll_number": "2026CS07", "student_name": "Viraj Mali", "study_hours": 2, "attendance": 60, "assignments": 50, "quizzes": 48},
    {"roll_number": "2026CS08", "student_name": "Hashmeet Syan", "study_hours": 1, "attendance": 55, "assignments": 45, "quizzes": 40},
    {"roll_number": "2026CS09", "student_name": "Harshwardhan Zalte", "study_hours": 9, "attendance": 95, "assignments": 92, "quizzes": 94},
    {"roll_number": "2026CS10", "student_name": "Sahil S Patel", "study_hours": 6, "attendance": 82, "assignments": 78, "quizzes": 76},
    {"roll_number": "2026CS11", "student_name": "Prathmesh Sutar", "study_hours": 7, "attendance": 88, "assignments": 84, "quizzes": 82},
    {"roll_number": "2026CS12", "student_name": "Anurag Sutar", "study_hours": 5, "attendance": 75, "assignments": 70, "quizzes": 72},
    {"roll_number": "2026CS13", "student_name": "Vishal Agrahari", "study_hours": 3, "attendance": 62, "assignments": 58, "quizzes": 54},
    {"roll_number": "2026CS14", "student_name": "Rohan Aryi", "study_hours": 2, "attendance": 58, "assignments": 52, "quizzes": 50},
    {"roll_number": "2026CS15", "student_name": "Krishna Prajapati", "study_hours": 4, "attendance": 68, "assignments": 64, "quizzes": 60},
    {"roll_number": "2026CS16", "student_name": "Harshal Patond", "study_hours": 8, "attendance": 90, "assignments": 86, "quizzes": 88},
    {"roll_number": "2026CS17", "student_name": "Praneet Revankar", "study_hours": 1, "attendance": 50, "assignments": 40, "quizzes": 35},
    {"roll_number": "2026CS18", "student_name": "Ashish Ghadge", "study_hours": 9, "attendance": 97, "assignments": 94, "quizzes": 96},
    {"roll_number": "2026CS19", "student_name": "Bhupali Sharma", "study_hours": 6, "attendance": 79, "assignments": 74, "quizzes": 70},
    {"roll_number": "2026CS20", "student_name": "Muskaan Sharma", "study_hours": 7, "attendance": 83, "assignments": 78, "quizzes": 75},
    {"roll_number": "2026CS21", "student_name": "Sahil Suryawanshi", "study_hours": 5, "attendance": 72, "assignments": 68, "quizzes": 65},
    {"roll_number": "2026CS22", "student_name": "Ketan Bhoye", "study_hours": 3, "attendance": 60, "assignments": 55, "quizzes": 50},
    {"roll_number": "2026CS23", "student_name": "Ankosh Sondkar", "study_hours": 2, "attendance": 57, "assignments": 48, "quizzes": 45},
    {"roll_number": "2026CS24", "student_name": "Shlok Kadam", "study_hours": 4, "attendance": 66, "assignments": 60, "quizzes": 58},
    {"roll_number": "2026CS25", "student_name": "Mohd Masihood Khan", "study_hours": 8, "attendance": 91, "assignments": 89, "quizzes": 87},
    {"roll_number": "2026CS26", "student_name": "Aryan Mali", "study_hours": 5.4, "attendance": 78, "assignments": 67, "quizzes": 65},
    {"roll_number": "2026CS27", "student_name": "Rudra Khairnale", "study_hours": 4.2, "attendance": 71, "assignments": 59, "quizzes": 56},
    {"roll_number": "2026CS28", "student_name": "Sarvesh Santosh Parab", "study_hours": 6.9, "attendance": 67, "assignments": 57, "quizzes": 58},
    {"roll_number": "2026CS29", "student_name": "Sahil Akash Patil", "study_hours": 6.3, "attendance": 52, "assignments": 59, "quizzes": 86},
    {"roll_number": "2026CS30", "student_name": "Amol Amar Pawar", "study_hours": 7.9, "attendance": 90, "assignments": 86, "quizzes": 85},
    {"roll_number": "2026CS31", "student_name": "Avishkar Mandhare", "study_hours": 8.1, "attendance": 91, "assignments": 89, "quizzes": 86},
    {"roll_number": "2026CS32", "student_name": "Vinod Sule", "study_hours": 9.4, "attendance": 97, "assignments": 97, "quizzes": 96},
    {"roll_number": "2026CS33", "student_name": "Vedant Pingat", "study_hours": 7.3, "attendance": 89, "assignments": 84, "quizzes": 82},
    {"roll_number": "2026CS34", "student_name": "Shubham Gadge", "study_hours": 8.6, "attendance": 94, "assignments": 90, "quizzes": 89},
    {"roll_number": "2026CS35", "student_name": "Saanvi Sahu", "study_hours": 6.4, "attendance": 82, "assignments": 76, "quizzes": 78},
    {"roll_number": "2026CS36", "student_name": "Nidhi Sinha", "study_hours": 8.0, "attendance": 90, "assignments": 86, "quizzes": 85},
    {"roll_number": "2026CS37", "student_name": "Swapnil Dhivore", "study_hours": 7.7, "attendance": 88, "assignments": 85, "quizzes": 83},
    {"roll_number": "2026CS38", "student_name": "Om Chavan", "study_hours": 9.3, "attendance": 96, "assignments": 94, "quizzes": 92},
    {"roll_number": "2026CS39", "student_name": "Vedika Bane", "study_hours": 7.1, "attendance": 87, "assignments": 81, "quizzes": 80},
    {"roll_number": "2026CS40", "student_name": "Manas Bhole", "study_hours": 8.5, "attendance": 93, "assignments": 91, "quizzes": 89},
    {"roll_number": "2026CS41", "student_name": "Suraj Solanki", "study_hours": 6.9, "attendance": 84, "assignments": 79, "quizzes": 81},
    {"roll_number": "2026CS42", "student_name": "Rishabh Manale", "study_hours": 4.8, "attendance": 74, "assignments": 65, "quizzes": 62},
    {"roll_number": "2026CS43", "student_name": "Swagat Kochrekar", "study_hours": 5.2, "attendance": 76, "assignments": 68, "quizzes": 64},
    {"roll_number": "2026CS44", "student_name": "Shubham Waidkar", "study_hours": 4.1, "attendance": 70, "assignments": 58, "quizzes": 59},
    {"roll_number": "2026CS45", "student_name": "Soham Memry", "study_hours": 5.5, "attendance": 77, "assignments": 69, "quizzes": 66},
    {"roll_number": "2026CS46", "student_name": "Saurabh Kumar Dixit", "study_hours": 3.8, "attendance": 66, "assignments": 56, "quizzes": 55},
    {"roll_number": "2026CS47", "student_name": "Saurabh Kumar", "study_hours": 5.0, "attendance": 75, "assignments": 64, "quizzes": 61},
    {"roll_number": "2026CS48", "student_name": "Soham Sayyed", "study_hours": 4.3, "attendance": 69, "assignments": 60, "quizzes": 58},
    {"roll_number": "2026CS49", "student_name": "Shubham Godse", "study_hours": 5.4, "attendance": 78, "assignments": 67, "quizzes": 65},
    {"roll_number": "2026CS50", "student_name": "Shubham Mishra", "study_hours": 3.9, "attendance": 68, "assignments": 55, "quizzes": 57},
    {"roll_number": "2026CS51", "student_name": "Rahul Prajapati", "study_hours": 4.7, "attendance": 73, "assignments": 63, "quizzes": 60},
    {"roll_number": "2026CS52", "student_name": "Kanak Jangid", "study_hours": 4.2, "attendance": 71, "assignments": 59, "quizzes": 56},
    {"roll_number": "2026CS53", "student_name": "Vikram Jha", "study_hours": 5.1, "attendance": 76, "assignments": 66, "quizzes": 63},
    {"roll_number": "2026CS54", "student_name": "Vidha Kokle", "study_hours": 3.6, "attendance": 65, "assignments": 54, "quizzes": 54},
    {"roll_number": "2026CS55", "student_name": "Aryan Bhole", "study_hours": 5.3, "attendance": 77, "assignments": 68, "quizzes": 67},
    {"roll_number": "2026CS56", "student_name": "Suraj Gond", "study_hours": 4.0, "attendance": 67, "assignments": 57, "quizzes": 58},
    {"roll_number": "2026CS57", "student_name": "Deepak Naik", "study_hours": 2.5, "attendance": 55, "assignments": 45, "quizzes": 40},
    {"roll_number": "2026CS58", "student_name": "Aditya Yadav", "study_hours": 1.8, "attendance": 48, "assignments": 38, "quizzes": 42},
    {"roll_number": "2026CS59", "student_name": "Pratiksha Zodge", "study_hours": 3.0, "attendance": 60, "assignments": 50, "quizzes": 48},
    {"roll_number": "2026CS60", "student_name": "Divesh Khairnar", "study_hours": 1.2, "attendance": 42, "assignments": 32, "quizzes": 35}
]

# 2. HELPER TO GENERATE NEW DYNAMIC VOLUMES
first_names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Reyansh", "Krishna", "Ishaan", "Shaurya", "Diya", "Ananya"]
last_names = ["Sharma", "Verma", "Patel", "Singh", "Joshi", "Kumar", "Reddy", "Nair", "Mehra", "Gupta"]

def generate_dynamic_list(class_prefix, total_students, seed_val):
    random.seed(seed_val)
    students = []
    for i in range(1, total_students + 1):
        roll_no = f"{class_prefix}{i:02d}"
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        if i <= (total_students * 0.7):
            study = round(random.uniform(6.0, 9.5), 1)
            attendance = random.randint(80, 98)
            assignments = random.randint(75, 95)
            quizzes = random.randint(75, 95)
        else:
            study = round(random.uniform(1.5, 4.5), 1)
            attendance = random.randint(45, 68)
            assignments = random.randint(35, 60)
            quizzes = random.randint(35, 60)

        students.append({
            "roll_number": roll_no,
            "student_name": name,
            "study_hours": study,
            "attendance": attendance,
            "assignments": assignments,
            "quizzes": quizzes
        })
    return students

# Generate standard files

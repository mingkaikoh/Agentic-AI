def calculate_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'Pass'
    else:
        return 'Fail'

def xmum_grading_system():
    print("--- Xiamen University Malaysia Grading Portal ---")
    try:
        student_id = input("Enter Student ID: ")
        score_input = input(f"Enter total marks for student {student_id}: ")
        score = float(score_input)

        if score < 0 or score > 100:
            print("Error: Valid marks range is 0 to 100.")
            return

        grade = calculate_grade(score)
        print(f"ID: {student_id}")
        print(f"Calculated Grade: {grade}")

        if grade == 'Fail':
            print("Status: Required to resit the subjects.")
        else:
            print("Status: Requirements met. Congrats!")

    except ValueError:
        print("Input Error: Marks must be a numerical value.")

if __name__ == "__main__":
    xmum_grading_system()
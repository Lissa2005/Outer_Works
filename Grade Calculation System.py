#Upgraded Grade Calculation System

def calculate_final_grade(coursework, midterm, final_exam):
    if not (0 <= coursework <= 100 and 0 <= midterm <= 100 and 0 <= final_exam <= 100):
        return "Error", "Invalid input: Scores must be between 0 and 100."
    
    final_score = (coursework * 0.40) + (midterm * 0.25) + (final_exam * 0.35)
    
    if final_score >= 70:
        grade = 'A'
    elif final_score >= 50:
        grade = 'B'
    elif final_score >= 40:
        grade = 'C'
    else:
        grade = 'F'
    
    return final_score, grade

def main():
    try:
        coursework = float(input("Enter coursework score (0-100): "))
        midterm = float(input("Enter midterm exam score (0-100): "))
        final_exam = float(input("Enter final exam score (0-100): "))
        
        final_score, grade = calculate_final_grade(coursework, midterm, final_exam)
        
        if final_score == "Error":
            print(grade)  # Display error message
        else:
            print(f"Final Grade: {final_score:.2f}")
            print(f"Letter Grade: {grade}")
            
    except ValueError:
        print("Invalid input: Please enter numeric values only.")

if __name__ == "__main__":
    main()

from collections import deque

grade_stack = []           
pending_queue = deque()    
final_grades = []          

 #Add a new submission to the queue of pending grades.
def add_submission(student_id):
   
    pending_queue.append(student_id)
    print(f"Submission added for student {student_id}.")
 # Grade the next student in the pending queue and add to stack for undo option.
def grade_next_submission(grade):
   
    if pending_queue:
        student_id = pending_queue.popleft()
        grade_stack.append((student_id, grade)) 
        final_grades.append((student_id, grade))
        print(f"Graded student {student_id} with grade {grade}.")
    else:
        print("No pending submissions to grade.")

def undo_last_grade():
    #Undo the last graded submission
    if grade_stack:
        student_id, grade = grade_stack.pop()  
        final_grades.remove((student_id, grade))  
        print(f"Undoing grade {grade} for student {student_id}.")
    else:
        print("No grades to undo.")

def view_final_grades():
    #Display all finalized student grades.
    if final_grades:
        print("Final Grades List:")
        for student_id, grade in final_grades:
            print(f"Student {student_id}: {grade}")
    else:
        print("No final grades to display.")

def view_pending_submissions():
    #Display all pending submissions
    if pending_queue:
        print("Pending Submissions:")
        for student_id in pending_queue:
            print(f"Student {student_id}")
    else:
        print("No pending submissions.")

# Example usage
add_submission(101)
add_submission(102)
add_submission(103)

# Grade the first two submissions
grade_next_submission(90)   
grade_next_submission(85)   

# Undo the last grading action
undo_last_grade()

# View final grades and pending submissions
view_final_grades()
view_pending_submissions()

# Grade the remaining submission
grade_next_submission(75)   

# Final grades after grading the last submission
view_final_grades()

# all grading functions
def grading(grade, weight: float) -> float:
    if grade == lab or grade == quiz:
        return weight * int(grade) / 6 if int(grade) <= 6 else weight
    else:
        return grade * weight * 10 ** -2


def total() -> float:
    return lab_wgr + quiz_wgr + asgn_wgr + midterms + final_wgr + mid_final_prep_wgr


# inputting grades (asgn = assignment)
print("Welcome to the ITP course's grade calculator\n    ")
print('Enter ONLY numerical values in the following  prompts.')
lab: str = input('The number of labs completed: ')
quiz: str = input('The number of quizzes completed: ')
print()
print("Enter your grades for the following assessments.")
asgn_1: float = float(input('Assignment 1: '))
asgn_2: float = float(input('Assignment 2: '))
asgn_3: float = float(input('Assignment 3: '))
asgn_4: float = float(input('Assignment 4: '))
midterm1: float = float(input('Midterm 1: '))
midterm2: float = float(input('Midterm 2: '))
Final: float = float(input('Final Exam: '))
mid_and_final: float = float(input('Midterms + Final Preparation: '))

# computing total grades (wgr = weighted grade)
lab_wgr = grading(lab, 20)
quiz_wgr = grading(quiz, 15)
average_asgn = (asgn_1 + asgn_2 + asgn_3 + asgn_4) / 4
asgn_wgr = grading(average_asgn, 16)
average_midterms = (midterm2 + midterm1) / 2
midterms = grading(average_midterms, 25)
mid_final_prep_wgr = grading(mid_and_final, 6)
final_wgr = grading(Final, 18)

print(f'Your final grade for the course: {round(total(), 2)}  %')

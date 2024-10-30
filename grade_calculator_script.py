num_lab_prob = int(input("Enter the number of labs completed: "))

num_quiz = int(input("Enter the number of quizzes completed: "))

mrk_ass_1 = int(input("Enter the grade for assignment 1: "))

mrk_ass_2 = int(input("Enter the grade for assignment 2: "))

mrk_ass_3 = int(input("Enter the grade for assignment 3: "))

mrk_ass_4 = int(input("Enter the grade for assignment 4: "))

mrk_mid_1 = int(input("Enter the grade for the midterm 1: "))

mrk_mid_2 = int(input("Enter the grade for the midterm 2: "))

mrk_final_exam = int(input("Enter the grade for the final exam: "))

mrk_mid_fin_prep = int(input("Enter the grade for midterms and final preparation: "))

def get_mrk(x:int) -> float:
    if x > 6:
        return 100
    else:
        return x/6 * 100

mrk_lab_prob = get_mrk(num_lab_prob)

mrk_quiz = get_mrk(num_quiz)

final_avg = (0.2 * mrk_lab_prob) + (0.15 * mrk_quiz) + ((mrk_ass_1 + mrk_ass_2 + mrk_ass_3 + mrk_ass_4) / 4) * 0.16 + ((mrk_mid_1 + mrk_mid_2) / 2) * 0.25 + 0.18 * mrk_final_exam + 0.06 * mrk_mid_fin_prep

print("Your grade is:", int(final_avg))

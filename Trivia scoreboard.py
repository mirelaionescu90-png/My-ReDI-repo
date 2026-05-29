player = "Mirela"
correct_answers = int(input("How many correct answers? "))
wrong_answers = int(input("How many correct answers? "))
bonus_question = 1

total_questions = (correct_answers) + (wrong_answers) + (bonus_question)
total_correct_answers = (total_questions) - (wrong_answers)
total_wrong_answers = (total_questions) - (correct_answers)
final_score = (correct_answers * 3) + (wrong_answers *1)

print(f"{player} answered {total_questions} questions.")
print(f"{player} answered {total_correct_answers} correctly.")
print(f"{player} answered {total_wrong_answers} wrongly.")
print(f"{player} scored {final_score} points. Good job!")
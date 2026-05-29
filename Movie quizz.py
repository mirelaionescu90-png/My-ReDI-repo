player = input("What is the name of the player? ")
easy_questions = 7
hard_questions = 13

total_questions = easy_questions + hard_questions
correct_answers = 5
wrong_answers = 2
total_score = (correct_answers) - (wrong_answers)

print(f"{player} answered {total_questions} questions and scored {total_score} points.")
print(f"Well done, {player}!")
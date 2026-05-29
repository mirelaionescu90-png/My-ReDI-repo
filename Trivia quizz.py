player_name = input("Enter the name of the player: ")
correct_answers = int(input("How many correct answers? "))
wrong_answers = int(input("How many wrong answers? "))

total_score = (correct_answers * 10) - (wrong_answers * 2)

print(f"{player_name} scored {total_score} points!")



user = input("Enter the name of the player: ")
correct_answers = int(input("How many correct answers? "))
wrong_answers = int(input("How many wrong answers? "))

total_questions = correct_answers + wrong_answers
total_score = (correct_answers * 5) - (wrong_answers * 2)

print(f"{user} answered {total_questions} and scored {total_score} points.")
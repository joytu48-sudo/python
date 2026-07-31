total_chores = 4
original_chores = total_chores
print(f"you have {total_chores} to complete today, complete them now!")

completed_chores = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1:
        next_chore = "Make your bed"
    elif chore_num == 2:
        next_chore = "Feed the pet"
    elif chore_num == 3:
        next_chore = "Take out the trash"
    elif chore_num == 4:
        next_chore = "Wash the dishes"

    answer = input(f"have you completed {next_chore}? [yes|no]: ").lower()

    if answer == "yes":
        completed_chores += 1
        chore_num += 1
        print("great job on completing the chore!")
    else:
        print("go and complete it!")

    print(f"chores remaining: {total_chores - completed_chores}")
    print()

print("good job on completing your entire checklist!")


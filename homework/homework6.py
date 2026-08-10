makams_total_homework = 5
Original_homework = makams_total_homework
print(f"good afternoon student\nstudents you have {makams_total_homework} ta homework ase and you have to finish it by tommorow or else you have to meet me in my office.")

completed_hw = 0
hw_num = 1

while hw_num <= makams_total_homework:
    if hw_num == 1:
        next_hw = "Math-d 5a 1-20"
    elif hw_num == 2:
        next_hw = "Math-d 6a 1-20"
    elif hw_num == 3:
            next_hw = "Math-d 7b 1-15"
    elif hw_num == 4:
            next_hw = "Add-math 2.1 1-35"
    elif hw_num == 5:
            next_hw = "Add-math 3.3 1-5"

    answer = input(f"have you completed {next_hw}? [yes|no]: ").lower()
    
    if answer == "yes":
        completed_hw += 1
        hw_num += 1
        print("fine, good")
    else:
        print("tumi ki bashe kichui koro na?, ja, taratari hw ta finish kor!")
    
        print(f"homework remaining: {makams_total_homework - completed_hw}")
        print()
    
    print("bhalo")
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} (Priority: High) - This task requires immediate attention today!")
        else:
            print(f"Reminder: {task} (Priority: High) - Please complete this soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} (Priority: Medium) - This task should be completed by the end of the week.")
        else:
            print(f"Reminder: {task} (Priority: Medium) - Plan to complete this when convenient.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} (Priority: Low) - Complete this when you have free time, but note the deadline.")
        else:
            print(f"Reminder: {task} (Priority: Low) - This can be done at your leisure.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
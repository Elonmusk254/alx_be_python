task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match case for priority
match priority:
    case "high":
        reminder = f"Reminder: {task} (Priority: High)"
        if time_bound == "yes":
            reminder += " - This task requires immediate attention today!"
        else:
            reminder += " - Please complete this soon."
    
    case "medium":
        reminder = f"Reminder: {task} (Priority: Medium)"
        if time_bound == "yes":
            reminder += " - This task should be completed by the end of the week."
        else:
            reminder += " - Plan to complete this when convenient."
    
    case "low":
        reminder = f"Reminder: {task} (Priority: Low)"
        if time_bound == "yes":
            reminder += " - Complete this when you have free time, but note the deadline."
        else:
            reminder += " - This can be done at your leisure."
    
    case _:
        reminder = f"Reminder: {task} - Please set a valid priority (high/medium/low)."

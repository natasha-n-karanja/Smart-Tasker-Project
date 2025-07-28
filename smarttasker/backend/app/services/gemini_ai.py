def suggest_goals(task_history):
    # Dummy example
    return ["Try a 25-min Pomodoro", "Set 3 top priorities for today"]

def interpret_task(description):
    if "Monday" in description:
        return {"tag": "weekly"}
    return {"tag": "daily"}

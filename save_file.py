import os

def save_file(task,value):
    text=f"GeminiAI prompt {task}**************************\n"
    os.path.exists("Manav")
    with open(f"Manav/prompt- {task}","w") as f:
        f.write(value)
    return
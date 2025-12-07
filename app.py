#main script

#add task feature
task = input("Enter a task: ")
with open("tasks.txt", "a") as file:
    file.write(task + "\n")
print("Task added!")

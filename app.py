#Task Manager CLI

#This program manages tasks using CLI

print("Your Tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks:
    print("- "+t.strip())


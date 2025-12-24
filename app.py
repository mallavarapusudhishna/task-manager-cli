#Task Manager CLI App

#This program manages tasks using a CLI

#This is just for practice.

print("Your tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks: 
    print("-"+t.strip())


#Task Manager CLI

<<<<<<< HEAD
#This program manages tasks using a CLI
print("Your tasks: ")
=======
#This program manages tasks using CLI

print("Your Tasks: ")
>>>>>>> 7d91ab70afaa9a6f7c12b9b6702dab118d1947cc
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks:
    print("- "+t.strip())


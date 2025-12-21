#Task Manager CLI App
#Temporary change for stash practice.
#This is just a sample to print tasks
#This program manages tasks using a CLI.
print("Your tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks: 
    print("-"+t.strip())


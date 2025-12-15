#Task Manager CLI App
#this is just an addition.
#this is another addition to this
#
#Temporary change for stash practice.
#This program manages tasks using a CLI.
print("Your tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks: 
    print("-"+t.strip())


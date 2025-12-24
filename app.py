#Task Manager CLI App

#This program manages tasks using a CLI

#This is just for practice.
#thinis balala


#this isvfghjzk
print("Your tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks: 
    print("-"+t.strip())


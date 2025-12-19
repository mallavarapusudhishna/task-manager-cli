#Task Manager CLI App
#Temporary change for stash practice.
#Author: Sudhishna Mallavarapu
#this is sample
#this is sample 2
#
#
#This program manages tasks using a CLI.
print("Your tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks: 
    print("-"+t.strip())


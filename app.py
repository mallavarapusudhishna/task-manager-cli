#Task Manager CLI App

#This program manages tasks using a CLI.
print("Your tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
<<<<<<< HEAD
for t in tasks: 
    print("-"+t.strip())

=======
for t in tasks:
    print("- "+t.strip())
#Author: Sudhishna Mallavarapu
>>>>>>> a091027 (Add Author tag comment)

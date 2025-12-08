#Task Manager CLI

#This program manages tasks using CLI

print("Your Tasks: ")
with open("tasks.txt", "r") as file:
    tasks = file.readlines()
for t in tasks:
    print("- "+t.strip())
>>>>>>> 90ba537304aea526c8ceaf3ae5538634a2dedae8

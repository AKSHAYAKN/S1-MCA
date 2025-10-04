students ={
    "Anu":[85,90,79],"Gowri":[72,88,91],"Vishnu":[95,80,85]
}
for name,marks in students.items():
    total = sum(marks)
    average = sum(marks)/len(marks)
    print(f"Student : {name}")
    print(f"Marks : {marks}")
    print(f"Total Marks : {total}")
    print(f"Average Marks : {average:.2f}")
    print("."*20)


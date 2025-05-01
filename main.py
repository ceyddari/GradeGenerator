import random
import math

def student_list_load(file_name):     
    students = []
    with open(file_name, "r", encoding="windows-1254") as file:
        for line in file:
            name, age = line.strip().split(",")
            students.append({"name": name, "age": int(age)})
    return students


def give_note(students):
    for stu in students:
        stu["notes"]=[random.randint(50,100) for _ in range(3)]
        stu["avarage"]=round(sum(stu["notes"])/len(stu["notes"]),2)

def successfull_students(students):
    return [s for s in students if s["avarage"] >= 70]


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age=age
        self.notes = []

    def add_note(self, *notes):
        self.notes.extend(notes)

    def avarage(self):
        return round(sum(self.notes) / len(self.notes),2)
    
    def __str__(self):
        return f"{self.name} ({self.age} aged) - Avarage: {self.avarage()}"
    
#main
def main():
    file = "students.csv"
    stu_list=student_list_load(file)
    if not stu_list:
        return
    
    give_note(stu_list)

    print("\n All Students: ")
    for idx, stu in enumerate(stu_list, 1):
        print(f"{idx}. {stu['name']} - Age: {stu['age']} - Avarage: {stu['avarage']}")

    print("\n Successfull Students: ")
    for stu in successfull_students(stu_list):
        print(f"{stu['name']} - Avarage: {stu['avarage']}")

    print("\n Ages: ", sorted({s['age'] for s in stu_list}))

main()

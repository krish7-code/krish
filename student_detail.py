import json
import os

file="student_data.json"
def load_detail():
    if not os.path.exists(file):
        return []
    else:
        with open(file,"r") as f:
            return json.load(f)

def add_detail():
    data=load_detail()
    name=input("Enter the name:")
    student_id=int(input("Enter the student id:"))
    number=input("Enter the number:")
    age=int(input("Enter age:"))
    department=input("Enter the department:")
    cg=float(input("Enter the CGPA:"))
    detail=({"Name":name,"S_ID":student_id,"Number":number,"Age":age,"Department":department,"CGPA":cg})
    data.append(detail)
    with open(file,"w") as f:
        json.dump(data,f,indent=4)
    print("Detail added succesfully")
def show_detail():
    data=load_detail()
    for d in data:
        print(f"{d['Name'].center(13)}|{d['S_ID']}|{d['Number'].center(12)}|{d['Age']}|{d['Department'].center(6)}|{d['CGPA']}")

        
def get_detail():
    data = load_detail()
    d = int(input("Enter the student ID:"))
    for i in data:
        if i["S_ID"] == d:
            print("Student detail.")
            print(f"{i['Name']} ==> {i['Number']}")
            break
    else:
        print("Student detail does not exist")


    
def update_detail():
    data=load_detail()
    n=int(input("Enter the student ID:"))
    for d in data:
        if d["S_ID"]==n:
            print("||For update or change the detail||")
            d["Name"]=input("Enter the name :")
            d["number"]=input("Enter the number:")
            d["Age"]=int(input("Age"))
            d["Department"]=input("Enter department:")
            d["CGPA"]=float(input("Enter the CGPA:"))
            with open(file,"w") as f:
                json.dump(data,f,indent=4)
            print("updated....")
            break
        else:
            print("Student ID does not exists !")
    
def remove_detail():
    data=load_detail()
    n=int(input("Enter the student ID:"))
    for i in range(len(data)):
        t_data=data[i]
        if t_data["S_ID"]==n:
            data.pop(i)
            print(f"Student detail is removed")
            break
        else:
            print("Detail does not exists!")
    with open(file,"w") as f:
        json.dump(data,f,indent=4)
    
def main():
    while True:
        print("Add new student ==> 1")
        print("View all student ==> 2")
        print("Search student ==>3")
        print("Update student detail ==>4")
        print("Delete student detail ==>5")
        print("Exit ==>6")
        choice=int(input("Enter the choice :"))
        if choice==1:
            add_detail()
        elif choice==2:
            show_detail()
        elif choice==3:
            get_detail()
        elif choice ==4:
            update_detail()
        elif choice==5:
            remove_detail()
        elif choice==6:
            break
        else:
            print("Ivalid")
main()

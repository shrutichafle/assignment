atendence=75
atend=int(input("enter the number class that atend:"))
total=int(input("enter the total number of class:"))
percentage=(atend/total)*100
if percentage>=atendance:
    print("you are allowed to sit in the exam")
else:
    print("you are not allowed to sit in the exam")
   
person1=int(input("enter the age of person1:"))
person2=int(input("enter the age of person2:"))
person3=int(input("enter the age of person3:"))
person4=int(input("enter the age of person4:"))
person5=int(input("enter the age of person5:"))
if person1<person2 and person1<person3 and person1<person4 and person1<person5:
    print("the youngest person is person1")
elif person2<person1 and person2<person3 and person2<person4 and person2<person5:
    print("the youngest person is person2")
elif person3<person1 and person3<person2 and person3<person4 and person3<person5:
    print("the youngest person is person3")
elif person4<person1 and person4<person2 and person4<person3 and person4<person5:
    print("the youngest person is person4")
elif person5<person1 and person5<person2 and person5<person3 and person5<person4:
    print("the youngest person is person5")
else:
    print("write the different age")
pas=45
obtain=int(input("enter the marks obtain:"))
total=int(input("enter the total marks:"))
percentage=(obtain/total)*100
if percentage>=pas:
    print("you obtain",percentage,"%")
    print("you are pass")
else:
    print("you obtain",percentage,"%")
    print("you are fail")
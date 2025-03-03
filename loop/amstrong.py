num=int(input("enter the number:"))
arm=0
temp=num
l=len(str(num))
while temp>0:
    digit=temp%10
    arm=arm+digit**l
    temp=temp//10
if num==arm:
    print("the number",num,"is armstrong")
else:
    print("the number",num,"is not armstrong")
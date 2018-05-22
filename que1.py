#bmi calculator
n=input("enter user name")
a=float(input("enter your weight in kg"))
b=float(input("enter your hight in meters"))
c=a/b**2
fp=open("F:\\bmi.txt","a+")
fp.write("%s:"%n)
fp.write("%f:"%c)
fp.write("\n")
fp.close
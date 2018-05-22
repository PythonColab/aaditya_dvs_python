def bmi():
	n=input("enter user name")
	a=float(input("enter your weight in kg"))
	b=float(input("enter your hight in meters"))
	c=a/b**2
	fp=open("F:\\bmi.txt","a+")
	fp.write("%s:"%n)
	fp.write("%f:"%c)
	fp.write("\n")
	fp.close
def calculator():
	a=int(input("enter first number"));
	b=int(input("enter second number"));
	c=int(input("enter operation i.e. 1(addition),2(substraction),3(multiplication),4(devision)"));
	if (a and b)==0:
		print("Zero detected....");
			
	else:
		if c==1:
			d=a+b;
			print("answer is:",d);
		elif c==2:
			d=a-b;
			print("answer is:",d);
		elif c==3:
			d=a*b;
			print("answer is:",d);
		elif c==4:
			d=a/b;
			print("answer is:",d);
		else:
			print("invalid entry");
	fp=open("F:\\calc.txt","a+")
	fp.write("%d:"%d)
	fp.write("\n")
	fp.close
def currency():
	fp=open("F:\\curr.txt","r+")
	b=float(fp.read())
	a=int(input("choose the initial currency in which the amount is curretly exist:\n press\n 1) INR(Rupee)\n 2) USD(American doller \n 3) Euro)"))
	if a==1:
		c=int(input("convert INR to\n 1) USD 2) Euro"))
	elif a==2 :
		c=int(input("convert USD to\n 1) INR 2) Euro"))
	elif a==3 :
		c=int(input("convert Euro to\n 1) USD 2) INR"))
	else:
		print("invalid input")
	if a==1 and c==1 :
		d=b/65
		print("USD:",d)
	elif a==1 and c==2 :
		d=b/80
		print("Euro:",d)
	elif a==2 and c==1 :
		d=b*65
		print("INR:",d)
	elif a==2 and c==2 :
		d=b*1.18
		print("Euro:",d)
	elif a==3 and c==1 :
		d=b/1.18
		print("USD:",d)
	elif a==3 and c==2 :
		d=b*80
		print("INR:",d)
	else:
		print("invalid")
	fp.close()
	fp=open("F:\\opcurr.txt","a+")
	fp.write("%d:"%d)
	fp.write("\n")
	fp.close
option=int(input("what type of calculation you want to perform \n1) BMI calculation \n2) Simple Calculator \n3) currency converter"))
if option==1:
	bmi()
elif option==2 :
	calculator()
elif option==3 :
	currency()
else:
	print("invalid input")
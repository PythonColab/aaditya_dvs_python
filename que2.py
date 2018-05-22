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
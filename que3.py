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

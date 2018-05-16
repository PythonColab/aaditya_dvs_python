a=1;
b=1;
while (a!=0 or b!=0):
	list1=[1,2,3,"accha"]
	a=int(input("enter\n 1\t(to add a value) \n 2\t(to remove a value)\n 3\t(to search value)"))
	if a==1:
		b=input("enter value to add")
		list1.append(b)
		print(list1)
	elif a==2:
		b=input("enter value which is to be removed")
		list1.remove(b)
		print(list1)
	elif a==3:
		b=input("enter value to be searched")
		list1.index(b)
		print(list1)
	else:
		print("invalid input")
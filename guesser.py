import random
arr=[]
r=0
l=1
h=int(input("Enter the upper limit"))
inp=''
while inp!='c':
	arr.append(r)
	#print(arr) #debug line
	r=random.randint(l,h)
	if r not in arr:
		inp=input(f"Is {r} the right answer? (l,h or c) ")
		if inp=='l':
			l=r
		elif inp == 'h':
			h=r
		elif inp=='c':
			print("Yes!")

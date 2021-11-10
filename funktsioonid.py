from tsukel import*
while True:
	print("Finktsioonid".center(50,"+"))
	v=input("arithmetic- A, Liigaasta- Y")
	if v.upper()=="A":
		arv1=float(input("Arv 1: "))
		arv2=float(input("Arv 2: "))
		sym=input("Tehe: ")
		rezult=arithmetic(arv1,arv2,sym)
		print(rezult)
	elif v.upper()=="Y":
		print("Kas aasta on liigaasta?")
		leap=is_year_leap(int(input("aasta: ")))
		print(leap)
	elif v.upper()=="S":
		print("square")
		ans=square(float(input("Сторона квадрата: ")))
		print(ans)

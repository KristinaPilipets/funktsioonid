from module1 import*
while True:
	print("Finktsioonid".center(50,"+"))
	v=input("arithmetic- A, Liigaasta- Y, Square- S, Season- SE")
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
	elif v.upper()=="SE":
		month=""
		while month not in [1,2,3,4,5,6,7,8,9,10,11,12]:
			try:
				month=int(input("Sisseta kuu number: "))
			except:
				TypeError
		ans=season(month)
		print(f"Sinu kuu on {ans} aastaaajas ")
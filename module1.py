from math import*
def arithmetic(a: float,b:float,c:str):
	"""lihtne kalkulaator
	+ - liitmine
	- - lahutamine
	* - korrutamine
	/ - jagamine
	:param float a: esimine arv
	:param float b: Teine arv
	:param str c: aritmeetiline tehing
	:rtype float:
	"""
	if c=="+":
		r=a+b
	elif c=="-":
		r=a-b
	elif c=="*":
		r=a*b
	elif c=="/":
		if b!=0:
			r=a/b
		else:
			print("Div0")
	else:
		print("Неизвестная операция")
	return r
def is_year_leap(aasta:int):
	"""Liigaasta
	Tagastab trui kui aasta on liigaasta ja false kui ei ole
	:param int aasta: Aasta number
	:rtype bool: Funktioni vastus loogilises formaadis
	"""
	l=aasta%4
	if l==0:
		ans=("True")
	else:
		ans=("False")
	return ans
def square(side:float):
	"""Square
	tagastab resultadi
	:param float side: side length
	:rtype str:
	"""
	P=side*4
	S=side**2
	D=sqrt(2*side**2)
	ans=(f"P={P}; S={S}; D="+str(round(D,2)))
	return ans
def season(a:int):
	if a==1 or a==2 or a==12:
		ans="talv"
	elif a==3 or a==4 or a==5:
		ans="kevad"
	elif a==6 or a==7 or a== 8:
		ans="suve"
	else:
		ans=="sügis"
	return ans
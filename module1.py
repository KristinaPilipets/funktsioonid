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
			r=("Div0")
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
	"""aastaaeg
	tagastab mis aastaaeg kuu on
	:param int a: kuu
	:rtype str:
	"""
	if a==1 or a==2 or a==12:
		ans="talv"
	elif a==3 or a==4 or a==5:
		ans="kevad"
	elif a==6 or a==7 or a== 8:
		ans="suve"
	else:
		ans=="sügis"
	return ans
def bank(a:float,b:int)->float:
	for i in range (1,b+1):
		e=a*0.10
		d=a+e
	return d
def is_prime(a:int):
	"""
	tagastab resultadi
	:param int a: esimine arv
	:rtyoe bool:
	"""
	if a!=2 or a!=3:
		if a%2==0:
			ans="False"
		else:
			if a%3==0:
				ans="False"
			else:
				ans="True"
	else:
		if a%5==0:
			ans="False"
		else:
			ans="True"
	return ans
def date(a:int,b:int,c:int):
	"""kas see on õige
	tagastab bool
	:param int a: paev
	:param int b: kuu
	:param int c: aasta
	:rtype bool:
	"""
	if ((b==1 or b>=1) and (b<=12 or b==12)) and ((a==1 or a>=1) and (a==31 or a<=31)) and c>=0:
		if b==2 and a<=30:
			if c%4==0 and a==29:
				ans="True"
			else:
				ans="False"
		elif (b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12) and (a==31 or a<=31):
			ans="True"
		else:
			ans="False"
	return ans
def XOR_cipher(string:str,key:str):
	"""tavaline sõna kodeeritakse
	:param str a: tekst
	:param b: võti
	:rtype str:
	"""
	result=""
	temp=int()
	for i in range(len(string)):#определяем кол-во символов
		temp = ord(string[i])#näitab sümboli kood
		for j in range (len(key)):
			temp ^= ord(key[j])#начинаем кодировать текст
		result +=chr(temp)#ставим кодированнный текст как результат чтобы запомнить его
	return result
def XOR_uncipher(string:str,key:str)->str:
	"""Kodeeritud text dekodeeritakse
	"""
	result=""
	temp=[]
	for i in range(len(string)):#определяем кол-во символов
		temp.append(string[i])
		for j in reversed(range(len(key))):#в обратном порядке ставим буквы
			temp[i]=chr(ord(key[j])^ord(temp[i]))
		result+=temp[i]
	return result
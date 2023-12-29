
## convert
def btd(n):
	h = 0
	for y in range(len(n)):
		print(n[y]+' × '+str(2**(len(n)-1-y)))
		h+=int(n[y])*(2**(len(n)-1-y))
	print('\n')
	return str(h)
	
def dtb(n):
	b = ''
	nc=int(n)
	while True:
		b+=str((nc%2))
		nc=nc//2
		print(str(nc))
		if(nc<1):
			break
	print(b)
	print('\n')
	return b[::-1]
	
	
	########### logic gate
def notg(f):
	if(f=='1'):
		return '0'
	else:
		return '1'

def andg(f,s):
	if(f=='1'):
		if(s=='1'):
			return '1'
		else:
			return '0'
	else:
		return '0'
		
def nandg(f,s):
		return notg(andg(f,s))
		
def org(f,s):
	return nandg(notg(f),notg(s))

def xorg(f,s):
	return andg(org(f,s),nandg(f,s))		
		
		############# diagram
def hadder(a,b):
		
		x1 = xorg(a,b)
		
		a1 = andg(a,b)
		
		return x1,a1
		
def fadder(a,b,ci):
	
	x1 = xorg(a,b)
	
	sum = xorg(x1,ci)
	
	a1 = andg(ci,x1)
	
	a2 = andg(a,b)
	
	co = org(a1,a2)

	return sum,co
	
	###########
def abit(f,s):
	letn = 0
	n=f
	k=s
	a=''
	b=''
	x=''
	co=''
	if(len(n)>len(k)):
		letn=len(n)
	else:
		letn=len(k)
	for i in range(letn):
		shk=''
		shkl=''
		if(i<len(n)):
			shk = n[-(i+1)]
		else:
			shk='0'
		if(i<len(k)):
			shkl = k[-(i+1)]
		else:
			shkl='0'
		
		if(i<1):
			ha=hadder(shk,shkl)
			x+=ha[0]
			co=ha[1]
			print(shk+' + '+shkl+' = ',ha[0])
		else:
			v = fadder(shk,shkl,co)
			x+=v[0]
			co=v[1]
			print(shk+' + '+shkl+' = ',v[0])
	print('-> co = ',co)
	x+=co
	print(x[::-1]+'\n')
	return x[::-1]
	
f = input(' first -------->  ')
s = input(' second -------->  ')
a1 = dtb(f)
a2 = dtb(s)
ab1 = abit(a1,a2)
print('---> ',btd(ab1))


password = 'a123456'
i = 3
while i > 0:
	i = i -1
	pw = input('enter your password: ')
	if pw == password:
		print('login successfully')
		break
	else:
		print('password incorrect! you still have' , i, 'chances')

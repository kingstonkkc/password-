password = 'a123456'
i = 3
while i > 0:
	i = i -1
	pw = input('enter your password: ')
	if pw == password:
		print('login successfully')
		break
	else:
		print('password incorrect!')
		if i > 0:
			print('you still have' , i, 'chances')
		else:
			print('no more chances. account will be locked')

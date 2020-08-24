password = 'a123456'
i = 3
while True:
	pw = input('enter your password: ')
	if pw == password:
		print('login successfully')
		break
	else:
		i = i - 1
		print('password incorrect! you still have' , i, 'chances')
		if i == 0:
			print('login failed')
			break
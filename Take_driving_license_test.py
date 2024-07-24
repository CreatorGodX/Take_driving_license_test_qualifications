#Take_driving_license_test




country = input('Which country are you from? (Taiwan / America) : ')
if country != 'Taiwan' and country != 'America':
	print('You can only enter Taiwan or America')
  
age = input('How old are you? : ')

age = int(age)

if country == 'Taiwan':
    if age >= 18:
        print('You can take a driving license test')
    else:
    	print("You can't take a driving license test")
elif country == 'America':
	if age >= 16:
		print('You can take a driving license test')
	else:
	    print("You can't take a driving license test")

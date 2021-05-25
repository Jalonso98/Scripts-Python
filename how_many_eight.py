cont =0
for i in range(1,101):
	if '88' == str(i):
		print(f'{cont}+2 = {(cont+2)} [{i}]')
		cont+=2
	elif '8' in str(i):
		print(f'{cont}+1 = {(cont+1)} [{i}]')
		cont+=1
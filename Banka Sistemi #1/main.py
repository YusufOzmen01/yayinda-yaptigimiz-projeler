import json
import random
import os
db = {}

def update():
	os.remove('db.json')
	open('db.json','w').write(json.dumps(db))

try:
	open('db.json','x')
except:
	pass

if open('db.json','r').read() == '':
	open('db.json','w').write('{}')
else:
	try:
		db = json.loads(open('db.json','r').read())
	except:
		pass
while (True):
	while (True):
		while (True):
			a = input('Giriş - Kayıt - Çıkış?? (g,k,e) : ')
			if a != 'g' and a != 'k' and a != 'e':
				print('Yanlış seçenek.\n')
			else:
				break
		if a == 'k':
			uid = random.randint(100000,999999)
			password = input('Şifre giriniz : ')
			print('IDniz {} - şifreniz {}'.format(uid,password))
			db.update({uid:{"password":password,"balance":10000}})
			update()
		elif a == 'g':
			uid = input('ID? : ')
			password = input('Şifre? : ')
			if db[uid] == None:
				print('Hatalı giriş.')
			else:
				if db[uid]["password"] != password:
					print('Hatalı giriş.')
				else:
					while (True):
						b = input('=====YUSFU BANKASINA HOŞGELDİNİZ=====\n\nBakiyeniz : {}\n\nİşlemler =>\nPara Gönder (p)\nÇıkış Yap (e)\n\nSeçim? :'.format(db[uid]["balance"]))
						if b != 'p' and b != 'e':
							print('Yanlış seçenek.\n')
						else:
							if b == 'p':
								while (True):
									c = input('ID? : ')
									if db[c] == None:
										print('Böyle bir ID bulunamadı!')
									else:
										d = int(input('Miktar? : '))
										if int(db[uid]["balance"]) < d:
											print('Bakiye yetersiz.')
										else:
											tmp = int(db[uid]["balance"])
											tmp = tmp - d
											db[uid]["balance"] = tmp
											tmp = int(db[c]["balance"])
											tmp = tmp + d
											db[c]["balance"] = tmp
											update()
											print('{} lira gönderildi! Kalan bakiye {}'.format(d,db[uid]["balance"]))
											break
							else:
								break
		else:
			break
	break
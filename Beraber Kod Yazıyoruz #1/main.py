import random
import os
def update(haritaa):
	out = ""
	indexx = 0
	for i in range(64):
		if indexx / 8 >= 1:
			out = out + "\n"
			indexx = 0
		if haritaa[i] == 0:
			out = out + "█"
		elif haritaa[i] == 1:
			out = out + "@"
		elif haritaa[i] == 2:
			out = out + "©"
		indexx = indexx + 1
	print(out)
	out = ""
harita = []
score = 0
characterPos = random.randint(1,62)
applePos = random.randint(1,62)

for i in range(64):
	harita.append(empty)

harita[characterPos] = 1
harita[applePos] = 2
isPrinted = False
while (score < 20):
	os.system('cls')
	if isPrinted == False:
		print('Sen @ işaretisin. Amacın © işaretini yemek. 20 kez yersen kazanırsın. Bol şans!\n')
		isPrinted = True
	update(harita)
	inp = input('Skor : {} - Yön? (w,a,s,d) : '.format(score))
	if inp == 'w':
		harita[characterPos] = 0
		if characterPos < 8:
			characterPos = characterPos + 56
		else:
			characterPos = characterPos - 8
		harita[characterPos] = 1
	elif inp == 's':
		harita[characterPos] = 0
		if characterPos > 56:
			characterPos = characterPos - 56
		else:
			characterPos = characterPos + 8
		harita[characterPos] = 1
	elif inp == 'a':
		harita[characterPos] = 0
		if characterPos % 8 == 0:
			characterPos = characterPos + 7
		else:
			characterPos = characterPos - 1
		harita[characterPos] = 1
	elif inp == 'd':
		harita[characterPos] = 0
		if (characterPos + 1) % 8 == 0:
			characterPos = characterPos - 7
		else:
			characterPos = characterPos + 1
		harita[characterPos] = 1

	if characterPos == applePos:
		score = score + 1
		harita[applePos] = 0
		applePos = random.randint(1,62)
		harita[applePos] = 2
		harita[characterPos] = 1
print('Oyun bitti! Tebikler!')
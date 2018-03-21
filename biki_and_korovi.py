import os
import random

def randomNum():
	numOne = random.randint(0, 9)
	numTwo = random.randint(0, 9)
	while(numTwo == numOne):
		numTwo = random.randint(0, 9)
	numThree = random.randint(0, 9)
	while(numThree == numOne or numThree == numTwo):
		numThree = random.randint(0, 9)
	numFour = random.randint(0, 9)
	while(numFour == numOne or numFour == numTwo or numFour == numThree):
		numFour = random.randint(0, 9)
	sumNum = str(numOne) + str(numTwo) + str(numThree) + str(numFour)
	return sumNum

def main():
	os.system('cls')
	print('Быки и коровы', end = '\n\n')
	print('Правила игры:')
	print('Компьютер задумывает четыре различные цифры из 0,1,2,...9. У игрока 10 ходов, чтобы узнать эти цифры и их порядок.')
	print('Каждый ход состоит из четырёх цифр, 0 может стоять на первом месте. В ответ компьютер показывает число отгаданных цифр,')
	print('стоящих на своих местах (число быков) и число отгаданных цифр, стоящих не на своих местах (число коров).', end='\n\n')
	print('Компьютер уже что-то задумал. Играем!')
	temporary = input()
	del temporary
	os.system('cls')
	numComputer = randomNum()
	print('Число загадано! Попробуй его отгадать!', numComputer, end = '\n\n')
	i = 0
	while(i < 10): #10 попыток
		cow = bull = 0
		numUser = input()
		if(numUser.isdigit() == True and len(numUser) == 4):
			for j in range(4):
				if(numUser[j] == numComputer[j]):
					cow += 1
			for k in range(4):
				if(numUser[k] == numComputer[0] or numUser[k] == numComputer[1] or numUser[k] == numComputer[2] or numUser[k] == numComputer[3]):
					bull += 1		
			print('Коров -', cow, 'Быков - ', bull)
			i += 1
			if(numUser == numComputer):
				print('\nТы победил! Поздравляю!')
				quit()
		else:				
			print('Некорректный ввод, попытка не засчитана!')
	print('\nТы проиграл, загаданное число было -', numComputer, end = '\n\n')
main()	
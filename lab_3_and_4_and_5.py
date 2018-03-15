import os
import time
import getpass

def entry(): #вход
	os.system('cls')
	fileLogin = open('login.txt', 'r') #открытие файла с логинами для чтения
	filePass = open('password.txt', 'r') #открытие файла с паролями для чтения
	fileRole = open('role.txt', 'r') #открытие файла с ролями для чтения
	baseLogin = fileLogin.read() #запись логинов в строку
	basePass = filePass.read() #запись паролей в строку
	baseRole = fileRole.read() #запись ролей в строку
	login = input('Логин: ') #ввод логина
	if baseLogin.find(login) == -1: #пользователь не сущ-ет
		print('Такого пользователя не существует.')
		time.sleep(2)
		return entry()
	elif baseLogin.find(login) != -1: #пользователь сущ-ет
		baseLogin = baseLogin.split() #строка с логинами в список
		basePass = basePass.split() #строка с паролями в список
		baseRole = baseRole.split() #строка с ролями в список
		id = baseLogin.index(login) #место нахождения логина
		password = getpass.getpass(prompt = 'Пароль: ') #ввод пароля
		if basePass[id] != password: #неверный пароль
			print('Неверный пароль.')
			time.sleep(1)
			return entry()
		elif basePass[id] == password: #верный пароль
			fileLogin.close()
			filePass.close()
			fileRole.close()
			return id	 	
	else:
		print('Error!')		
def registration(): #регестрация
	os.system('cls')
	login = input('Логин: ') 
	fileLogin = open('login.txt', 'r+') #открытие файла login.txt для чтения
	baseLogin = fileLogin.read() #чтение содержимого файла в baseLogin
	if baseLogin.find(login) != -1: #если логин занят
		print('Логин занят.') 
		time.sleep(1)
		return registration() 
	elif baseLogin.find(login) == -1: #если логин не занят
		login = login + ' ' #добавление пробела в конец логина
		fileLogin.write(login) #запись логина в файл
		fileLogin.close() #закрытие файла
		password = getpass.getpass(prompt = 'Пароль: ') #ввод пароля
		filePass = open('password.txt', 'a') #открытие файла password.txt для добавления
		password = password + ' ' #добавление пробела в конец пароля
		filePass.write(password) #запись пароля в файл
		filePass.close() #закрытие файла
		fileRole = open('role.txt', 'a') #открытие файла role.txt для добавления
		fileRole.write('user ') #запись роли в файл
		fileRole.close() #закрытие файла 
		print('Регестрация прошла успешно!')
		time.sleep(1)
	else:
		print('Error!')		
def user(id): #пользователь
	os.system('cls')
	print('Hello User!')
	print('1.Изменить свой логин.')
	print('2.Изменить свой пароль.')
	print('3.Выход из учетной записи.')
	print('0.Выход из программы.')
	x = input('Ввод: ')
	if x == '1': #изменить свой логин
		changeYourLogin(id)
		user(id)
	elif x == '2': #изменить свой пароль
		changeYourPass(id)
		user(id)	
	elif x == '3': #выход из учетной записи
		main()	
	elif x == '0': #выход из программы
		os.system('cls')
		quit()
	else:
		print('Error')
def admin(id): #админ
	os.system('cls')
	print('Hello Admin!')
	print('1.Посмотреть список пользователей.')
	print('2.Изменить роль пользователя.')
	print('3.Сбросить пароль пользователя.')
	print('4.Изменить свой логин.')
	print('5.Изменить свой пароль.')
	print('6.Выход из учетной записи.')
	print('0.Выход из программы.')
	x = input('Ввод: ')
	if x == '1': #посмотреть список пользователей
		viewUsers()
		admin(id)
	elif x == '2': #изменить роль пользователя
		changeUserRole()
		admin(id)
	elif x == '3': #сбросить пароль пользователя
		resetUserPassword()
		admin(id)
	elif x == '4': #изменить свой логин
		changeYourLogin(id)
		admin(id)
	elif x == '5': #изменить свой пароль
		changeYourPass(id)
		admin(id) 			
	elif x == '6': #выход из учетной записи
		main()	
	elif x == '0': #выход из программы
		os.system('cls')
		quit()
	else:
		print('Error')
def changeYourLogin(id): #изменить свой логин
	os.system('cls')
	fileLogin = open('login.txt', 'r') #открытие файла с логинами для чтения
	baseLogin = fileLogin.read() #запись логинов в строку
	baseLogin = baseLogin.split() #строка с логинами в список
	loginOld = baseLogin[id] #старый логин
	loginNew = input('Введите новый логин: ') #новый логин
	baseLogin = ' '.join(baseLogin) #лист в строку с пробелами между логинами
	baseLogin = baseLogin.replace(loginOld, loginNew) #замена в строке старого логина на новый
	baseLogin = baseLogin + ' ' #добавление в конец строки пробела
	fileLogin.close() #закрытие файла
	fileLogin = open('login.txt', 'w') #открытие файла с логинами для перезаписи
	fileLogin.write(baseLogin) #запись новой базы вместо старой
	fileLogin.close() #закрытие файла
	print('Логин успешно изменен.')
	time.sleep(1)
def changeYourPass(id): #изменить свой пароль
	os.system('cls')
	filePass = open('password.txt', 'r') #открытие файла с паролями для чтения
	basePass = filePass.read() #запись паролей в строку
	basePass = basePass.split() #строка с паролями в список
	PassOld = basePass[id] #старый пароль
	PassNew = getpass.getpass(prompt = 'Введите новый пароль: ') #новый пароль
	basePass = ' '.join(basePass) #лист в строку с пробелами между паролями
	basePass = basePass.replace(PassOld, PassNew) #замена в строке старого пароля на новый
	basePass = basePass + ' ' #добавление в конец строки пробела
	filePass.close() #закрытие файла
	filePass = open('password.txt', 'w') #открытие файла с паролями для перезаписи
	filePass.write(basePass) #запись новой базы вместо старой
	filePass.close() #закрытие файла
	print('Пароль успешно изменен.')
	time.sleep(1)		
def viewUsers(): #посмотреть список всех пользователей
	os.system('cls')
	fileLogin = open('login.txt', 'r') #открытие файла с логинами для чтения
	baseLogin = fileLogin.read() #запись логинов в строку
	baseLogin = baseLogin.split() #строка с логинами в список
	baseLogin = '\n'.join(baseLogin) #лист в строку с переводом на новую строку между логинами
	fileLogin.close() #закрытие файла
	print(baseLogin)
	sleep = input()
def changeUserRole(): #изменить роль пользователя
	os.system('cls')
	fileLogin = open('login.txt', 'r') #открытие файла с логинами для чтения
	fileRole = open('role.txt', 'r') #открытие файла с ролями для чтения
	baseLogin = fileLogin.read() #запись логинов в строку
	baseRole = fileRole.read() #запись ролей в строку
	login = input('Введите логин пользователья, чью роль вы хотите изменить: ') #ввод логина пользователя
	if baseLogin.find(login) == -1: #пользователь не сущ-ет
		print('Такого пользователя не существует.')
		time.sleep(2)
		return changeUserRole()
	elif baseLogin.find(login) != -1: #пользователь сущ-ет
		baseLogin = baseLogin.split() #строка с логинами в список
		baseRole = baseRole.split() #строка с ролями в список
		id = baseLogin.index(login) #место нахождения логина
		newRole = input('Введите роль(user/admin): ') #ввод новой роли
		if newRole != 'user' and 'admin':
			print('Неккоректный ввод!')
			time.sleep(1)
			return changeUserRole()
		baseRole.insert(id, newRole) #вставка новой роли для пользователя со свдигом остальных
		baseRole.pop(id+1) #уделение последующего(т.к. был сдвиг), со свдигом назад
		baseRole = ' '.join(baseRole) #список в строку с пробелами между ролями
		baseRole = baseRole + ' ' #добавление к концу пробела
		fileRole.close() #закрытие файла с ролями
		fileRole = open('role.txt', 'w') #открытие файла с ролями для перезаписи
		fileRole.write(baseRole) #перезапись
		fileRole.close() #закрытие файлов
		fileLogin.close()
		print('Роль успешно изменена.')
		time.sleep(2)
	else:
		print('Error!')
def resetUserPassword(): #сброс пароля пользователя
	os.system('cls')
	fileLogin = open('login.txt', 'r') #открытие файла с логинами для чтения
	filePass = open('password.txt', 'r') #открытие файла с паролями для чтения
	baseLogin = fileLogin.read() #запись логинов в строку
	basePass = filePass.read() #запись паролей в строку
	login = input('Введите логин пользователя, чей пароль вы хотите сбросить: ') #ввод логина
	if baseLogin.find(login) == -1: #пользователь не сущ-ет
		print('Такого пользователя не существует.')
		time.sleep(2)
		return resetUserPassword()
	elif baseLogin.find(login) != -1: #пользователь сущ-ет
		baseLogin = baseLogin.split() #строка с логинами в список
		basePass = basePass.split() #строка с паролями в список
		id = baseLogin.index(login) #место нахождения логина
		basePass.insert(id, 'qwerty') #вставка стандартного пароля, со сдвигом остальных
		basePass.pop(id+1) #удаление старого пароля со сдвигом назад
		basePass = ' '.join(basePass) #лист в строку с пробелами между паролями
		basePass = basePass + ' ' #вставка пробела в конец 
		filePass.close() #закрытие файла
		filePass = open('password.txt', 'w') #открытие файла с паролями для перезаписи
		filePass.write(basePass) #перезапись на новую базу с паролями
		filePass.close() #закрытие файлов
		fileLogin.close()
		print('Пароль успешно сброшен на стандартный')
		time.sleep(2)
	else:
		print('Error!')					
	
def main():
	os.system('cls')
	print('1.Войти.')
	print('2.Зарегестрироваться.')
	print('0.Выход из программы.')
	x = input('Ввод: ')
	if x == '1': #вход
		id = entry() #ид пользователя
		fileRole = open('role.txt', 'r') #открытие файла с ролями для чтения
		baseRole = fileRole.read() #запись ролей в строку
		baseRole = baseRole.split() #строка с ролями в список
		if baseRole[id] == 'user': #если роль user
			user(id)
		elif baseRole[id] == 'admin': #если роль admin
			admin(id)
		else:
			print('Error!')		
	elif x == '2': #регестрация
		registration()
		main()
	elif x == '0': #выход
		os.system('cls')
		quit()	
	else:
		print('Некорректный ввод.')	

main()
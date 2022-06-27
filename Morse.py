from pynput.keyboard import Key, Listener
from colorama import Fore, Style
import winsound as ws
import random, time, os

def Clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def Command(msg):
    msg = Brg + Fore.BLUE + '[ → ] ' + Rst + msg + Rst
    return msg

def Message(msg):
    msg = Brg + Fore.CYAN + '[ # ] ' + Rst + random.choice(Colours) + msg + Rst
    print(msg)

def Logo():
    logo = '''
    ███      ███   ██████   ████████    ██████  █████████
    ████    ████  ██▒▒▒▒██  ██▒▒▒▒▒██  ██▒▒▒▒▒  ██▒▒▒▒▒▒▒
    ██▒██  ██▒██  ██    ██  ██     ██  ██       ██
    ██ ▒▒██▒▒ ██  ██    ██  ████████▒  ▒█████   ██████
    ██   ▒▒   ██  ██    ██  ██▒▒▒██▒    ▒▒▒▒██  ██▒▒▒▒
    ██        ██  ██    ██  ██   ▒██        ██  ██
    ██        ██  ▒██████▒  ██    ▒██  ██████▒  █████████
    ▒▒        ▒▒   ▒▒▒▒▒▒   ▒▒     ▒▒  ▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒'''
    Clear()
    print(random.choice(Colours) + logo + Rst + '\n')
    print(Brg + Fore.GREEN + '[ ✔ ] ' + Rst + random.choice(Colours) + 'Created by Bhavesh Kale\n' + Rst)

def Trainer_Decode(sym):
    if sym in list(Morse.values()):
        char = list(Morse.keys())[list(Morse.values()).index(sym)]
        char = Brg + Fore.GREEN + char + Rst
    else: char = Brg + Fore.RED + '?' + Rst
    return char

def Tester_Decode(sym, char):
    global Right, Wrong
    if sym in list(Morse.values()):
        ch = list(Morse.keys())[list(Morse.values()).index(sym)]
        if char.upper() == ch.upper():
            ch = Brg + Fore.GREEN + ch + Rst
            Right += 1
        else:
            ch = Brg + Fore.RED + ch + Rst
            Wrong += 1
    else:
        ch = Brg + Fore.RED + '?' + Rst
        Wrong += 1
    return ch

def Trainer_Press(key):
    global Pressed, Not_Pressed, Next, Pre_Str, word, sym, sen1, sen2, sen3, sen4

    if key == Key.down and Next == True:
        char = Trainer_Decode(sym)
        word += char
        sen4 = sen3; sen3 = sen2; sen2 = sen1; sen1 = word + '\n'
        word = sym = ''
        Logo()
        Message('Morse code Trainer')
        Message('For exit press "ESC"')
        Message('For next line press "DOWN"\n')
        print(sen4 + sen3 + sen2 + sen1 + word, end = '')
        Not_Pressed = True
        Next = False

    if key == Key.space:
        Release = 0
        if Not_Pressed == False:
            Rel_End = time.time()
            Release = round((Rel_End - Rel_Str) * 1000)
        if Pressed == False:
            Pre_Str = time.time() 
            if Release >= 3 * u_delay:
                char = Trainer_Decode(sym)
                sym = ''
                if char != '':
                    Logo()
                    Message('Morse code Trainer')
                    Message('For exit press "ESC"')
                    Message('For next line press "DOWN"\n')
                    print(sen4 + sen3 + sen2 + sen1 + word + char, end = '', flush = True)
                    word += char
                if Release >= 18 * u_delay:
                    Logo()
                    Message('Morse code Trainer')
                    Message('For exit press "ESC"')
                    Message('For next line press "DOWN"\n')
                    print(sen4 + sen3 + sen2 + sen1 + word + ' ', end = '', flush = True)
                    word += ' '
            Pressed = True

def Tester_Press(key):
    global Pressed, Not_Pressed, Next, Pre_Str, word, sym, Test, Right, Wrong, Letter, String
    Length = len(String)
    if key == Key.right and Next == True:
        word = sym = ''
        Right = Wrong = Letter = 0
        Not_Pressed = True
        Test += 1
        if Test >= 5: Test = 0
        if Test == 0: String ='HELLOHOWAREYOUIAMFINE'
        if Test == 1: String ='QOYXZPRRVSBKSEWDHALTD'
        if Test == 2: String ='93FS4B05BF3ZZ75BVD287'
        if Test == 3: String ='QWCX472-VHVU/DFJCS57B'
        if Test == 4: String ='#H%DF38*CIDT793G=353J'
        Logo()
        Message('Morse code Trainer')
        Message('For exit press "ESC"')
        Message('For next test press "RIGHT"\n')
        print(String)
        Next = False

    if Letter < Length and key == Key.space:
        Release = 0
        if Not_Pressed == False:
            Rel_End = time.time()
            Release = round((Rel_End - Rel_Str) * 1000)
        if Pressed == False:
            Pre_Str = time.time() 
            if Release >= 3 * u_delay:
                char = Tester_Decode(sym, String[Letter])
                Letter += 1
                sym = ''
                if char != '':
                    Logo()
                    Message('Morse code Tester')
                    Message('For exit press "ESC"')
                    Message('For next test press "RIGHT"\n')
                    print(String)
                    print(word + char, end = '', flush = True)
                    word += char
                if Letter >= Length:
                    print('\n\nCorrect = %d / %d      Percentage = %.1f%%' %(Right, Length, (Right * 100 / Length)))
                    print('Wrong = %d / %d      Percentage = %.1f%%' %(Wrong, Length, (Wrong * 100 / Length)))
            Pressed = True

def Release(key):
    global Pressed, Not_Pressed, Next, Rel_Str, sym
    Next = True
    if key == Key.esc:
        return False
    if key == Key.space:
        Pre_End = time.time()
        Rel_Str = time.time()
        Press = round((Pre_End - Pre_Str) * 1000)
        if Press >= u_delay:
            if Press >= 3 * u_delay:
                sym += '-'
                print('-', end = '', flush = True)
            else:
                sym += '.'
                print('.', end = '', flush = True)
        Pressed = False
        Not_Pressed = False

def Trainer():
    Logo()
    Message('Morse code Trainer')
    Message('For exit press "ESC"')
    Message('For next line press "DOWN"\n')
    with Listener(on_press = Trainer_Press, on_release = Release) as listener:
        listener.join()
    print()

def Morse_to_Character():
    Logo()
    Message('Morse to character')
    Message('Every letter code is saperated by " "')
    Message('For spacing the words use "|"\n')

    code = input(Command('Enter your message code in "." & "-" : '))
    lst = code.split(' ')
    print('\n' + code + ' = ', end = '', flush = True)
    for letter in lst:
        if letter in list(Morse.values()):
            value = list(Morse.keys())[list(Morse.values()).index(letter)]
            value = Brg + Fore.GREEN + value + Rst
        else:
            value = Brg + Fore.RED + '?' + Rst
        
        ws.Beep(2500, 250); time.sleep(0.25); print(value, end = '', flush = True)
    print()

def Character_to_Morse():
    Logo()
    Message('Character to Morse\n')

    code = input(Command('Enter your message in characters : '))
    print('\n' + code + ' = ', end = '', flush = True)
    for letter in code:
        if letter.upper() in list(Morse.keys()):
            value = list(Morse.values())[list(Morse.keys()).index(letter.upper())]
        else:
            value = '?'
        for val in value:
            if val == '.':
                ws.Beep(2500, 250)
                time.sleep(0.25)
                print(val, end = '', flush = True)
            elif val == '-':
                ws.Beep(2500, 750)
                time.sleep(0.75)
                print(val, end = '', flush = True)
            elif val == '|':
                time.sleep(1.75)
                print(val, end = '', flush = True)
            else:
                ws.Beep(2500, 1750)
                time.sleep(1.75)
                print(val, end = '', flush = True)

        time.sleep(0.25)
        print(' ', end = '', flush = True)
    print()

def Tester():
    Logo()
    Message('Morse code Tester')
    Message('For exit press "ESC"')
    Message('For next test press "RIGHT"\n')
    print(String)
    with Listener(on_press = Tester_Press, on_release = Release) as listener:
        listener.join()
    print()

def Exit():
    print('Have a nice day\n')

Colours = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
Rst = Style.RESET_ALL
Brg = Style.BRIGHT
Not_Pressed = True
Pressed = False
Next = True
u_delay = 75
Right = Wrong = Test = Letter = 0
word = sym = sen1 = sen2 = sen3 = sen4 = ''
String ='HELLOHOWAREYOUIAMFINE'

Morse = {'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....',
         'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.',
         'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-',
         'Y' : '-.--', 'Z' : '--..', '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....',
         '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.', '0' : '-----', '.' : '.-.-.-', ',' : '--..--',
         '?' : '..--..', '!' : '-.-.--', "'" : '.----.', '"' : '.-..-.', '(' : '-.--.', ')' : '-.--.-', '&' : '.-..',
         ':' : '---...', ';' : '-.-.-.', '/' : '-..-.', '_' : '..--.-', '=' : '-...-', '+' : '.-.-.', '-' : '-....-',
         '$' : '...-..-', '@' : '.--.-.', ' ' : '|'}

if __name__ == '__main__':
    choice = ''
    Choices = {'1' : 'Trainer',
               '2' : 'Character to Morse',
               '3' : 'Morse to Character',
               '4' : 'Tester',
               '5' : 'Exit'}
    while choice not in Choices:
        Logo()
        Message('Available Options :')
        for key, value in Choices.items():
            print('[ {key} ] {value}'.format(key = key, value = value))
        print()
        choice = input(Command('Enter Your Choice : '))
        if choice == '1': Trainer()
        elif choice == '2': Character_to_Morse()
        elif choice == '3': Morse_to_Character()
        elif choice == '4': Tester()
        elif choice == '5': Exit()
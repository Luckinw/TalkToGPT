from chatgpt import talkgpt
import pyinputplus as pypl

while True:
    user = pypl.inputStr(prompt='Write Text... ')
    print(talkgpt(user))
    cont = pypl.inputYesNo(prompt='Have another question? ')
    if cont == 'no' : break

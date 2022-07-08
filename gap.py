#import pyttsx3

#pyttsx3.speak('Hi, Ozodbek')

from pyttsx3 import * 

while True:
	text = input('> ')
	speak(text)
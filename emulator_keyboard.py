Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... import serial
... from pynput.keyboard import Controller
... 
... # Initialize serial communication and keyboard controller
... ser = serial.Serial('COM4', 9600)
... 
... keyboard = Controller()
... 
... while True:
...     if ser.in_waiting > 0:
...         line = ser.readline().decode('utf-8').strip()
...         if line == "BUTTON":
...             keyboard.press('a')

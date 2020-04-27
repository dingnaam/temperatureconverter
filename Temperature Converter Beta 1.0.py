import math

def cToF():
    global f
    f = int(input("Input temperature in celcius: "))
    ans_c = f * 9 / 5 + 32
    print(ans_c)

def fToC():
    global c
    c = int(input("Input temeperature in fahrenheit: "))
    ans_f = (c - 32) *5 / 9
    print(ans_f)
    
unit = str(input("Convert from Fahrenheit to Celcius (C) or from Celcius to Fahrenheit (F): "))
if (unit == "C"):
    fToC()
elif (unit == "F"):
    cToF()
else:
    print("Please type \"F\" or \"C\" to calculate")
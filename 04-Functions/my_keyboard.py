###
# Functions to read any data type from the keyboard
#
def input_string(message):
    tekst = input(message)
    return tekst

def input_integer(message):
    liczba_zaokr = input(message)
    return liczba_zaokr

def input_real(message):
    liczba_całk = input(message)
    return liczba_całk

def input_boolean(message):
    logiczna = input(message)
    return logiczna == "y"
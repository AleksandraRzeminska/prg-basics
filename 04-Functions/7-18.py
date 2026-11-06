##
#A sentence is an ordered group of words 
# separated by spaces. 
# Define a function f(sentence) 
# that returns a sentence with spaces removed.

def f(sentence):
    spacja = sentence.replace(" ","")
    return spacja

if __name__ == '__main__':
    print(f("integrated development environment"))
    print(f("A programming language is a system of notation for writing computer programs"))
###
#A device in a door registers people entering 
# and leaving a room.
# The + sign means a person entering a room 
# and the -- sign a person leaving a room. 
# Define the function f(detector) that returns True 
# if at least 3 people were in the room at the same time, 
# or False otherwise.

def f(detector):
    current_people = 0
    
    for symbol in detector:
        if symbol == '+':
            current_people += 1
        elif symbol == '-':
            current_people -= 1
            
        # Check if at any moment 3 or more people were in the room
        if current_people >= 3:
            return True
            
    return False


if __name__ == '__main__':
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))

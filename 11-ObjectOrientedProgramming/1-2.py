class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perimeter(self):
      return self.a *4

square1 = Square(4)
square2 = Square(6)

wynik1 = square1.area()
wynik2 = square2.area()

obwod1=square1.perimeter()
obwod2=square2.perimeter()

print('Square with side 4:')
print(f'Area is {wynik1}, Perimeter is {obwod1}')
print ('Square with side 6:')
print(f'Area is {wynik2}, Perimeter is {obwod2}')

#lub
print('Square with side 4:')
print('Area is', square1.area(), 'Perimeter is', square1.perimeter())
print ('Square with side 6:')
print('Area is', square2.area(), 'Perimeter is', square2.perimeter())
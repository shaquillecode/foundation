class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Shaquille", "O'neal")
x.printname()
############################
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

def __next__(self):
  if self.a <= 20:
    x = self.a
    self.a += 1
    return x
  else:
      raise StopIteration
import datetime

x = datetime.datetime.now()

print(x)
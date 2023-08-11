#Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#Boolean

print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


#function can return a boolean
print("hi")
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

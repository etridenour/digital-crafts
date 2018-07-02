class Person:
  def greet (self):  #self points to object you are creating (ex. me, matt)
    print("Hello")
me = Person()
me.greet()

matt = Person()
matt.greet()
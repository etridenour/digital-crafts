
# #1

# class Person: 
#     def __init__(self, name, email, phone, friends):  
#      self.name = name 
#      self.email = email 
#      self.phone = phone 
#      self.friends = friends

#     def greet(self, other_person): 
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

#     def print_contact(self):
#         print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

#     #Add a method 2
#     def print_contact_info(self):
#         print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)


# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# sonny.greet(jordan)

# jordan.greet(sonny)

# sonny.print_contact()
# jordan.print_contact()

# sonny.print_contact_info()

# jordan.friends.append(sonny)

# #2

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year


# car = Vehicle('Nisssan', 'Leaf', 2015)
# print(car.make, car.model, car.year)





#add a method

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print(self.year, self.make, self.model)

# car = Vehicle('Nisssan', 'Leaf', 2015)
# car.print_info()



#add a method 2
# class Person: 
#     def __init__(self, name, email, phone):  
#      self.name = name 
#      self.email = email 
#      self.phone = phone 

#     def greet(self, other_person): 
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

#     def print_contact(self):
#         print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

#     #Add a method 2
#     def print_contact_info(self):
#         print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)


# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')


# sonny.print_contact_info()




#add instance variable
# class Person: 
#     def __init__(self, name, email, phone):
#      self.name = name   
#      self.email = email 
#      self.phone = phone 
#      self.friends = []

#     def greet(self, other_person): 
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

#     def print_contact(self):
#         print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

#     def print_contact_info(self):
#         print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)

    


# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')


# jordan.friends.append(sonny)
# sonny.friends.append(jordan)

# print(len(jordan.friends))


#add a add_friendd method
# class Person: 
#     def __init__(self, name, email, phone):
#      self.name = name   
#      self.email = email 
#      self.phone = phone 
#      self.friends = []

#     def greet(self, other_person): 
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

#     def print_contact(self):
#         print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

#     def print_contact_info(self):
#         print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)
    
#     def add_friend(self, friend):
#         self.friends.append(friend.name)

    
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# jordan.add_friend(sonny)
# print(jordan.friends)


#add a num_friends method
# class Person: 
#     def __init__(self, name, email, phone):
#      self.name = name   
#      self.email = email 
#      self.phone = phone 
#      self.friends = []

#     def greet(self, other_person): 
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

#     def print_contact(self):
#         print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

#     def print_contact_info(self):
#         print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)
    
#     def add_friend(self, friend):
#         self.friends.append(friend.name)

#     def num_friends(self):
#         print(len(self.friends))

    
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# jordan.add_friend(sonny)

# jordan.num_friends()


#count number of greetings
# class Person: 
#     def __init__(self, name, email, phone):
#      self.name = name   
#      self.email = email 
#      self.phone = phone 
#      self.friends = []
#      self.greeting_count = 0

#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))
#         self.greeting_count += 1

#     def print_contact(self):
#         print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

#     def print_contact_info(self):
#         print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)
    
#     def add_friend(self, friend):
#         self.friends.append(friend.name)

#     def num_friends(self):
#         print(len(self.friends))
    

# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)



#__str__
# class Person: 
#     def __init__(self, name, email, phone):
#      self.name = name   
#      self.email = email 
#      self.phone = phone 
#      self.friends = []
#      self.greeting_count = 0

#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))
#         self.greeting_count += 1

#     def print_contact(self):
#         print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

#     def print_contact_info(self):
#         print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)
    
#     def add_friend(self, friend):
#         self.friends.append(friend.name)

#     def num_friends(self):
#         print(len(self.friends))

#     def __str__(self): 
#      return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
    

# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# print(jordan)
# print(sonny)


# Bonus
class Person: 
    def __init__(self, name, email, phone):
     self.name = name   
     self.email = email 
     self.phone = phone 
     self.friends = []
     self.greeting_count = 0
     self.num_unique_people_greeted = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        

    def print_contact(self):
        print('Name: {}  Email: {}   Number: {}'.format(self.name, self.email, self.phone))

    def print_contact_info(self):
        print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)
    
    def add_friend(self, friend):
        self.friends.append(friend.name)

    def num_friends(self):
        print(len(self.friends))

    def __str__(self): 
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')





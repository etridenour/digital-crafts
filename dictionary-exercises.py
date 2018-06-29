print("---------- Exercise 1----------")

#1
phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}

#2
print(phonebook_dict['Elizabeth'])
phonebook_dict["Kareem"] = "938-489-1234"
print(phonebook_dict)

#3
del phonebook_dict["Alice"]
print(phonebook_dict)

#4
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

#5
print(phonebook_dict)




print("---------- Exercise 2 Nested Dictionaries ----------")

ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}

print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['name'])
print(ramit['friends'][1]['interests'][1])

print("---------- Letter Summary ----------")

def letter_histogram(word):
    h = {}
    for l in word:
        if l in h:
            h[l] += 1
        else:
            h[l] = 1
    print(h)

letter_histogram('fun times')


print("---------- Word Summary ----------")

def word_histogram(phrase):
    histogram = {}
    word = ""
    for letter in phrase:
        if letter.isalpha():
            word += letter
        else:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
            word = ""
    if word in histogram:
        histogram[word] += 1
    else:
        histogram[word] = 1     
    print(histogram)

print(word_histogram('to be or not to be'))

            









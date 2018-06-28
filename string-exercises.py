print("-----Number 1-----")
string = "i love pizza"
print(string.upper())

print("-----Number 2-----")
print(string.capitalize())

print("-----Number 3-----")
print(string[::-1])

print("-----Number 4-----")
paragraph = """Free, like a bird out in the wind of the night, like a 747 to LA that\'s in flight. 
Free - like a garden flourishing in the wind, like a student bout to do it when he\'s graduating."""
p_upper = paragraph.upper()
replace = (('A', '4'), ('E', '3'), ('G', '6'), ('I', 'l'), ('O', '0'), ('S', '5'), ('T', '7'))
for x, y in replace:
    p_upper = p_upper.replace(x, y)
print(p_upper)

print("-----Number 5-----")
word = input("What is the word? ")

a = word.find('aa')
e = word.find('ee')
i = word.find('ii')
o = word.find('oo')
u = word.find('uu')

if e >= 0:
    e_word = word.replace('ee', 'e' * 5)
    print(e_word)
elif a >= 0:
    a_word = word.replace('aa', 'a' * 5)
    print(a_word)
elif i >= 0:
    i_word = word.replace('ii', 'i' * 5)
    print(i_word)
elif o >= 0:
    o_word = word.replace('oo', 'o' * 5)
    print(o_word)
elif u >= 0:
    u_word = word.replace('uu', 'u' * 5)
    print(u_word)
else:
    print(word)

print("-----Number 6-----")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
phrase = "lbh zhfg hayrnea jung lbh unir yrnearq"
position = 0
newposition = 0
finalstring = " "
for phraseL in phrase:
    if phraseL.isspace() == False:
       position = alphabet.index(phraseL)
       newposition = position - 13
       finalstring = finalstring + alphabet[newposition]
print(finalstring)


    




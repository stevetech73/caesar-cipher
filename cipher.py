# add your code here

# create a dictionary

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipher_dict = {}     # create an empty dictionary

count = 5                  # this is how many characters to shift

for letter in alphabet:          
    key = letter                        # create a key
    value = alphabet[count]             # create a value for the key
    count = count + 1
    # print(count)
    # print(key, value)
    cipher_dict[key] = value               # create an entry to the dictionary
    if count == 26:
        count = 0                           # when you reach 26, reset counter to 0
    else:
        continue
    
# print(cipher_dict)                       # print the dictionary


enter_text = input("Enter a sentence: ")
enter_text = enter_text.lower()  # convert everything to lowercase

coded_text = ""                    # create an empty container
for char in enter_text:                   # for every member of 'enter_text'
    if char in cipher_dict:             # if the member is a 'key' in the dictionary
        char = cipher_dict[char]      # the value of 'char' = dictionary[key] = the value of the key
    coded_text += char               # add the value, 'char', to the container
    
print(coded_text)
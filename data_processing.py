sentence = input("Please enter your sentence ")

sentence_formatted = sentence.strip().upper()

print(sentence_formatted)


paragraph = input("Please enter your paragraph ")

count_words = paragraph.split()
num_words = len(count_words)

print("The paragraph contains:", num_words)

string = input("Please enter a string ")

string_check = string.isdigit()

print(string_check)

stringr = input("Please enter another string ")

string_replace = stringr.replace("a", "o")

print(string_replace)


name = input("Please type your full name with a space between first and last ")

initials = "".join(x[0] for x in name.split()).upper()

print(initials)

strlength = input("Please enter one more string ")

length = len(strlength)

print(length)
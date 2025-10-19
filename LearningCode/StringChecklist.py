# String checklist

# Create an empty string
empty_string = ""
ver2 = ''

# determine if a string is empty
if not empty_string:
    print("str_var is empty!!!")

# Format a string to be able to contain dynamic data
name = input("Yo whats yo name")
dynamo = f"hello {name}!"

# Access individual characters/items in a string
n = int(input("Yo what yo character yo wwanna find"))
nchar = name[n]

# Access the first, access the last character in a string
firstchar = name[0]
lastchar = name[-1]

# Join multiple strings together
stringOne = input("String one: ")
stringTwo = input("String two: ")
stringOneTwo = stringOne + stringTwo

# Reverse a string
NameReverse = name[::-1]

# Create a copy of a string
namecopy = name

# Compare strings for equality
if stringOne == stringTwo:
    print("equal")

# Determine the minimum and maximum value within a string
for char in name:
    minchar = char
    maxchar = char
    if char < minchar:
        minchar = char
    elif char > maxchar:
        maxchar = char

# Determine if an item or a pattern exists within a string
skibidistring = "skibiditoilet"
if "skibidi" in skibidistring:
    print("YES IT EXISTS")
else:
    print("NAH IT DONT")

# Locate the index of an item or a pattern in a string
index = skibidistring.find("skibidi")
print(index)

# Count how often an item or a pttern occurs within a string
skibidicount = skbidistring.count("skibidi")

# Convert all items in a string to uppercase/lowercase
skibidistring = skibidistring.upper()
skbidistring = skibidistring.lower()

# Determine if the string can be converted to an integer
str_nm = "67"
num = 0
if str_nm.isdigit(): # Checks if the string is composed of only digits
    num = int(str_num)

#Convert a string to an integer
num = int(str_num)

# Determine if a string only contains alphabetical characters
if skibidistring.isalpha():
    print(True)

# Remove non-alphabetical characters from a string.
gibberish = "OIDSJDHIOUAUHDLAOH!)#*094014u1hjdsaidhaioVGuiahisdohu183891ry9183oh"
clean = ""
i = 0
while i < len(gibberish):
    if gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1

# Remove all alphabetical characters from a string.
i = 0
clean = ""
while i < len(gibberish):
    if gibberish[i].isalpha() == False:
        clean += gibberish[i]
    i += 1

# Remove all whitespaces from a string
whitespacer = " AJAJAJ    JAJAJ   "
whitespacer = whitespacer.replace(" ", "")

# Sort a string in ASCII order or reverse-ASCII order
sorted_string = skibidi.sort()
sorted_
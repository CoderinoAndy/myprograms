# Create an empty list
mylist = []
# Determine if a string is empty
s = ""
if not s:
    print("s empty")
# len() counts the # of elements
lengthlist = [1, 2, 3]
print(len(lengthlist))

# sum() gets the sum of the elements
print(sum(lengthlist))

# min() gets the minimum value of the elements
testalpha = ["a", "b", "c"]
print(min(testalpha))
testnum = [1, 2, 3]
print(min(testnum))

# max() gets the max value of the elements
print(max(testalpha))
print(max(testnum))

# Access individual characters in a list
raceList = ["first", "second", "third", "fourth"]
print(f"{raceList[0]} won the race")
print(f"{raceList[3]} is so buns genuinely")

# Access the first and last characters in a list
print(f"{raceList[0]}")
print(f"{raceList[-1]}")

combinedlist = testalpha + testnum
print(combinedlist)
#or
testalpha.extend(testnum)
#mutates testalpha to have testnum
#or
for x in testnum:
    testalpha.append(x)

# Reverse a list
print(raceList[::-1])

# Create a copy of a list
copyRaceList = raceList[:]
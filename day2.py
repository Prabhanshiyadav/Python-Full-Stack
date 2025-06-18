
                                            #  (Strings in Python)

#                                    1️⃣ Creating and Accessing Strings
s1 = "Hello, Python!"
print(s1)           # Entire string
print(s1[0])        # First character: 'H'
print(s1[-1])       # Last character: '!'

s2 = "India is my country"
print(s2)
print(s2.isalpha())     
print(s2.replace("India", "USA"))  # Replace 'India' with 'USA'




#                                    2️⃣ String Methods
text = "hello world"
print(text.upper())           # HELLO WORLD
print(text.capitalize())      # Hello world
print(text.title())           # Hello World
print(text.replace("world", "Python"))  # hello Python
print(text.count("l"))        # 3
print(len(text))              # 11



#                                     3️⃣ Slicing & Indexing         
text = "PythonProgramming"

print(text[0:6])    # 'Python'
print(text[6:])     # 'Programming'
print(text[:6])     # 'Python'
print(text[::-1])   # Reverse: 'gnimmargorPnohtyP'




#                                     4️⃣ String Formatting
name = "Alice"
age = 22

# f-string
print(f"My name is {name} and I am {age} years old.")

# .format()
print("My name is {} and I am {} years old.".format(name, age))




#                                      5️⃣ String Concatenation
a = "Hello"
b = "World"
c = a + " " + b    # "Hello World"
print(c)
print(a * 3)       # "HelloHelloHello"

 
                                       # 💡 Challenge: Word Frequency Counter

sentence = "python is fun and easy to learn"
print(sentence)
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
    print(freq)




                                             # ✅ Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)


                                             # ✅ Accessing elements
print("First fruit:", fruits[0])


                                             # ✅ Modifying elements
fruits[1] = "blueberry"
print("Updated fruits:", fruits)


                                             # ✅ Adding elements
fruits.append("dragonfruit")
print("After append:", fruits)


                                             # ✅ Inserting at a position
fruits.insert(1, "kiwi")
print("After insert:", fruits)


                                             # ✅ Removing elements
fruits.remove("apple")
print("After removing 'apple':", fruits)


                                             # ✅ Looping through list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)


                                             # ✅ List comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares using list comprehension:", squares)


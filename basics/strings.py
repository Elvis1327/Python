

myStr = 'hello world'

#Concatenar there are two ways
print("my Name is "+myStr)
# another way to concatenar
print(f"my name is {myStr}") # the letter f is obligatory


# print(dir(myStr))

print(myStr.upper()) # Return all keyWords upperCase
print(myStr.lower()) # Return all keywords lowerCase
print(myStr.capitalize()) # return the first letter in CapitalCase
print(myStr.replace('Hello', 'bye')) # Can replace one word
print(myStr.count('l')) # return the times we use a letter in this case 3 

print(myStr.startswith('hola')) # return a boolean depending if the word is starting with the word passed as an argument in this case False

print(myStr.split('o')) # convert a strign in a List depending what is passing as an argument, by default it separate by space

print(myStr.find('o')) # return the index of a letter passed as an argument

print(len(myStr)) # devuleve la longuitud de un string o arreglo


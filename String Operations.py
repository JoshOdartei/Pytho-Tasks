"""
EXAMPLES OF STRING SUBSETTING
"""

text = "Allos@Parakletos 1"
print(text[0:5]) #Displays the first 5 elements
print(text[1::2])  #Displays odd-indexed elements
print(text[0:-1:3]) #Displays all elements from start to end with a step of 3

print(len(text)) #prints the length of the string
print(text.replace(" ","_")) #replaces space with an underscore
print(text.split(" ")) #Splits the string along the space
print(text.upper()) # Prints the string in caps

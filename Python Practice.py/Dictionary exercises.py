#                                 Exercise
# 1) Create a dictionary and take input from the user and return the meaning of the word from the dictionary.
dict1 = {"Set" : "Set is an organized collection of objects.","Mutable" : "Liable to change","Immutable" : "Not liable to change","Floccinocinihilipilification" : "The act of estimating something or someone is worthless."}
input1 = input("Enter the meaning of the word you want to find : ").capitalize()
if input1 in dict1.keys() : 
    print(dict1[input1])
else :
    print("Invalid input.Please try again.")
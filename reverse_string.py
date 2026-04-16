# Reverse a string in python using for loop



#Logic
 
string = "python"
reversed_string = ""

for char in reversed_string:
    reversed_string = char + reversed_string

print(reversed_string)





# Function

def revesed_maker(string : str) -> str:
    if not isinstance (string,str):
        raise TypeError("Input is not a string")
        
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

if __name__== "__main__":
   try:
       user_input = input("Enter your string to reverse: ")
       result =revesed_maker(user_input)
       print(f"your reversed string is: {result}")
   except TypeError as e:
       print(e)
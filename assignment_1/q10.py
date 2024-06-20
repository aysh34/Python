# Write a Python program that performs the following steps:
# ● Define a string vowels containing all lowercase vowels ('aeiou').
# ● Take input from the user to enter a letter (lowercase). Check if the entered
# letter is 'a' using membership operators (in or not in). Print True if the
# entered letter is 'a', otherwise print False

vowels = "aeiou"
user = input("Enter any letter(lowercase): ")
print(
    "checking whether user's entered letter present in vowels or not\n", user in vowels
)
print("checking whether user's entered letter is 'a' or not\n", user == "a")

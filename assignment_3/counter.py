starting_no = int(input("Enter a starting number: "))  # ask user to enter a starting_no
while (
    starting_no >= 0
):  # keep executing while loop until starting_no is greater or equal to zero
    print(starting_no)  # print current number
    starting_no -= 1  # decrement starting no by 1
print("Countdown finished!")

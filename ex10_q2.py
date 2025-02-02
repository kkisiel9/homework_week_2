import getpass
# the star is the wild card
# # Question 2
# # Defining the variable (string) pin, which will used to match what the user supplies
# pin = '3456'
# # Restricting the attempts users have to 3
# pin_attempt = 3
# # This uses a for loop since we only want 3 users to have 3 attempts
# for i in range(pin_attempt):
#     # the prompt message for uses
#     supplied_pin = input('Enter your pin:')
#     supplied_pin = getpass.getpass(prompt='Enter your pin:', stream=None)
#     # Condition statement to check if the pin supplied by user matches the pin variable we defined
#     if supplied_pin == pin:
#         print(f"Please proceed with one of the options: Cash Withdraw, Balance Enquiry, Mini Statement, Pin Unblock")
#         break
#     else:
#         pin_attempt = pin_attempt -1
#         if  pin_attempt > 0:
#             print(f"You have {pin_attempt} attempts left")
#         else:
#             print("Incorrect pin: Too many attempts; Your card is now blocked")
#
#
#
# # Question 3
# Restricting the attempts users have to 3
pin_attempt = 3
pin ='3456'

for i in range(pin_attempt):
    supplied_pin = getpass.getpass(prompt='Please enter your pin')

    if supplied_pin == pin:
        print('Please proceed with one of the options: Cash Withdraw, Balance Enquiry, Mini Statement, Pin Unblock')
        break # Exit loop if the PIN is correct
    else:
        pin_attempt = pin_attempt - 1 # Decrase the number of attempts by 1 each time
        if pin_attempt > 0:
            print(f"You have {pin_attempt} attempts left") # Let users know the number of attempts
        else:
            print("Incorrect pin: Too many attempts; Your card is now blocked") # Once the users have reached the maximum attempts


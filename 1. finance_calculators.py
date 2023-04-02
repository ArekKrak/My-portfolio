""" 
1. I imported the math module.
2. To make sure the first two (excluding the heading) 'print()' statements are aligned from the dash point, 
   I used the 'format' function to determine that point.
3. I created a variable to store the user's input and appended the 'lower()' method so that the user's input 
   never affects how the program proceeds.
4. The first 'if' condition checks whether the input is correct; if not, the error message will pop up and prompt 
   the user to try again.
5. I've set a block of nested 'if' conditions to perform the following operations:
    5a. If the user types "investment" in, they're asked to give some figures like the amount of money to be paid in, 
        interest rate, and the number of years.
    5b. The user is next asked to choose a simple or compound interest by the 'input' statement.
    5c. Of course, if they happen to mistype the answer, they will then receive an error and will be prompted
        to try again.
    5d. The variables containing all calculations were set, as given in the 'Interest formula'. Also, I wrapped 
        the values of those variables with 'round()' function to round the outcome to two decimals, which originally 
        was out of control.
    5e. At the bottom of the block, I nested another block of the 'if' statements printing accordingly to the chosen type of
        interest.
6. One condition of the 'if' statement comprises the home loan repayment calculator:
    6a. Just as in the case of the investment calculator, I set a few input statements to store the user's input, then variables 
        consisting of calculations, according to the manual, and a 'print()' statement at the bottom.
7. I tried to keep the code clean and made sure it was readable, together with the output. I added the heading because the output 
   looks cooler with it, and the error message in the investment calculator block of conditions to make the calculator more efficient. 
   I tested the code in every possible way, and it works fine. """

import math

print("\t\t\tFINANCIAL CALCULATORS\n")
print(f"{'investment':<11}- to calculate the amount of interest you'll earn on your investment")
print(f"{'bond':<11}- to calculate the amount you'll have to pay on a home loan")
calc_type = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if calc_type != "investment" and calc_type != "bond":
    print("Incorrect input. Please, try again.")

if calc_type == "investment":
    amount = int(input("\nPlease, enter the amount you want to deposit: £"))
    interest_rate = int(input("Please, enter the interest rate: "))
    years = int(input("Please, enter the number of years you want to invest for: "))
    interest = input("Do you want \"simple\", or \"compound\" interest? ").lower()
    if interest != "simple" and interest != "compound":
        print("Incorrect input. Please, try again.")
    r = interest_rate / 100
    simple_int = round(amount*(1 + r*years), 2)
    comp_int = round(amount * math.pow((1+r), years), 2)
    if interest == "simple":
        print("\nThe total balance after the term of " + str(years) + " year(s), at the " + str(interest_rate) +
               "% rate is £" + str(simple_int) + ".")
    if interest == "compound":
        print("\nThe total balance after the term of " + str(years) + " year(s), at the " + str(interest_rate) +
               "% rate is £" + str(comp_int) + ".")

if calc_type == "bond":
    value = int(input("\nPlease, enter the value of the house: £"))
    interest_rate = int(input("Please, enter the interest rate: "))
    months = int(input("Please, enter the number of months you plan to take to repay the bond: "))
    i = (interest_rate / 100) / 12
    rep_formula = round((i * value)/(1 - (1 + i)**(-months)), 2)
    print("\nThe total amount to repay each month, at the " + str(interest_rate) + "% rate is £" + str(rep_formula) + ".")

""" 
1. I created initial 'print()' statements containing the heading and the types of operations for 
   the user.
2. I created the try-except block for a better user experience. If they happen to press the 
   ctrl + c key combination at any point during the process, the program will throw 
   a 'KeyboardInterrupt' exception and will be terminated. The user will be prompted to reboot it.
3. The variable 'new_filename' that stores the user's input creates a new text file.
4. For the program to give the user opportunity to do a series of calculations within the same boot,
   I encapsulated another try-except block to inform the user about the exceptions like 
   'ZeroDivisionError' or 'ValueError' in a friendly manner, within a 'while' loop.
    4a. The variable 'file' with the value 'a' opens a new file and records every operation 
        therein.
    4b. The latter three variables are for the user input which later is used to execute
        an operation.
    4c. To prevent any unwanted bug while choosing a type of operation, the 'while' loop, with 
        a series of the 'and' logical operators, comes in to keep everything in order.
    4d. In the next four 'if' conditional blocks, the operations for particular types of equations 
        are performed. Each block consists of the following statements:
        - 'print()' statement to display the result of the equation;
        - '.write()' statement to write the result into the text file;
        - the result of the division within the division 'if' block is wrapped in a 'round()' 
          function to control the decimal points. The results are rounded to one decimal point.
    4e. To check whether or not the user wants to continue, I added user input statement:
        - if they choose not to continue, they're then redirected to the "read" stage;
        - of course, if they happen to mistype, they're given a choice, the 'while' loop again
          gives this opportunity;
    4f. At the end of the loop, a '.close()' statement closes the file, and no more results are 
        written in. The user is then redirected to follow further instructions to read all the 
        equations recorded in the file.
5. To get the "read" stage to work well and make it user-friendly, the try-except block within 
   the while loop gives again user the chance to attempt a correct input as long as they fail.
    5a. An input statement was created to ask the user for the filename. Every time they fail 
        to give the correct name, an exception 'FileNotFoundError' will be thrown, after which 
        they will be prompted to try again - quite friendly :-)
    5b. Once the correct answer is given, the 'open()' statement with the value 'r' (read-only)
        will load up all the equations.
    5c. The 'print()' statement will display them all, and the last three will terminate 
        the program.
6. I tested my application in numerous ways to see if it has any bugs, but I haven't found
   anything confirming the existence thereof. """

print("\nTHIS IS THE SIMPLE CALCULATOR\n\nBelow are the following operations you can perform:\n" +
      "\nAddition (+)\nSubtraction (-)\nMultiplication (*)\nDivision (/)")

try:
    
    new_filename = input("\nEnter your new filename (.txt): ")
    while True:
        try:
            
            file = open(new_filename, "a")
            num1 = int(input("\nEnter the first number: "))
            num2 = int(input("Enter the second number: "))
            operator = input("\nSelect the type of operation you want to do.\n" +
                              "[choose one of the following operators for particular type of " +
                                "operation: +, -, *, /]: ")

            while operator != '+' and operator != '-' and operator != '*' and operator != '/':
                operator = input("\nInvalid input. Please, try again: ")

            if operator == '+':
                print(f"\n{num1} + {num2} = " + str(num1 + num2))
                file.write(f"\n{num1} + {num2} = " + str(num1 + num2))
            
            elif operator == '-':
                print(f"\n{num1} - {num2} = " + str(num1 - num2))
                file.write(f"\n{num1} - {num2} = " + str(num1 - num2))
            
            elif operator == '*':
                print(f"\n{num1} * {num2} = " + str(num1 * num2))
                file.write(f"\n{num1} * {num2} = " + str(num1 * num2))
            
            elif operator == '/':
                print(f"\n{num1} / {num2} = " + str(round(num1 / num2, 1)))
                file.write(f"\n{num1} / {num2} = " + str(round(num1 / num2, 1)))
            
            question = input("\nDo you want to continue or read all of your equations done" +
                                " so far?\n[press 'c' for \"continue\" or 'r' for " +
                                "\"read\"]:\t").lower()

            while question != 'c' and question != 'r':
                question = input("\nInvalid input. Please, try again: ").lower()
            
            if question == 'c':
                continue
            
            elif question == 'r':
                break

        except ZeroDivisionError:
            print("\nYou can't divide by zero. Please, try again.")
        except ValueError:
            print("\nInvalid value. Please, try again.")
    
    file.close()

    while True:
        file = None
        try:
            
            filename = input("\nEnter your filename (.txt) here: ")
            file = open(filename, "r")
            print(file.read())
            file.close()
            print("")
            break
        
        except FileNotFoundError:
            print("\nThe file that you are trying to open does not exist. Please, try again.")

except KeyboardInterrupt:
    print("\n\n\t### APPLICATION INTERRUPTED ###\n")
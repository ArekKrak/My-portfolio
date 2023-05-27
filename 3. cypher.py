""" 
1. I defined a function that encrypts messages input by the user using one parameter.
	1a. I set an empty string variable that will store ciphertext in the latter steps.
	1b. The 'for' loop iterates through a plaintext input in the 'plaintext' argument. That 
		iteration is designed for the following operations within an 'if-elif-else' block of
		statements:
			- the 'if' statement verifies if a letter is uppercase; if so, an integer representing
			  the Unicode of the given uppercase letter (A-Z is within a 65-90 ASCII range) in
			  the ASCII character table is converted, using the 'ord()' function and then that
			  character is returned in the line below, using the 'chr()' function;
			- the 'elif' statement verifies if a letter is lowercase; if so, an integer 
			  representing the Unicode of the given lowercase letter (a-z is within a 97-122 ASCII
			  range) in the ASCII character table is converted, using the 'ord()' function and then
			  that character is returned in the line below, using the 'chr()' function;
			- the 'else' statement handles non-alphabet characters;
			- perform the actual encryption, which is done by using the following formula: 
			  C = (P + K) % 26, where 'C' stands for 'Ciphertext', 'P' for 'Plaintext', 
			  and 'K' for 'Key'.
	1c. The function is finalised with a 'print statement', which uses the empty string variable
		and prints out the ciphertext.
2. The user interface part of the application starts with a heading, which I called 'CONTACT FORM'.
3. To ensure a user-friendly experience of the application, I included the user-operated part
   within a 'try-except' block in the event of interrupting the application by the user.
4. The application is a contact form (rudimentary, though as for ciphers absolutely ok) consisting
   of the subject, text box, and e-mail address box; all well-formatted to ensure a positive
   user experience. """

def cipher(plaintext):
    
	cipher_str = ''		# A variable to hold the latter ciphertext.

	for i in plaintext:
		if i.isupper():
			# Below is conversion of uppercase letters with a key equal to 15.
			cipher_upper = 65 + ((ord(i) - 65 + 15) % 26)
			# The undermentioned statement returns encrypted uppercase letter.
			cipher_str = cipher_str + chr(cipher_upper)
		elif i.islower():
			# Below is conversion of lowercase letters with a key equal to 15.
			cipher_lower = 97 + ((ord(i) - 97 + 15) % 26)
			# The undermentioned statement returns encrypted lowercase letter.
			cipher_str = cipher_str + chr(cipher_lower)
		else:
			# Below is the statement that handles non-alphabet characters.
			cipher_str = cipher_str + i
	
	# Whatever text input by the user is printed out as a ciphertext using the appropriate variable
	print(f"{'[Encrypted]':<22}" + cipher_str + "\n")

print("\n______________________________________________________________________\n")
print(f"{'':<28}CONTACT FORM\n")

try:	# <-- Just in case of interrupting the program by the user.

	plaintext = input(f"{'Subject:':<22}")
	cipher(plaintext)
	plaintext = input(f"{'Your message:':<22}")		# Well formatted.
	cipher(plaintext)
	plaintext = input(f"{'Your e-mail address:':<22}")
	cipher(plaintext)

	print("Thanks for submitting our [safe!] form. We'll get back to you shortly.")
	print("\n______________________________________________________________________")

except KeyboardInterrupt:
	print("\n\n\t****** APPLICATION INTERRUPTED ******\n")

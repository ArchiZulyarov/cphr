print("Welcome to Zulyarov Chipher.\n Do you want to encrypt or decrypt your message?\n 1 - encrypt  2 - decrypt.")
answer = int(input("Enter 1 or 2: "))
alpha = 'abcdefghijklmnopqrstuvwxyz'

if answer == 1:
	n = int(input("\nEnter key to encrypt: "))
	s = input("Message: ").strip()
	res = ''
	for c in s:
		res += alpha[(alpha.index(c) + n) % len(alpha)]
	c= ('' + res + '')
	print(c)
  
	out1 = (c[::-1])
	print(out1)

	out = ' '.join(format(ord(x), 'b') for x in out1)
	print(out)
  
  
if answer == 2:
	g = input("Decrypt: ")
	
	revert = ''.join([chr(int(s, 2)) for s in g.split()])
	print(revert)
	
	a = (revert[::-1])
	print(a)

	
	
	encrypted_message = a.strip()
	print()
	key = int(input("Enter key to decrypt: "))
	decrypted_message = ""
	for c in encrypted_message:

		if c in alpha:
			position = alpha.find(c)
			new_position = (position - key) % 26
			new_character = alpha[new_position]
			decrypted_message += new_character
		else:
			decrypted_message += c 
	print("Your decrypted message is: ",decrypted_message)

	


# Tkinter
from tkinter import *
# Keypair generation
from simplefhe import generate_keypair
# Client-Side encryption
from pathlib import Path
from simplefhe import (
	encrypt, load_public_key, load_relin_keys, 
	display_config, load_encrypted_value, 
	load_private_key, decrypt
)

# Keypair generation
public_key, private_key, relin_keys = generate_keypair()
Path('keys').mkdir(exist_ok=True)
public_key.save('keys/public.key')
private_key.save('keys/private.key')
relin_keys.save('keys/relin.key')
#print('Keypair saved to keys/ directory')

sensitive_data = []
string_array = []
int_array = []

def addList():
	sensitive_data.append(dataValue.get())
	entry.delete(0, END)

def encryptData():
	for num in sensitive_data:
		string_array.append(str(num))	
	joined_string = ",".join(string_array)
	print(f'Data to encrypt: {joined_string}')
	#Label(root, textvariable=joined_string).grid(row=2, column=3, columnspan=2)

	load_public_key('keys/public.key')
	load_relin_keys('keys/relin.key')
	#display_config()

	# Create directory 'inputs' only if it doesn't exist
	Path('inputs').mkdir(exist_ok=True)

	# Encrypt
	for num in string_array:
		try:
			int_array.append(int(float(num.strip('"'))))
		except ValueError:
			pass

	termwidth, fillchar = 78, '='
	print(f' ENCRYPT '.center(termwidth, fillchar))
	for i, entryData in enumerate(int_array):
		# Encrypt with the public key
		encrypted = encrypt(entryData)
		# Save encrypted data to the new directory 'inputs'
		encrypted.save(f'inputs/{i}.dat')
		print(f'[CLIENT] Input {entryData} encrypted to inputs/{i}.dat')

	# Create directory 'outputs' only if it doesn't exist
	Path('outputs').mkdir(exist_ok=True)

	# Function to apply to the encrypted data
	def f(x): return x**3 - 3*x + 1

	# Apply the function to the encrypted data -> FHE basics
	for i in range(len(sensitive_data)):
	    # Obtain the encrypted values from the 'inputs' directory
	    value = load_encrypted_value(f'inputs/{i}.dat')
	    # Apply the function ON the encrypted data
	    result = f(value) 
	    # Save the result of applying the function on the encrypted data to the 'outputs' directory
	    result.save(f'outputs/{i}.dat')
	    #print(f'[SERVER] Processed entry {i}: inputs/{i}.dat -> outputs/{i}.dat')

def decryptData():
	load_private_key('keys/private.key')
	load_relin_keys('keys/relin.key')
	#display_config()

	# Decrypt
	# We will obtain the function x**3 - 3*x + 1 on sensitive_data
	termwidth, fillchar = 78, '='
	print(f' DECRYPT '.center(termwidth, fillchar))
	for i, entryData in enumerate(sensitive_data):
	    # Bring the data of the 'outputs' folder
	    encrypted = load_encrypted_value(f'outputs/{i}.dat')
	    # Obtains result of the application of the function on the sensitive_data, decrypted
	    result = decrypt(encrypted)
	    print(f'[CLIENT] Result for {entryData}: {result}')

# Initialize Tkinter
root = Tk()

root.geometry("550x300")
root.config(background="#213141")
# Header
Label(root, text="Client", font="ar 15 bold", bg="#56CD63", pady=5, fg="white").grid(row=0, column=3)

# Data
data = Label(root, text="Insertar datos a encriptar: ", padx=10)
data.grid(row=1, column=2)
dataValue = IntVar()
entry = Entry(root, textvariable=dataValue)
entry.grid(row=1, column=3)
entry.delete(0, END)

#Label(root, text="Datos a encriptar: ", padx=10).grid(row=2, column=2)

# Buttons
Button(text="Añadir", command=addList).grid(row=3, column=3, pady=10)
Label(root, text="* Añade a la lista de\n datos para encriptar.", fg="#ff0000").grid(row=3, column=4, padx=10)
Button(text="Encriptar", command=encryptData).grid(row=4, column=3, pady=10)
Button(text="Mostrar datos desencriptados", command=decryptData).grid(row=5, column=3, pady=10)

root.mainloop()


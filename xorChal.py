#decode this cipher: B~e6awe6byy6sweo6pyd6oyc6~c~)6Xsnb6b{s61zz6{w}s6cxtdsw}wtzs6uf~sd

def xor_operation(char, key):
    return chr( ord(char) ^ key )

def encrypt_message(input_string, key=22):
    # doing xor on every character of input_string
    xor_chars = [xor_operation(char, key) for char in input_string]
    
   
    cipher = ''.join(xor_chars)
    return cipher


input_string = "Fake flag"


result = encrypt_message(input_string)  
print(result)

#hint: 
#message ^ key = cipher
#cipher ^ key = message







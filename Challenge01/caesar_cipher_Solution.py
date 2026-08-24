SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def caesar_cipher(message, key, mode):
    translated = ''
    num_symbols = len(SYMBOLS)
    
    if mode == '1':
        key = -key
        
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = (symbol_index + key) % num_symbols
            translated += SYMBOLS[translated_index]
        else:
            translated += symbol
            
    return translated

# user input
mode = input("Choose mode encrypt (1) decrypt (2): ").strip()
message = input("Enter your message: ")
key = int(input("Enter key shift (number): "))

# cipher and result
output = caesar_cipher(message, key, mode)
print(f"\nResult: {output}")

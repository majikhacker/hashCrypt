# Mapping for the custom language
custom_mapping = {
    'A': 'E', 'B': 'D', 'C': 'K', 'D': 'B', 'E': 'A',
    'F': 'S', 'G': 'T', 'H': 'R', 'I': 'O', 'J': 'Z',
    'K': 'C', 'L': 'N', 'M': 'W', 'N': 'L', 'O': 'I',
    'P': 'V', 'Q': 'X', 'R': 'H', 'S': 'F', 'T': 'G',
    'U': 'Y', 'V': 'P', 'W': 'M', 'X': 'Q', 'Y': 'U',
    'Z': 'J'
}

# Create case-insensitive mapping
custom_mapping.update({k.lower(): v.lower() for k, v in custom_mapping.items()})

def create_translator(mapping):
    def translate(text):
        return ''.join(mapping.get(char, char) for char in text)
    return translate

# Create the translator function
translate_to_custom = create_translator(custom_mapping)

# Interactive loop
while True:
    user_input = input("Enter text to translate (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    translated_output = translate_to_custom(user_input)
    print("Translated text:", translated_output)

original_input = input("The message to encrypt is: ")
original_input = original_input.upper()
final_input = ""

for letter in original_input:
    hidden_letter = ord(letter)
    new_letter = hidden_letter + 13
    if new_letter >= 65 and new_letter <= 90:
        final_input = final_input + chr(new_letter)
    elif new_letter > 90:
        new_letter = new_letter - 26
        final_input = final_input + chr(new_letter)
print("The new message is: " + final_input)

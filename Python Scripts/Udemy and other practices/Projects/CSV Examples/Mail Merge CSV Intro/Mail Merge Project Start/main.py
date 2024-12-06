#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"    # Constant where we will replace the starting letter: [name]

with open("./Input/Names/invited_names.txt") as names_file: # relative file path
    names = names_file.readlines()    # Turn it into a list
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() # Normal read file without doing anything. Turn it into a string
    # print(letter_contents)
    for name in names: # name is just a counter
        stripped_name = name.strip() # Takes away the space between name and comma
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) # Replaces the PLACEHOLDER
        # Changed the title of the document
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.doc", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        
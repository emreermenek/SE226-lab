import random
import string


replacement_dict = {}

string.punctuation

print("Choose 5 characters (lowercase only) and assign 3 replacement options each:")
other_replacements = set()
for _ in range(5):

    while True:
        letter = input("Enter a lowercase character: ")
        if letter in replacement_dict or not letter.islower() or len(letter) != 1:
            print("Invalid or duplicate letter, try again.")
        else:
            break

    replacements = set()
    while len(replacements) < 3:
        replacement = input(f"Enter a replacement for '{letter}': ")
        if len(replacement) == 1 and replacement not in replacements and replacement not in other_replacements and replacement in string.punctuation:
            replacements.add(replacement)
            other_replacements.add(replacement)
        else:
            print("Invalid or duplicate replacement, try again.")

    replacement_dict[letter] = list(replacements)


passwords = [''.join(random.choices(string.ascii_lowercase, k=15)) for _ in range(5)]


categorized_passwords = {"strong": [], "weak": []}

for password in passwords:
    modified_password = list(password)
    replaced_count = 0

    for i, char in enumerate(password):
        if char in replacement_dict:
            modified_password[i] = random.choice(replacement_dict[char])
            replaced_count += 1

    modified_password = ''.join(modified_password)

    if replaced_count > 4:
        categorized_passwords["strong"].append(modified_password)
    else:
        categorized_passwords["weak"].append(modified_password)



print("\nGenerated Passwords:\n")

print("STRONG PASSWORDS:")
for pwd in categorized_passwords["strong"]:
    print(pwd)

print("\nWEAK PASSWORDS:")
for pwd in categorized_passwords["weak"]:
    print(pwd)

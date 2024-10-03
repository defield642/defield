#Write a program that counts number of vowels in a sentence

def vowels_calcu(sentence):
    vowels=set("aeiouAEIOU")

    #using loop to count number of vowels in a sentences

    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1

    return vowel_count   

user_input = input("Enter a sentence:\n")

number_of_vowels = vowels_calcu(user_input)

print("number of vowels is:",number_of_vowels)

            

    

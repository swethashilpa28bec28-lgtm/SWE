#Count vowels
def count_vowels(s):
   
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

string = input("Enter any string:")
vowel_count = count_vowels(string)
print("No of vowels in the given string is:",vowel_count)


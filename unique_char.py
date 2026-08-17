#unique characters in set


def print_unique_chars(s):
 
  unique_characters = set()

  for char in s:
    unique_characters.add(char)

  print(f"The unique characters in the string '{s}' are:")

  for unique_char in unique_characters:
    print(unique_char, end=' ')
  print() 


input_string = input("Enter any string:")
print_unique_chars(input_string)

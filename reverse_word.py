#Reverse of words in sentences

def reverse_words_in_sentence(sentence):
    
    words = sentence.split()
    
    
    reversed_words = [word[::-1] for word in words]
    
    
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Example usage:
input_sentence = input("Enter any string:")
output_sentence = reverse_words_in_sentence(input_sentence)

print(f"Original sentence: {input_sentence}")
print(f"Reversed words sentence: {output_sentence}")

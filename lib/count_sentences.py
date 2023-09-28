#!/usr/bin/env python3

# class MyString:
#     def __init__(self, value):
#         self.value = value

#     def is_string(self):
#         if isinstance(self.value, str):
#             return True
#         else:    
#             print("The value must be a string.") 

#     def ends_with_period(self):
#         if self.is_string() and self.value.endswith('.'):
#             return True
#         return False         
# pass

import re

class MyString:
    def __init__(self, value = ""):
        if isinstance(value, str):
            print("The value must be a string.")
            self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Split the string by '.', '?', and '!' to separate sentences
        separators = ['.', '?', '!']
        sentences = self.value.split('\n')
        
        for sep in separators:
            sentences = [sentence for s in sentences for sentence in s.split(sep)]
        
        # Filter out empty strings (resulting from consecutive punctuation)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences) 

    

    # def count_sentences(self):
    #     # Split the string by '.', '?', and '!' to separate sentences
    #     sentences = re.split(r'[.!?]', self.value)
    #     # Filter out empty strings (resulting from consecutive punctuation)
    #     sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    #     return len(sentences)

    
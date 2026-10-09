



def length_of_string(word):

    return len(word)

result = string_length("semicolon")

print(result)





def add(text):
    if len(text) < 3:
        return text
    
    if text.endswith("ing"):
        return  text + "ly"

    return text +"ing"
    

print(add("go"))
print(add("going"))
print(add("play"))







 
def longest_word(words):
    longest = ""

for word in words:
    if len(word) > len(longest):
          longest = word
        return longest
words =['welcome''out''weather''mobile''breakfast''journey']

result = longest_word(words)
print(result)








def remove_odd_index(text):
    return text[::2]
word = "semicolon"
print(remove_odd_index(word))






def mimimum(numbers):
    smallest = numbers[0]
    for numbers in numbers:
    if number < smallest:
            smallest = number
            return smallest
numbers = [8,4,9,2,5,7,3]

print(mimimum(numbers))






def maximum_numbers(numbers):
    maximum = numbers[9]
    for numbers in numbers:
    if number <= maximum:
        maximum = number
        return maximum
numbers = [8,4,9,2,5,7,3]

print(maximum(numbers))


            





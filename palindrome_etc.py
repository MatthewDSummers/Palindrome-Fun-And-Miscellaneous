def is_palindrome(text):
    text = "".join([x for x in text if x.isalpha()]).lower()
    return text[::-1] == text[::1]

def pals_from_string(text):
    text = text.split()
    return [word for word in text if word[::1] == word[::-1]]

def pals_from_string_list(list_of_strings):
    return [word for word in list_of_strings if word[::1] == word[::-1]]

def count_chars(text):
    the_count = {}
    for letter in text:
        if letter.isalpha():
            the_count[letter] = the_count.get(letter, 0) + 1
    return the_count

def reverse_each_word(text):
    if isinstance(text, str):
        text = text.split()
        reversed_text = [word[::-1] for word in text]
        return " ".join(reversed_text)
    else:
        raise TypeError("Input must be a string")

def remove_dupes(the_list):
    # fictional benchmark 
    if len(the_list) > 1000:
        return list(set(the_list))
    else:
        # just to demonstrate it algorithmically 
        items = []
        for item in the_list:
            if item not in items:
                items.append(item)
        return items

def return_evens(num_list):
    if not isinstance(num_list, list):
        raise TypeError("Input must be a list")
    return [x for x in num_list if x % 2 == 0]

# O U T P U T

print(is_palindrome("A Man, A Plan, A Canal, Panama!"))
# True 

print(is_palindrome("This is not a palindrome"))
# False 

print(pals_from_string("racecar javascript level mustard noon"))
# ['racecar', 'level', 'noon']

print(pals_from_string_list(["racecar", "javascript", "level", "mustard", "noon"]))
# ['racecar', 'level', 'noon']

letter_count = count_chars("hello, world")
for k, v in letter_count.items():
    print(f"{k}: {v}")

# h: 1
# e: 1
# l: 3
# o: 2
# w: 1
# r: 1
# d: 1

print(reverse_each_word("hello world!"))
# olleh !dlrow

print(remove_dupes([1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 8, 8, 9]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(remove_dupes(["Moo", "Moo", "Cow"]))
# ['Moo', 'Cow']

print(return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
# [2, 4, 6, 8, 10, 12, 14, 16]
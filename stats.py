def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters={}

    for letter in text.replace(" ", "").lower():
        if letter in letters:
            letters[letter]+=1
        else:
            letters[letter]=1
    return letters

def sort_on(items):
    return items["num"]

def sort_dicts(letters):
    letters_list =[]

    for letter in letters:
        letters_list.append({
            "char":letter,
            "num":letters[letter]
        })

    letters_list.sort(reverse=True, key=sort_on)

    return letters_list
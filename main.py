def listifyer(word):
    listify = list(word)
    return listify


def rearrPL(word):
    seperator = ','
    del word[-1]
    del word[-1]
    last_element = word[(len(word) - 1)]
    word.insert(0, last_element)
    del word[-1]
    new_word = seperator.join(word)
    return new_word


def rearrE(word):
    first_letter = word[0]
    seperator = ','
    word.remove(word[0])
    word.append(first_letter)
    word.append("a")
    word.append("y")
    new_word = seperator.join(word)
    return new_word


def PL2E():
    theWord = input("What word are we translating?: ")
    listified_word = listifyer(theWord)
    rearranged_word = rearrPL(listified_word)
    translated_word1 = rearranged_word.replace(",", "")
    translated_word2 = translated_word1.lower()
    translated_word3 = translated_word2.capitalize()
    print(theWord + " ----> " + translated_word3)


def E2PL():
    theWord = input("What word are we translating?: ")
    listified_word = listifyer(theWord)
    rearranged_word = rearrE(listified_word)
    translated_word1 = rearranged_word.replace(",", "")
    translated_word2 = translated_word1.lower()
    translated_word3 = translated_word2.capitalize()
    print(theWord + " ----> " + translated_word3)


def choose():
    usrint = input(
        "What are we translating to?: \npig latin or english(p/e): ")
    if usrint == "p":
        E2PL()
    elif usrint == 'e':
        PL2E()
    else:
        print("That's not an option choose (p/e)")
        choose()


choose()

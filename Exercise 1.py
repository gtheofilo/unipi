def split_into_sentences(sentence):
    lastLimit = 0
    splitted = []
    for i in range(0, len(sentence) ):
        if (sentence[i] == " " and sentence[i + 1] == sentence[i + 1].upper()):
            splitted.append(sentence[lastLimit:i])
            lastLimit = i + 1
    splitted.append(sentence[lastLimit:i + 1])
    return splitted

def mark_remover(splitted):
    newSentence = []
    for sentence in splitted:
        newStr = ""
        if (sentence[-1].isalpha()):
            for char in sentence:
                if (char != "!"):
                    newStr = newStr + char
        else:
            for i in range(-1 , -len(sentence) -1, -1):
                if (sentence[i] != "!"):
                    limit = i + len(sentence)
                    break
            for i in range(0, limit + 1):
                if (sentence[i] != "!"):
                    newStr = newStr + sentence[i]
            newStr = newStr + sentence[limit::]
        newSentence.append(newStr)
    return newSentence

print "+---------------------------------------------------+"
print "|Introduction to Computer Science - Exercise One (1)|"
print "+---------------------------------------------------+\n"
sentence = raw_input("Type your string >> ")
print "\n"
splitted = split_into_sentences(sentence)
removed = mark_remover(splitted)
for item in removed:
    print item,
a = input()

'''
Generator module
'''


from random import randint


def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yield the substrings.
    {option} precises if an action is performed on the substrings before they are yielded.
    '''
    if not isinstance(text, str) or (option != None and option not in ['shuffle', 'ordered', 'unique']):
        yield "ERROR"
        return
    shattered_text = text.split(sep)

    if option == None:
        for word in shattered_text:
            yield word
    elif option == 'shuffle':
        while shattered_text:
            i = randint(0, len(shattered_text) - 1)
            word = shattered_text[i]
            shattered_text.pop(i)
            yield word
    elif option == 'ordered':
        shattered_text.sort()
        for word in shattered_text:
            yield word
    else:
        shattered_text = list(dict.fromkeys(shattered_text))
        for word in shattered_text:
            yield word

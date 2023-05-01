import random
def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
option precise if a action is performed to the substrings before it is yielded.'''
    if not isinstance(text, str):
        yield "ERROR"
        return
    words = text.split(sep)
    if option == 'shuffle':
        newlist = []
        while len(words) > 0:
            ranum = random.randint(0, len(words) - 1)
            retword  = words[ranum]
            words.remove(words[ranum])
            yield retword
    elif option == 'unique':
        words = list(dict.fromkeys(words))    
    elif option == 'ordered':
        words.sort(key=str.lower)
    elif option != None:
        yield "ERROR"
        return
    for i in words:
            yield i



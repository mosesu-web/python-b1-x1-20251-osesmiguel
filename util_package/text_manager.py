import string
# Do not change the following lines

TEXT = '''Are the following lines palindromes?
A man, a plan, a canal, Panama.
This line is not a palindrome
Don't nod
The next one might be my favorite
Taco Cat!
Another non-palindrome
Rats live on no evil star.
If your program finds this line, it's not working
Neil, a trap! Sid is part alien!
Step on no pets.
Dammit, I'm mad!
Madam, I'm Adam.
Madam, in Eden, I'm Adam.
Rise to vote, sir.
Never odd or even
If I had a hi-fi
Yo, banana boy!
Do geese see God?
No devil lived on.
Ah, Satan sees Natasha.
Lewd did I live & evil I did dwel!
A dog, a panic in a pagoda
Was it a cat I saw?
Was it a car or a cat I saw?
A Toyota's a Toyota.
Another non-palindrome
No lemons, no melon
Now I see bees, I won.
Ma is as selfless as I am.
Nurse, I spy gypsies-run!
The next one isn't as cool as the Panama one
A dog, a plan, a canal, pagoda
Was it Eliot's toilet I saw?
Some of these are hilarious. Papaya war?!
No, sir, away! A papaya war is on!
Go hang a salami, I'm a lasagna hog.
I, madam, I made radio! So I dared! Am I mad? Am I?
Swap God for a janitor, rot in a jar of dog paws.
Eva, can I see bees in a cave?
Not a palindrome
So many dynamos!
Red rum, sir, is murder.
'''


def is_newline(character):
    # Do not change this method
    """ A function that detects the ending of a sentence. Here, the sentences are separated by a "\n". 
    If the character is this simbol it will return True.
    """
    return character == "\n"


def is_space(character):
    # Do not change this method
    """ A function that detects if a character is an blank space.
    """
    return character == " "


def remove_punctuation_marks(cad):
    # Do not change this method
    """ A function that removes punctuation marks from a word or a text.
    """
    return cad.translate(str.maketrans('', '', string.punctuation))


def split_into_words(text: str) -> list[str]:
    """ 
    Divide un texto en palabras basandose en el caracter " " para la
    división. Previamente, se eliminan todos los simbolos de puntuacion
    del texto.
    Devuelve una lista que contiene todas las palabras encontradas
    """
    word: str =''
    words_list: list[str] = []
    for character in remove_punctuation_marks(text):
        if word and (is_space(character) or is_newline(character)):
            words_list.append(word)
            word = ''
        if not is_space(character) and not is_newline(character):
            word += character
    if word:  # Si al final del bucle, ha quedado una palabra dentro de word, esta se incluye
        words_list.append(word)
    return words_list


def split_into_sentences(text: str, no_punctuation: bool = False) -> list[str]:
    """ 
    Divide un string en oraciones usando el caracter especial \n para ello.
    Si el parámetro no_punctuation tiene el valor True, entonces se eliminan
    todos los simbolos de puntuación antes de dividir el texto.
    Devuelve una lista que contiene todas las oraciones encontradas.
    """
    sentence: str = ''
    sentences_list: list[str] = []
    if no_punctuation:
        text = remove_punctuation_marks(text)
    for character in text:
        if is_newline(character):
            sentences_list.append(sentence)
            sentence = ''
        else:
            sentence += character
    if sentence:  # Si al final del bucle, ha quedado una oración dentro de sentence, esta se incluye
        sentences_list.append(sentence)

    return sentences_list

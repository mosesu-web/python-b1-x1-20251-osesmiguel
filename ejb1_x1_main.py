"""El objetivo general del ejercicio es crear una serie de funciones que nos permitan realizar operaciones 
sobre un texto.

Para este ejercicio, no se debe usar la función split de Python. En vez de ello, deberás  usar las 
siguientes funciones auxiliares que serán de gran ayuda al resolver el ejercicio. Asimismo, se pueden 
elegir crear nuevas funciones adicionales. A continuación, presentaremos una descripción de estos métodos:

* is_newline(character): Es una función que detecta el final de una oración. Deberás suponer que las frases 
están separadas por "\n" (nueva línea). Si el carácter es este símbolo, devolverá True.

* is_space(character): Es una función que detecta si un carácter es un espacio en blanco. Si el carácter es 
este símbolo, devolverá True.

* remove_punctuation_marks(cad): Una función que elimina los signos de puntuación de una palabra o un texto. 
Este método devuelve como resultado una cadena de caracteres sin signos de puntuación.

Las funciones descritas en el apartado anterior forman parte del módulo denominado 'text_manager.py', por lo tanto, 
es preciso importar estas en el módulo 'ejb1_x1_main.py', el cual es el módulo principal en el que desarrollaremos 
nuestra solución. 
En este ejercicio utilizaremos  la variable "TEXT" de tipo cadena de caracteres(definida en el módulo text_manager.py), 
la cual será empleada en cada una de las siguientes funciones como parámetro. Los métodos que se solicita 
desarrollar son:

* find_largest_word(text): Un método que permite detectar la palabra más larga en un texto. Este método debe 
devolver como resultado una cadena de caracteres correspondiente a la palabra más larga. Al evaluar la palabra
no debe contener signos de puntuación. 

* is_palindrome_word(word): Es una función recursiva que nos permitirá detectar si una palabra es palíndromo. 
Un palíndromo es una palabra que se lee igual en un sentido que en otro. Por ejemplo las siguientes palabras son 
palíndromos: Ata; Aviva; Azuza; Apa; Afromorfa. Para el ejercicio, el texto se encuentra en lengua inglesa, 
por lo que no se requiere realizar ningún tipo de acción en relación con tildes o acentos. Al evaluar la palabra 
no debe contener signos de puntuación. El valor que devuelve es de tipo booleano. Si es un palíndromo devolverá 
"True", y en el caso contrario "False". 

* count_palindrome_words(text): Se trata de una función que nos permitirá enumerar las apariciones de palíndromos 
en el texto, por lo tanto, esta retorna un número entero. Para esto debemos hacer uso de la anterior 
función is_palindrome_word(word).

* find_size_largest_sentence(text, filter): Se trata de una función que permite encontrar el tamaño de la oración 
más larga cuyo valor de filtro esté en esa sentencia. Si no existe una oración que coincida con el filtro deberá 
lanzar una excepción del tipo ValueError. El valor a retornar es un número entero que representa la longitud de 
la cadena en cuestión. 
Por ejemplo: si se invoca a la función con los parámetros text = "Hola, Pepe.\n¿Cómo estás, amigo?", el parámetro
filter = "a", este debe devolver 19, ya que en la segunda oración "¿Cómo estás, amigo?", se encuentra incluido 
el valor pasado como filtro y la oración tiene una longitud de la cadena de texto más larga. 
"""
# Add your imports here
from util_package.text_manager import TEXT, split_into_words, split_into_sentences


def find_largest_word(text: str) -> str:
    """
    Busca la palabra más larga dentro de un texto y la devuelve.
    """
    words: list[str] = split_into_words(text)
    max_word: str =''
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word


def is_palindrome_word(word: str) -> bool:
    """
    Comprueba si un string es un palindromo.
    Devuelte un valor True/False en función de si es o no un palindromo
    """
    word = word.casefold()
    if len(word) < 2:
        return True
    return word[0] == word[-1] and is_palindrome_word(word[1:-1])


def count_palindrome_words(text: str) -> int:
    """
    Divide un string en una lista de palabras y de frases y busca los palindromos dentro de esta lista.
    Devuelve el número de palindromos encontrados
    """
    palindromes: set[str] = set()
    words_list: list[str] = split_into_words(text)
    sentences_list: list[str] = split_into_sentences(text, no_punctuation= True)  # Elimina los signos de puntuación.
    for word in  words_list+sentences_list:
        if is_palindrome_word(word) and len(word)>=3:
            palindromes.add(word.casefold())
    return len(palindromes)


def find_size_largest_sentence(text: str, filter: str) -> int:
    """
    Divide un texto en oraciones y busca cual es la oración más larga
    que contiene el valor de filter. Si no encuentra ninguna oración que
    contenga el valor de filter, entonces devuelve un ValueError.
    """
    max_sentence: int = 0
    sentences = split_into_sentences(text)

    for sentence in sentences:
        if (filter in sentence) and (len(sentence) > max_sentence):
            max_sentence = len(sentence)
    if max_sentence > 0:
        return max_sentence
    else:
        raise ValueError(f'El filtro {filter} no esta presente en ninguna sentencia')


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
#print("La palabra mas larga es:", find_largest_word(TEXT))
#print("'aa' es un palíndromo su resultado es:", is_palindrome_word("aa"))
#print("'abx' no un palíndromo su resultado es:", is_palindrome_word("abx"))
#print("'a' es un palíndromo su resultado es:", is_palindrome_word("a"))
#print("'Ababa' es palíndromo su resultado es:", is_palindrome_word("Ababa"))
#print("El número de palabras identificadas como palíndromos es:", count_palindrome_words(TEXT))
#print("El tamaño de la oración más larga con el filtro='a', es :", find_size_largest_sentence(TEXT, filter="a"))

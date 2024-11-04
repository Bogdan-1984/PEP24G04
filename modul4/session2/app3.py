text = """In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de
uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile. Publicul
a aflat deja acele detalii ale crimei care au iesit la iveala in ancheta politiei; dar multe au fost
suprimate cu acea ocazie, deoarece cazul acuzarii era atat de coplesitor de puternic, incat nu era
necesar sa se prezinte toate faptele. Abia acum, la sfarsitul a aproape zece ani, imi este permis sa
aprovizionez acele verigi lipsa care alcatuiesc intregul lant remarcabil. Crima era interesanta in
sine, dar acel interes nu era nimic pentru mine in comparatie cu continuarea de neconceput, care
mi-a oferit cel mai mare soc si surpriza din orice eveniment din vitța mea aventuroasa. Chiar si
acum, dupa acest interval lung, mă trezesc emotionat cand ma gandesc la asta si simt din nou acel
potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea."""


def count_letters(python_text: str):
    counter = 0
    for letter in python_text:
        if letter.isalpha():
            counter += 1

    return counter


text_letters = count_letters(text)
print(f"Letters are {text_letters} and all characters are {len(text)}")


def get_words(python_text: str):
    result = []
    list_of_words = python_text.split()
    for word in list_of_words:
        new_word = word.strip(',.1234567890')
        if new_word:
            result.append(new_word)
    return result


list_of_words = get_words(text)
print(list_of_words)


def words_with_s(word_list: list[str]):
    for word in word_list.copy():  # try not to use copy and debug what happens
        if not word.lower().startswith('s'):
            word_list.remove(word)
    return word_list


print(words_with_s(list_of_words))
print(list_of_words)

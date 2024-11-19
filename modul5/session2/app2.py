text = """in p$imava$a anu^ui 1894, t%ata ^%nd$a a f%!t int#$#!ata, ia$
^um#a ^a m%da a f%!t &%n!t#$nata d# u&id#$#a %n%$abi^u^ui $%na^d
adai$ in &i$&um!tant# &#^# mai n#%bi!nuit# !i in#xp^i&abi^#.
pub^i&u^ a af^at d#ja a&#^# d#ta^ii a^# &$im#i &a$# au i#!it ^a
iv#a^a in an&@#ta p%^iti#i; da$ mu^t# au f%!t !up$imat# &u a&#a
%&azi#, d#%a$#&# &azu^ a&uza$ii #$a atat d# &%p^#!it%$ d#
put#$ni&, in&at nu #$a n#&#!a$ !a !# p$#zint# t%at# fapt#^#. abia
a&um, ^a !fa$!itu^ a ap$%ap# z#&# ani, imi #!t# p#$mi! !a
ap$%vizi%n#z a&#^# v#$igi ^ip!a &a$# a^&atui#!& int$#gu^ ^ant
$#ma$&abi^. &$ima #$a int#$#!anta in !in#, da$ a&#^ int#$#! nu
#$a nimi& p#nt$u min# in &%mpa$ati# &u &%ntinua$#a d# n#&%n&#put,
&a$# mi-a %f#$it &#^ mai ma$# !%& !i !u$p$iza din %$i&# #v#nim#nt
din vitța m#a av#ntu$%a!a. &@ia$ !i a&um, dupa a&#!t int#$va^
^ung, mă t$#z#!& #m%ti%nat &and ma gand#!& ^a a!ta !i !imt din
n%u a&#^ p%t%p b$u!& d# bu&u$i#, uimi$# !i n#in&$#d#$# &a$# mi-a
&ufundat &u t%tu^ mint#a."""

char = {'!': 's', '@': 'h', '#': 'e', '$': 'r', '^': 'l', '%': 'o', '&': 'c', '*': 'k'}


def decrypt(encrypted_text: str, decryption_method: dict):
    decrypted_text = ""
    for character in encrypted_text:
        if character in decryption_method:
            decrypted_text += decryption_method[character]
        else:
            decrypted_text += character
    return decrypted_text


dec_text = decrypt(text, char)

print(dec_text)
sentences = dec_text.split('.')
for sentence in sentences:
    print(80 * '#')
    # first = ''
    new_sentance = ''
    var1 = True
    for c in sentence:
        c: str
        if c.isalpha() and var1:
            c = c.upper()
            var1 = False
        new_sentance += c
    # sentence_gen = sentence.__iter__()
    # new_sentance = ''
    # for c in sentence_gen:
    #     if c.isalpha():
    #         c = c.upper()
    #         new_sentance += c
    #         new_sentance += ''.join(sentence_gen)
    #         break
    #     else:
    #         new_sentance += c
    # for c in sentence_gen:
    #     if not c.isalpha():
    #         next(sentence_gen)

    print(new_sentance)

# c)
words = dec_text.split()
print(words)
new_words = []
for word in words:
    word = word.strip(',')
    if word.isnumeric():
        continue
    new_words.append(word)
print(new_words)

# d)
print('short words')
result = []
for word in new_words:
    if 5 <= len(word) <= 8:
        result.append(word)
print(set(result))


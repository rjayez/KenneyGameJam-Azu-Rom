import sys


def nbCommonLetters(word1, word2):
    commonLetters = list(set(word1) & set(word2))
    return len(commonLetters)


def nbCommonVowelLetters(word1, word2):
    commonLetters = list(set(word1) & set(word2))
    return len(list(set(commonLetters) & set(vowels)))


def nbCommonConsonantLetters(word1, word2):
    commonLetters = list(set(word1) & set(word2))
    return len(list(set(commonLetters) & set(vowels)))



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
vowels = ['a', 'e', 'y', 'u', 'i', 'o']

mots = ['drill', 'pallet', 'computer', 'micro', 'notebook', 'mixer', 'bag', 'suitcase', 'pan', 'glass', 'screen',
        'lamp', 'camera', 'pickaxe', 'hammer', 'knife', 'card', 'compass', 'bone', 'banknote', 'money', 'wallet',
        'disk',
        'clamp', 'drug', 'ball', 'bat', 'joystiq', 'key', 'saw', 'shovel']

words = set()
for mot in mots:
    words = set(mot).union(set(words))

print(words)

dictWords = {}
print('mot avec au moins une lettre en commun')
# mot avec au moins une lettre en commun
for mot in mots:
    commonWords = []
    for mot2 in mots:
        if mot is not mot2 and nbCommonLetters(mot, mot2) > 0:
            commonWords.append(mot2)

    dictWords[mot] = commonWords

print(dictWords)

print('mot avec 2 lettres en commun')
dictWords = {}

for mot in mots:
    commonWords = []
    for mot2 in mots:
        if mot is not mot2 and nbCommonLetters(mot, mot2) > 1:
            commonWords.append(mot2)

    dictWords[mot] = commonWords

print(dictWords)

print('mot avec 1 consonnes et 1 voyelles en commun')
dictWords = {}

for mot in mots:
    commonWords = []
    for mot2 in mots:
        if mot is not mot2 and nbCommonConsonantLetters(mot, mot2) > 0 and nbCommonVowelLetters(mot, mot2) > 0:
            commonWords.append(mot2)

    dictWords[mot] = commonWords

print(dictWords)

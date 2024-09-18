#!/usr/bin/python3
# coding=utf-8
import random
from string import ascii_lowercase

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall strenger i generert instans.
n_strings_lower = 3
# Høyest mulig antall strenger i generert instans.
n_strings_upper = 8
# Laveste mulige antall tegn i hver streng i generert instans.
n_chars_lower = 3
# Høyest mulig antall tegn i hver streng i generert instans.
n_chars_upper = 15
# Antall forskjellige bokstaver som kan brukes i strengene. Må være mellom 1 og
# 26. Plukker de første `n_diff_chars` bokstavene i alfabetet.
n_diff_chars = 5
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def char_to_int(char):
    return ord(char) - 97


def sort(A, n, i):
    """
    Takes in an array of strings A,
    of size n,
    and index of i

    Sorts the words in A based on the char at position i
    Returns the sorted array
    """
    ALPHABET_SIZE = 26
    SIZE = ALPHABET_SIZE + 1
    C = [0] * SIZE
    B = [0] * n
    # count occurrences
    for word in A[0:n]:
        if i < len(word):
            char = word[i]
            C[char_to_int(char) + 1] += 1
        else:
            # word too small
            C[0] += 1
    # accumulate
    for j in range(1, SIZE):
        C[j] += C[j - 1]
    # insert
    for j in range(n - 1, -1, -1):
        word = A[j]
        if i < len(word):
            char = word[i]
            B[C[char_to_int(char) + 1] - 1] = word
            C[char_to_int(char) + 1] -= 1
        else:
            B[C[0] - 1] = word
            C[0] -= 1
    return B

def flexradix(A, n, d):
    if n <= 1:
        return A
    for i in range(d - 1, -1, -1):
        A = sort(A, n, i)
    return A

# Hardkodete instanser på format: (A, d)
tests = [
    ([], 1),
    (["a"], 1),
    (["a", "b"], 1),
    (["b", "a"], 1),
    (["a", "z"], 1),
    (["z", "a"], 1),
    (["ba", "ab"], 2),
    (["b", "ab"], 2),
    (["ab", "a"], 2),
    (["zb", "za"], 2),
    (["abc", "b"], 3),
    (["xyz", "y"], 3),
    (["abc", "b"], 4),
    (["xyz", "y"], 4),
    (["zyxy", "yxz"], 4),
    (["ab", "aaa"], 3),
    (["abc", "b", "bbbb"], 4),
    (["abcd", "abcd", "bbbb"], 4),
    (["abcd", "wxyz", "bbbb"], 4),
    (["abcd", "wxyz", "bazy"], 4),
    (["ab", "aab", "aaab", "aaaab", "aaaaab"], 6),
    (["a", "b", "c", "babcbababa"], 10),
    (["a", "b", "c", "babcbababa"], 10),
    (["w", "x", "y", "xxyzxyzxyz"], 10),
    (["b", "a", "y", "xxyzxyzxyz"], 10),
    (["jfiqdopvak", "nzvoquirej", "jfibopvmcq"], 10),
]

def gen_examples(k, nsl, nsu, ncl, ncu):
    for _ in range(k):
        strings = [
            "".join(random.choices(
                ascii_lowercase,
                k=random.randint(ncl, ncu)
            )) for _ in range(random.randint(nsl, nsu))
        ]
        yield (strings, max(map(len, strings)))


if generate_random_tests:
    ascii_lowercase = ascii_lowercase[:n_diff_chars]
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        n_strings_lower,
        n_strings_upper,
        n_chars_lower,
        n_chars_upper,
    ))

failed = False
for A, d in tests:
    answer = sorted(A)
    student = flexradix(A[:], len(A), d)
    if student != answer:
        if failed:
            print("-"*50)
        failed = True

        print(f"""
Koden feilet for følgende instans:
A: {A}
n: {len(A)}
d: {d}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")

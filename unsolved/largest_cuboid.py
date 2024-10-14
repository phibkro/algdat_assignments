#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å juste på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = True
# Antall tilfeldige tester som genereres
random_tests = 10
# Lavest mulig antall verdier i generert instans.
n_lower = 3
# Høyest mulig antall verdier i generert instans.
# NB: Om denne verdien settes høyt (>30) kan testene ta veldig lang tid.
n_upper = 25
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


def largest_cuboid(x):
    # Skriv koden din her
    pass


# Hardkodete tester
tests = [
    [[1]],
    [[1, 1], [2, 1]],
    [[1, 1], [5, 1]],
    [[0, 0], [0, 0]],
    [[10, 0], [0, 10]],
    [[10, 6], [5, 10]],
    [[100, 100], [40, 55]],
]


def generate_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        yield [random.choices(range(5 * n), k=n) for _ in range(n)]


# Treg bruteforce løsning for å finne løsnings for tilfeldig genererte tester.
def bruteforce_largest_cuboid(x):
    A = 0
    for B in range(len(x)):
        for C in range(len(x[0])):
            for D in range(B, len(x)):
                for E in range(C, len(x[0])):
                    h = min(min(y[C : E + 1]) for y in x[B : D + 1])
                    A = max(A, (D - B + 1) * (E - C + 1) * h)
    return A


if generate_random_tests:
    if seed:
        random.seed(seed)

    tests.extend(generate_examples(random_tests, n_lower, n_upper))

failed = False
for x in tests:
    student = largest_cuboid([y[:] for y in x])
    answer = bruteforce_largest_cuboid(x)
    if student != answer:
        if failed:
            print("-" * 50)

        failed = True

        print(f"""
Koden ga feil svar for følgende instans:
x: {x}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")

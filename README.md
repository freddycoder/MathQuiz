# MathQuiz
Un quiz mathématique avec voix

## Synopsis

Le projet a pour but un l'entrainement pour le calcule mentale. L'ordinateur pose les questions et les affiches dans le terminal. Pour répondre il suffit de taper la réponse et appuyer sur entrer. Ensuite l'ordinateur pose une autre question. Pour quitter il entrer x. Les opération sont l'addition, la soustraction, la multiplication, la division, la racine carré et le carré d'un nombre.

## Python packages

import random
from gtts import gTTS
from playsound import playsound


## Motivation

La motivation pour ce projet est de créé un outils simple, éfficace et facile à utiliser.

## Installation

Pour les distibutions basés sur Debian:
Télécharger le repo.
Pour faire le quiz, il faut exécuter dans un terminal le script install_requirments.
Lancer le fichier avec python3

## Hack the code

Pour des équations plus difficiles il est possible de modifier le 'range' des nombres possible pour générer l'équation. Exemple:
#Division
    if operation == 1:
        num1=random.randrange(-13, 13)
        num2=random.randrange(-13, 13)

## Contribuer

Please don't esitate.

## License

Tout droit réservé

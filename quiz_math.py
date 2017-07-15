import random
from gtts import gTTS
from playsound import playsound

print("Entrainement mathématique:")
print("Pour quitté tapper x")

run = True
bonne_reponse = 0
question_total = 0

while run == True:
#Choisir une opération au hasard
    operation = random.randrange(1, 4)

#Division
    if operation == 1:
        num1=random.randrange(2, 13)
        num2=random.randrange(2, 13)
        reponse=num1*num2

        print(str(reponse) + " / " + str(num2))
        #Text to speech section
        tts = gTTS(text="Diviser" + str(reponse) + " par " + str(num2), lang="fr")
        tts.save("question.mp3")
        playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
            print("Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.")
            #Text to speech section. Besion des module Gtts et playsound
            tts = gTTS(text="Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.", lang="fr")
            tts.save("resultat.mp3")
            playsound("resultat.mp3")
            run = False

        elif int(num1)==int(tentative):
            print("Bonne réponse")
            playsound("bonne_reponse.mp3")
            bonne_reponse += 1
            question_total += 1
        else:
            print("Mauvaise réponse")
            playsound("mauvaise_reponse.mp3")
            question_total += 1
#Multiplication
    elif operation == 2:
        num1=random.randrange(2, 13)
        num2=random.randrange(2, 13)
        reponse=num1*num2

        print(str(num1) + " x " + str(num2))
        #Text to speech section
        tts = gTTS(text="Multiplier" + str(num1) + " par " + str(num2), lang="fr")
        tts.save("question.mp3")
        playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
            print("Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.")
            #Text to speech section. Besion des module Gtts et playsound
            tts = gTTS(text="Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.", lang="fr")
            tts.save("resultat.mp3")
            playsound("resultat.mp3")
            run = False

        elif int(reponse)==int(tentative):
            print("Bonne réponse")
            playsound("bonne_reponse.mp3")
            bonne_reponse += 1
            question_total += 1
        else:
            print("Mauvaise réponse")
            playsound("mauvaise_reponse.mp3")
            question_total += 1

#Soustraction
    elif operation == 3:
        num1=random.randrange(2, 99)
        num2=random.randrange(2, 99)
        reponse=num1-num2

        print(str(num1) + " - " + str(num2))
        #Text to speech section
        tts = gTTS(text="Soustraire" + str(num1) + " de " + str(num2), lang="fr")
        tts.save("question.mp3")
        playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
            print("Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.")
            #Text to speech section. Besion des module Gtts et playsound
            tts = gTTS(text="Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.", lang="fr")
            tts.save("resultat.mp3")
            playsound("resultat.mp3")
            run = False

        elif int(reponse)==int(tentative):
            print("Bonne réponse")
            playsound("bonne_reponse.mp3")
            bonne_reponse += 1
            question_total += 1
        else:
            print("Mauvaise réponse")
            playsound("mauvaise_reponse.mp3")
            question_total += 1

#Addition
    elif operation == 4:
        num1=random.randrange(2, 99)
        num2=random.randrange(2, 99)
        reponse=num1+num2

        print(str(num1) + " + " + str(num2))
        #Text to speech section
        tts = gTTS(text="Additionner" + str(num1) + " de " + str(num2), lang="fr")
        tts.save("question.mp3")
        playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
            print("Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.")
            #Text to speech section. Besion des module Gtts et playsound
            tts = gTTS(text="Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.", lang="fr")
            tts.save("resultat.mp3")
            playsound("resultat.mp3")
            run = False

        elif int(reponse)==int(tentative):
            print("Bonne réponse")
            playsound("bonne_reponse.mp3")
            bonne_reponse += 1
            question_total += 1
        else:
            print("Mauvaise réponse")
            playsound("mauvaise_reponse.mp3")
            question_total += 1

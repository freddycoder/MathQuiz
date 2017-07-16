import random
from gtts import gTTS
from playsound import playsound

run = True
bonne_reponse = 0
question_total = 0

print("Entrainement mathématique:")
print("Pour quitté tapper x")

while run == True:
#Choisir une opération au hasard
    operation = random.randrange(1, 7)
#Division
    if operation == 1:
        num1=random.randrange(-13, 13)
        num2=random.randrange(-13, 13)
        while num1 == 0:
            num1=random.randrange(-13, 13)
        while num2 == 0:
            num2=random.randrange(-13, 13)
        reponse=num1*num2

        print(str(reponse) + " / " + str(num2))
        #Text to speech section
        if reponse < 0:
            tts = gTTS(text="Diviser moins" + str(reponse) + " par " + str(num2) + "?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        else:
            tts = gTTS(text="Diviser " + str(reponse) + " par " + str(num2) + "?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
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
        num1=random.randrange(-13, 13)
        num2=random.randrange(-13, 13)
        reponse=num1*num2

        print(str(num1) + " x " + str(num2))
        #Text to speech section
        if num1 < 0:
            tts = gTTS(text="Multiplier moins" + str(num1) + " par " + str(num2) + "?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        else:
            tts = gTTS(text="Multiplier " + str(num1) + " par " + str(num2) + "?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
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
        num1=random.randrange(-99, 99)
        num2=random.randrange(-99, 99)
        reponse=num1-num2

        print(str(num1) + " - " + str(num2))
        #Text to speech section
        if num1 < 0:
            tts = gTTS(text="Soustraire " + str(num1) + " de " + str(num2) + " ?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        else:
            tts = gTTS(text="Soustraire" + str(num1) + " de " + str(num2) + " ?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
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
        num1=random.randrange(-99, 99)
        num2=random.randrange(-99, 99)
        reponse=num1+num2

        print(str(num1) + " + " + str(num2))
        #Text to speech section
        if num1 < 0:
            tts = gTTS(text="Additionner " + str(num1) + " de " + str(num2) + "?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        else:
            tts = gTTS(text="Additionner" + str(num1) + " de " + str(num2) + "?", lang="fr")
            tts.save("question.mp3")
            playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
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
#Racine carré
    elif operation == 5:
        num1=random.randrange(2, 20)
        carre=num1*num1
        print("La racine carré de " + str(carre))
        #Speech to text section
        tts = gTTS(text="La racine carré de " + str(carre) + "?", lang="fr")
        tts.save("reponse.mp3")
        playsound("reponse.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
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
#Au carré
    elif operation == 6:
        num1=random.randrange(2, 20)
        carre=num1*num1
        print(str(num1) + " au carré")
        #Speech to text section
        tts = gTTS(text=str(num1) + " au carré" + "?", lang="fr")
        tts.save("question.mp3")
        playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
            run = False

        elif int(carre)==int(tentative):
            print("Bonne réponse")
            playsound("bonne_reponse.mp3")
            bonne_reponse += 1
            question_total += 1
        else:
            print("Mauvaise réponse")
            playsound("mauvaise_reponse.mp3")
            question_total += 1
'''
Section en construction

#Produit-somme \ Section en construction, il faut changer le randrange de operation au début de la boucle pour pour activer ce elif
    if operation == 7:
        num1=random.randrange(-13, 13)
        num2=random.randrange(-13, 13)
        num3=(num2/(2*num1))**2
        print("La somme-produit de " + str(num1) + str(num2) + str(num3) + "?")
        #Speech to text section
        tts = gTTS("La somme-produit de " + str(num1) + str(num2) + str(num3) +" ?")
        tts.save("question.mp3")
        playsound("question.mp3")
        tentative=input("Réponse : ")

        if tentative == "x":
            run = False

        elif int(carre)==int(tentative):
            print("Bonne réponse")
            playsound("bonne_reponse.mp3")
            bonne_reponse += 1
            question_total += 1
        else:
            print("Mauvaise réponse")
            playsound("mauvaise_reponse.mp3")
            question_total += 1
'''

#Réponse finale
print("Tu as eu " + str(bonne_reponse) + " bonne réponse sur " + str(question_total) + " questions.")
tts = gTTS(text="Tu as eu " + str(bonne_reponse) + " bonnes réponses sur " + str(question_total) + " questions.", lang="fr")
tts.save("resultat.mp3")
playsound("resultat.mp3")
if 100*bonne_reponse/question_total < 60:
    print("Tu n'aurais même pas eu la note de passage.")
    tts=gTTS(text="Tu n'aurais même pas eu la note de passage.", lang="fr")
    tts.save("commentaire.mp3")
    playsound("commentaire.mp3")
elif bonne_reponse == question_total:
    print("Waouw! Tu eu la bonne réponse pour tous les questions!")
    tts=gTTS(text="Waouw! Tu as eu la bonne réponse pour toutes les questions!", lang="fr")
    tts.save("commentaire.mp3")
    playsound("commentaire.mp3")
else:
    print("Bravo! Tu as passer le test!")
    tts=gTTS(text="Bravo tu as passer le test!", lang="fr")
    tts.save("commentaire.mp3")
    playsound("commentaire.mp3")

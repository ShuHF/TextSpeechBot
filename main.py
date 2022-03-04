#audio
import sys
import speech_recognition as sr
import pyttsx3 as botspeech
import random
#websitre
import webbrowser
# Press the green button in the gutter to run the script.
greeting= ["nani","Hello", "Yes that me", "Roger", "Waiting for command", "Hi"]
goodbye = ["bye bye", "Hmph", "Shutting down", "Have a good day", "Bye"]
if __name__ == '__main__':
    alice = botspeech.init()
    voices = alice.getProperty('voices')
    alice.setProperty('voice', voices[1].id)
    alice.say("Hi, I am Alice. The cutest bot in the world!")
    alice.runAndWait()
    #listening to voice
    mainvoice = sr.Recognizer()
    gameoption = sr.Recognizer()
    answer = sr.Recognizer()
    while True:

        with sr.Microphone() as source:
            if not source:
                alice.say("No mic device found")
                print("No mic device found")
                alice.say(goodbye)
                alice.runAndWait()
                exit()
            print("Speak now")
            text = mainvoice.listen(source)
            try:
                recongnizedtext = mainvoice.recognize_google(text)
                print(recongnizedtext)
                if recongnizedtext.lower() == "alice":
                    alice.say(random.choice(greeting))
                    alice.runAndWait()
                elif recongnizedtext.lower() == "dc":
                    alice.say(random.choice(goodbye))
                    alice.runAndWait()
                    sys.exit()
                elif recongnizedtext.lower() == "game":
                    alice.say("Let play guess the number, say 1 for me to guess, 2 for you to guess")
                    alice.runAndWait()
                    with sr.Microphone() as source1:
                        audio2 = gameoption.listen(source1)
                        number = random.randint(1,100)
                        try:
                            alice.say("From 1 to 100")
                            alice.runAndWait()
                            choice = gameoption.recognize_google(audio2)
                            if choice.lower() == "1":
                                counter = 0
                                upper = 100
                                lower = 1
                                alice.say("I can read your mind. 1 for higher, 2 for lower, 3 for correct answer")
                                alice.runAndWait()
                                while True:
                                    alice.say(number)
                                    alice.runAndWait()
                                    with sr.Microphone() as source2:
                                        try:
                                            audio3 = answer.listen(source2)
                                            result = answer.recognize_google(audio3)
                                            print(result)
                                            if result == "1":
                                                counter +=1
                                                upper = number
                                                alice.say("I will get it in the next try!")
                                                alice.runAndWait()
                                            elif result== "2":
                                                counter += 1
                                                lower = number + 1
                                                print(lower, upper)
                                                alice.say("I will get it in the next try!")
                                                alice.runAndWait()
                                            elif result == "6":
                                                alice.say("I am smart! HAHAHAHAHA I took {} tries".format(counter))
                                                alice.runAndWait()
                                                break
                                            number = random.randint(lower, upper)
                                        except sr.UnknownValueError:
                                            alice.say("Can't catch that")
                                            alice.runAndWait()
                            elif choice.lower() == "2":
                                alice.say("See if you can read my mind")
                                alice.runAndWait()
                                counter = 0
                                while True:
                                    with sr.Microphone() as source2:
                                        try:

                                            audio3 = answer.listen(source2)
                                            result = answer.recognize_google(audio3)
                                            number = int(number)
                                            print(number)
                                            if int(result) > number:
                                                counter +=1
                                                alice.say("Too high! You can't read my mind")
                                                alice.runAndWait()
                                            elif int(result) < number:
                                                counter +=1
                                                alice.say("Too low! You can't read my mind")
                                                alice.runAndWait()
                                            elif int(result) == number:
                                                if counter == 1:
                                                    alice.say("Well done, mortal")
                                                    alice.runAndWait()
                                                else:
                                                    alice.say("No one can read my mind,  you took {} tries".format(counter))
                                                    alice.runAndWait()
                                                break
                                        except sr.UnknownValueError:
                                            alice.say("Can't catch that")
                                            alice.runAndWait()

                        except sr.UnknownValueError:
                            print("nope. Exiting")





                elif recongnizedtext.lower() == "ligma":
                    alice.say("LICK MY BALLS")
                    alice.runAndWait()
            except sr.UnknownValueError:
                print("dont get it")

#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

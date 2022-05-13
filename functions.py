import random
import pyttsx3
import speech_recognition as sr

# voice
eng = pyttsx3.init()
voice = eng.getProperty("voices")[1].id
eng.setProperty("rate", 150)
eng.setProperty("voice", voice)


def voice(a):
    eng.say(a)
    eng.runAndWait()


# audio
recg = sr.Recognizer()


def audio1():
    with sr.Microphone() as scorue:
        print("Tell some thing")
        audio = recg.listen(scorue)

        try:
            text = recg.recognize_google(audio)
        except:
            voice("Not recognized")
    return text


def audio2():
    with sr.Microphone() as scorue:
        print("Tell some thing")
        audio = recg.listen(scorue)

        try:
            text = recg.recognize_google(audio, language="si-LK")
        except:
            voice("Not recognized")
    return text


def RandomGuessing(a, b):
    voice("Welcome to the Random Guessing Game. What is your name?")
    player = audio1()

    rnum = random.randint(a, b)
    voice("Hello {}. Guess a number from {} to {} in sinhala.".format(player, a, b))

    while True:
        try:
            unum = audio2()
            unum = int(unum)
            break
        except:
            voice("ValueError, please enter integer.")
    c = 1

    while unum != rnum:
        if unum >= a and unum <= b:
            if unum < rnum:
                voice("Please try a higher value than {}".format(unum))
            else:
                voice("Please try a lower value than {}".format(unum))

            while True:
                try:
                    unum = audio2()
                    unum = int(unum)
                    False
                except:
                    voice("ValueError, please enter integer.")
            c += 1
        else:
            voice("Restart the game and try with a guess within {} to {}".format(a, b))
            break
    else:
        if c <= 5:
            voice("You have won the game!!!")
        else:
            voice("You have lost. You have tried {} attempts. Try again".format(c))
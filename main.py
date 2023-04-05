import pyautogui as gui
import time
import PIL
import random

sayings = [":100:Yo", "Oh", "o", "O", "What?", "What??", "What???", "what?",
           "no way", "an't no way", "kys", "wdym", "lol", 
           "haha!", "HAHA", "LO",
           "L0L", "hello", "hi", "halo", "helo",
           "wtf", "tf", "?", "??", "???", "are you autistic", "autistic?",
           "what did you say", "what do you say", "what do you mean",
           "what you mean?", "I'm just minding my own buisness",
           "your stupid", "i'm stupid", "you dum", "you stubid", "funny"
           "so do u", "so", "same thing", "no way", "yeah", "ya", "Yeah",
           "$h1+", "truuue", "shut up", ":laughing:",
           "i am confused", "dat funny", "what da dog doin", "fr", "FR"
           "FR!!!", "...", "..", ".",
           "i no udrstad",
           "i would never", "bro does not understand what he saying",
           "no u", "bonjur", "same difference", "how do you know"
           "why would you know", "its all the same thing", "bozo",
           "what you sayin", "WW2", "irl", "bro", "BRO",
           "bro does not know what he is sayin fr", "FOR REAL?", "FR?",
           "why..."]

while (1):
    gui.write(sayings[random.randint(0, len(sayings) - 1)])
    time.sleep(random.random() * 2)
    gui.write("\n")
    time.sleep(random.random() * 2)

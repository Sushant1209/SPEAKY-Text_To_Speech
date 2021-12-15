# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The  text file that you want to convert to audio

fh = open("text.txt", "r")
mytext = fh.read().replace("\n","")

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# output
myobj.save("output.mp3")
#close file handler by function called close
fh.close()
# Playing the converted file
os.system("output.mp3")

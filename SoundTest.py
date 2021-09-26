# Tone Sorting Algorithm "NoteKnower" By Timothy Colledge, Hunter Allen, and Kevin Cavicchia
# CITE: Timothy Colledge
# CITE: Hunter Allen
# CITE: Kevin Cavicchia
# Libraries Used:
#   numpy - https://numpy.org/
#   random - https://docs.python.org/3/library/random.html
#   cs101audio - No Online Documentation [Source Files in ]
# Software Used
#   Thonny 
#   Visual Studio Code
#   GitHub
#   YTMP3 - https://ytmp3.cc/en21/

#Imports
from cs101audio import *
import numpy as np
import random

#Var Declaration
UserInputNotes = []
Notes = []
notesSounds = []
noteStringsLetters = ["C","D","E","F","G","A","B"]
noteStringsNumbers = np.arange(0, 9).tolist()
count = 0

#Function for Note Making returns 1 in order to increase counter Var this could allow for note creation using a different data set if desired
def MakeNote(count,String, Letter):
    notesSounds.append(generate_music_note(noteStringsLetters[Letter]+str(noteStringsNumbers[String]),4,"Square"))
    notesSounds[count].apply_gain(100)
    return 1

#Generating Musical Note Sounds C scale sharps flats non-inclusive
for nString in range(9):
    for nLetter in range(7):
        count += MakeNote(count,nString,nLetter)
        

#Note Class
#Stores Sounds and the note Index info stored as Ints
class Note:
  def __init__(self, note, letter, octave):
      self.Sound = note
      self.Octave = octave
      if (letter == "C"): self.Letter = 0
      if (letter == "D"): self.Letter = 1
      if (letter == "E"): self.Letter = 2
      if (letter == "F"): self.Letter = 3
      if (letter == "G"): self.Letter = 4
      if (letter == "A"): self.Letter = 5
      if (letter == "B"): self.Letter = 6


#Resetting count for next loop
count = 0 

#Creating Note Objects
for note in range(9):
    for note2 in range(7):       
        Notes.append(Note(notesSounds[count],noteStringsLetters[note2],noteStringsNumbers[note]))
        count += 1

#Blank Note used for mixing algorithm and sorting algorithm
blank = Note(notesSounds[0],noteStringsLetters[0],noteStringsNumbers[0])

#Mixing Algorithm (A simplified variation of Fisher-Yates ["inside-out"])
for scramble in range(63):
    blank = Notes[scramble]
    randIndex = random.randint(0,62)
    Notes[scramble] = Notes[randIndex]
    Notes[randIndex] = blank

# Both Loops Below are the sorting algorithms used to to sort the notes 
# They use bubble sort by first sorting on "Octave" and then loop 2 does the "Letter" inside the octave

for x in range (len(Notes)):
    for y in range (len(Notes)-1):
        if Notes[y].Octave > Notes[y+1].Octave:
            blank = Notes[y+1]
            Notes[y+1] = Notes[y]
            Notes[y] = blank

for x in range (len(Notes)):
    for y in range (len(Notes)-1):
        if Notes[y].Letter > Notes[y+1].Letter and Notes[y].Octave == Notes[y+1].Octave:
                    blank = Notes[y+1]
                    Notes[y+1] = Notes[y]
                    Notes[y] = blank        
                    Notes[y].Sound.play() # This is for demonstration purposes only -- no need in final product

# This plays your sorted list and prints them as the paired notes
for x in range(63):
    print(x,Notes[x].Octave,Notes[x].Letter)
    Notes[x].Sound.play()   